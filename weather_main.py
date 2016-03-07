import weather_data
import datetime
import twit_bot

from city_id import toronto_id

if __name__ == "__main__":

    now = datetime.datetime.utcnow() - datetime.timedelta(hours=5)

    city_hist_dict = weather_data.DateInfo(toronto_id)

    min_current, max_current = weather_data.get_min_max()
    min_current=round(min_current,1)
    max_current=round(max_current,1)
    min_hist_extreme = city_hist_dict.get_min_extrm()
    max_hist_extreme = city_hist_dict.get_max_extrm()
    min_hist_avg = city_hist_dict.get_min_avg()
    max_hist_avg = city_hist_dict.get_max_avg()
    print("min: {0} max: {1}\nmin_avg: {2} max_avg: {3}\nmin_extreme: {4} max_extreme: {5}".format(round(min_current,1), round(max_current,1), min_hist_avg, max_hist_avg,min_hist_extreme, max_hist_extreme))

    twit = twit_bot.account()

    if(min_current < min_hist_extreme):
        twit.tweet_min_extreme(min_current,min_hist_extreme)
    elif(max_current > max_hist_extreme):
        twit.tweet_max_extreme(max_current,max_hist_extreme)
    elif(min_current < min_hist_avg):
        twit.tweet_min_avg(min_current,min_hist_avg)
    elif(max_current > max_hist_avg):
        twit.tweet_max_avg(max_current,max_hist_avg)

