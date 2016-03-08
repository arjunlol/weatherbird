from datetime import datetime

def log_to_file(filename, current_min, current_max, record_min, record_max, datetime_info):
    f = open(filename,'a+')
    f.write("{0},{1},{2},{3},{4}\n".format(current_min, current_max, record_min, record_max, str(datetime_info.time())))

