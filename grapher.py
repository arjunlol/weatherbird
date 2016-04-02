import matplotlib.pyplot as plot
import datetime
import data_display
import numpy as np
import os
import twit_bot
import matplotlib.pyplot as plt
from sys import argv

if __name__ == "__main__":

    if len(argv) < 2:
        print("Please provide city name")
        city_name = 'Toronto'
    else:
        city_name = argv[1]

    start_date = datetime.datetime.utcnow() - datetime.timedelta(days = 7)
    end_date = datetime.datetime.utcnow()

    logged_data_by_date = data_display.get_city_logged_data(city_name, start_date, end_date)

    high = 0
    low = 0
    avg = 0

    highs = []
    lows = []

    avg_highs = []
    avg_lows = []

    temp = []

    index = 0
    x_index = []
    labels = []
    for value in logged_data_by_date:
        for entry in value:
            highs.append(entry.high)
            lows.append(entry.low)
            temp.append((float(entry.high) + float(entry.low))/2)
            avg_highs.append(entry.seasonal_high)
            avg_lows.append(entry.seasonal_low)
            x_index.append(index)
            index += 1

            if (index - 12)%24 == 0:
                labels.append(entry.date[5:])
            else:
                labels.append('')

            if entry.high > entry.seasonal_high:
                high += 1
            elif entry.low < entry.seasonal_low:
                low += 1
            else:
                avg += 1
    print ("high: {0} low: {1}: avg: {2}".format(high, low, avg))

    ax = plt.gca()
    ax.set_axis_bgcolor('#D3D3D3')

    plt.plot(x_index,temp, color = 'black', label = 'Temperature')
    plt.plot(x_index,avg_highs, color = 'r', label = 'Seasonal High')
    plt.plot(x_index,avg_lows, color = 'b', label = 'Seasonal Low')
    plt.xticks(x_index, labels, rotation='horizontal')
    plt.xlabel('Date', fontsize=18)
    plt.ylabel('Temperature (°C)', fontsize=16)
    plt.legend(loc=2,prop={'size':10})
    filename = "weekly_trends"
    plt.savefig(filename)

    twit = twit_bot.account(city_name)
    twit.tweet_message_with_photo("Last week's temperature trends:\n", filename+'.png', city_name)
    os.remove(filename+'.png')



