import weather_data
import datetime
import twit_bot
from sys import argv

from city_id import city_id

if __name__ == "__main__":


    now = datetime.datetime.utcnow() - datetime.timedelta(hours=5)

    if len(argv) < 2:
        print("Please provide city name as arg, assuming Toronto")
        city_name = 'Toronto'
    else:
        city_name = argv[1]

    hist_weather = weather_data.HistoricInfoForCity(city_id[city_name])
    min_current, max_current = weather_data.get_current_min_max_tuple(city_id = city_id[city_name])

    print("min: {0} max: {1}\nmin_avg: {2} max_avg: {3}\nmin_extreme: {4} max_extreme: {5}".format(round(min_current,1), round(max_current,1), hist_weather.min_avg, hist_weather.max_avg,hist_weather.min_extrm, hist_weather.max_extrm))

    twit = twit_bot.account()

    if(min_current < hist_weather.min_extrm):
        twit.tweet_min_extreme(min_current, hist_weather.min_extreme, city_name)
    elif(max_current >  hist_weather.max_extrm):
        twit.tweet_max_extreme(max_current, hist_weather.max_extrm, city_name)
    elif(min_current <  hist_weather.min_avg):
        twit.tweet_min_avg(min_current, hist_weather.min_avg, city_name)
    elif(max_current >  hist_weather.max_avg):
        twit.tweet_max_avg(max_current, hist_weather.max_avg, city_name)

