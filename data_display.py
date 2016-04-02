from datetime import datetime, timedelta

class LoggedDataEntry:
    def __init__(self):
        self.low = None
        self.high = None
        self.seasonal_low = None
        self.seasonal_high = None
        self.extreme_low = None
        self.extreme_high = None
        self.date = None
        self.time = None

def log_to_file(filename, current_min, current_max, avg_min, avg_max, record_min, record_max, datetime_info):
    f = open(filename,'a+')
    f.write("{0},{1},{2},{3},{4},{5},{6}\n".format(current_min, current_max, avg_min, avg_max, record_min, record_max, str(datetime_info.time())))

def read_file_contents(filename, city):
    logged_data = []
    date = filename[(len(city) + len('data//') + 1):]
    f = open(filename, 'r')
    for line in iter(f.readline, b''):
        entry = LoggedDataEntry()
        entry.date = date
        entry_list = line.split(',')
        if len(entry_list) < 6:
            break
        entry.low = entry_list[0]
        entry.high = entry_list[1]
        entry.seasonal_low = entry_list[2]
        entry.seasonal_high = entry_list[3]
        entry.extreme_low = entry_list[4]
        entry.extreme_high = entry_list[5]
        entry.time = entry_list[6].rstrip('\n')
        logged_data.append(entry)

    return logged_data


def get_city_logged_data(city_name, date_start, date_end):
    logged_data = []

    day = date_start
    while day < date_end:
        filename = 'data//{0}-{1}'.format(city_name,str(day.date()))
        logged_data.append(read_file_contents(filename, city_name))
        day = day + timedelta(days=1)
    return logged_data

