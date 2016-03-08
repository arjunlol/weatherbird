from sys import argv

import weather_data
import twit_bot
import datetime
import random

from city_id import city_id

hashtags = ['#makeupyourmind ','#fromthevault ','#wildweather ','#xweather ']
snow_hashtags = ['#toqueson ','#snowday ','#frosty ','#blzrd ', '#snowday ']
rain_hashtags = ['#wetpets ','#brella ','#catsndogs ','#monsoon ']

if __name__ == "__main__":

    if len(argv) < 2:
        print("City defaulting to Toronto, enter city name as argument to override")
        city_name = 'Toronto'
    else:
        city_name = argv[1]

#Timezone info static on EST for now
    now = datetime.datetime.utcnow() - datetime.timedelta(hours=5)

#Initialize historic info for city
    city_hist_info = weather_data.HistoricInfoForCity(city_id[str(city_name)])

    it_rained = False
    it_snowed = False

    message = "{0} {1} Extremes:\n".format(now.strftime("%b"), now.day)
    message += "High: {0} C ({1})\n".format(city_hist_info.max_extrm, city_hist_info.max_extrm_yr)
    message += "Low: {0} C ({1})\n".format(city_hist_info.min_extrm, city_hist_info.min_extrm_yr)


    if(city_hist_info.max_rain > 0):
       message_to_add = "Rain: {0} mm ({1})\n".format(city_hist_info.max_rain, city_hist_info.max_rain_yr)
       if twit_bot.combined_less_than_140(message, message_to_add):
           message += message_to_add
           it_rained = True

    if(city_hist_info.max_snow > 0):
        message_to_add = "Snow: {0} cm ({1})\n".format(city_hist_info.max_snow,city_hist_info.max_snow_yr)
        if twit_bot.combined_less_than_140(message, message_to_add):
            message += message_to_add
            it_snowed = True

    if(city_hist_info.max_snow_accum > 0):
        message_to_add = "Depth: {0} cm ({1})\n".format(city_hist_info.max_snow_accum,city_hist_info.max_snow_accum_yr)
        if twit_bot.combined_less_than_140(message, message_to_add):
            message += message_to_add

#add hashtags from hashtag lists

    message = twit_bot.add_if_less_than_140(message, random.choice(hashtags))

    if(it_rained):
        message = twit_bot.add_if_less_than_140(message, random.choice(rain_hashtags))
    if(it_snowed):
        message = twit_bot.add_if_less_than_140(message, random.choice(snow_hashtags))

    print(len(message))
    print(message)

    twit = twit_bot.account()
    twit.custom_message(message)
