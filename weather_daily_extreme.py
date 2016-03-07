__author__ = 'Fritz'
import weather_data
import twit_bot
import datetime
import random

from city_id import toronto_id

hashtags = ['#makeupyourmind ','#fromthevault ','#wildweather ','#xweather ']
snow_hashtags = ['#toqueson ','#snowday ','#frosty ','#blzrd ', '#snowday ']
rain_hashtags = ['#wetpets ','#brella ','#catsndogs ','#monsoon ']

if __name__ == "__main__":

    now = datetime.datetime.utcnow() - datetime.timedelta(hours=5)

    city_hist_dict = weather_data.DateInfo(toronto_id)
    min_hist_extreme = city_hist_dict.get_min_extrm()
    max_hist_extreme = city_hist_dict.get_max_extrm()
    min_extreme_year = city_hist_dict.get_min_extreme_year()
    max_extreme_year = city_hist_dict.get_max_extreme_year()
    max_rain, max_rain_year = city_hist_dict.get_max_rain_tuple()
    max_snow_accumulation, max_snow_accumulation_year = city_hist_dict.get_max_snow_accumulation_tuple()
    max_snowfall, max_snowfall_year = city_hist_dict.get_max_snowfall_tuple()

    message = "{0} {1} Extremes:\n".format(now.strftime("%b"), now.day)
    message += "High: {0} C ({1})\n".format(max_hist_extreme,max_extreme_year)
    message += "Low: {0} C ({1})\n".format(min_hist_extreme,min_extreme_year)

    it_rained = False
    it_snowed = False

    if(max_rain > 0):
        message_to_add = "Rain: {0} mm ({1})\n".format(max_rain, max_rain_year)
        if(len(message+message_to_add) < 140):
            message += message_to_add
            it_rained = True

    if(max_snowfall > 0):
        message_to_add = "Snow: {0} cm ({1})\n".format(max_snowfall,max_snowfall_year)
        if(len(message+message_to_add) < 140):
            message += message_to_add
            it_snowed = True

    if(max_snow_accumulation > 0):
        message_to_add = "Depth: {0} cm ({1})\n".format(max_snow_accumulation,max_snow_accumulation_year)
        if(len(message+message_to_add) < 140):
            message += message_to_add

    message_to_add = random.choice(hashtags)
    if(len(message+message_to_add) < 140):
        message += message_to_add

    if(it_rained):
        message_to_add = random.choice(rain_hashtags)
        if(len(message+message_to_add) < 140):
            message += message_to_add

    if(it_snowed):
        message_to_add =  message_to_add = random.choice(snow_hashtags)
        if(len(message+message_to_add) < 140):
            message += message_to_add


    print(len(message))
    print(message)

    twit = twit_bot.account()
    twit.custom_message(message)
