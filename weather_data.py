__author__ = 'Fritz'

import urllib.request
import datetime


env_canada_filename={'6167865':'toronto_city_almanac_extremes.csv'}

def convert_k_to_c(k):
    return k - 273.15

def get_min_max(city_id = 6167865):
    weather_html = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?id={0}&APPID=530a8105af624df4a72b492620c0b287".format(city_id))
    weather = eval(weather_html.read())
    min_current = convert_k_to_c(weather['main']['temp_min'])
    max_current = convert_k_to_c(weather['main']['temp_max'])
    return min_current,max_current

def get_environment_canada_date_dict(filename, month, day):
    csv_file = open(filename)
    while True:
        csv_date = csv_file.readline()
        line_list = csv_date.split(',')
        if len(line_list) == 1:
            return {}
        if line_list[0] == str(month) and line_list[1] == str(day):
            return parse_environment_canada_line(line_list)


def parse_environment_canada_line(csv_date):
    weather_dict = {}
    weather_dict['Month'] = csv_date[0]
    weather_dict['Day'] = csv_date[1]
    weather_dict['AvgMaxTemp'] = csv_date[2]
    weather_dict['AvgMinTemp'] = csv_date[3]
    weather_dict['FreqOfPrecip'] = csv_date[4]
    weather_dict['HighestTemp'] = csv_date[5]
    weather_dict['HighestTempYear'] = csv_date[6]
    weather_dict['HighestTempPeriod'] = csv_date[7]
    weather_dict['HighestTempDatQual'] = csv_date[8]
    weather_dict['LowestTemp'] = csv_date[9]
    weather_dict['LowestTempYear'] = csv_date[10]
    weather_dict['LowestTempPeriod'] = csv_date[11]
    weather_dict['LowestTempDatQual'] = csv_date[12]
    weather_dict['GreatestPrecip'] = csv_date[13]
    weather_dict['GreatestPrecipYear'] = csv_date[14]
    weather_dict['GreatestPrecipPeriod'] = csv_date[15]
    weather_dict['GreatestPrecipDatQual'] = csv_date[16]
    weather_dict['GreatestRainfall'] = csv_date[17]
    weather_dict['GreatestRainfallYear'] = csv_date[18]
    weather_dict['GreatestRainfallPeriod'] = csv_date[19]
    weather_dict['GreatestRainfallDatQual'] = csv_date[20]
    weather_dict['GreatestSnowfall'] = csv_date[21]
    weather_dict['GreatestSnowfallYear'] = csv_date[22]
    weather_dict['GreatestSnowfallPeriod'] = csv_date[23]
    weather_dict['GreatestSnowfallDatQual'] = csv_date[24]
    weather_dict['MostSnowOnGround'] = csv_date[25]
    weather_dict['MostSnowOnGroundYear'] = csv_date[26]
    weather_dict['MostSnowOnGroundPeriod'] = csv_date[27]
    weather_dict['MostSnowOnGroundDatQual'] = csv_date[28]
    return weather_dict

class DateInfo:
    def __init__(self, city_id):
        self.city_id = city_id
        time_now = datetime.datetime.utcnow() - datetime.timedelta(hours=5)
        self.data_info = get_environment_canada_date_dict(env_canada_filename[self.city_id],time_now.month, time_now.day)
        print(self.data_info)

    def get_max_avg(self):
        return float(self.data_info['AvgMaxTemp'])

    def get_min_avg(self):
        return float(self.data_info['AvgMinTemp'])

    def get_max_extrm(self):
        return float(self.data_info['HighestTemp'])

    def get_max_extreme_year(self):
        return int(self.data_info['HighestTempYear'])

    def get_min_extrm(self):
        return float(self.data_info['LowestTemp'])

    def get_min_extreme_year(self):
        return int(self.data_info['LowestTempYear'])

    def get_max_rain_tuple(self):
        return float(self.data_info['GreatestRainfall']), int(self.data_info['GreatestRainfallYear'])

    def get_max_snow_accumulation_tuple(self):
        return float(self.data_info['MostSnowOnGround']), int(self.data_info['MostSnowOnGroundYear'])

    def get_max_snowfall_tuple(self):
        return float(self.data_info['GreatestSnowfall']), int(self.data_info['GreatestSnowfallYear'])

    def get_greatest_precip_tuple(self):
        return float(self.data_info['GreatestPrecip']), int(self.data_info['GreatestPrecipYear'])

historic_max_avg={'6167865':{'1':-0.7,'2':0.4, '3':4.7,'4':11.5,'5':18.4, '6':23.8,'7':26.6,'8':25.5,'9':21.0,'10':14.0,'11':7.5, '12':2.1}}
historic_max_extreme={'6167865':{'1':16.1,'2':14.4, '3':26.7,'4':32.2,'5':34.4,'6':36.7,'7':40.6,'8':38.9,'9':37.8,'10':30.0,'11':23.9, '12':19.9}}

historic_min_avg={'6167865':{'1':-6.7,'2':-5.6,'3':-1.9,'4':4.1,'5':9.9,'6':14.9,'7':18.0,'8':17.4,'9':13.4,'10':7.4,'11':2.3,'12':-3.1}}
historic_min_extreme={'6167865':{'1':-32.8,'2':-31.7,'3':-26.7,'4':-15.0,'5':-3.9, '6':-2.2,'7':3.9,'8':4.4,'9':-2.2,'10':-8.9,'11':-20.6, '12':-30}}

def get_historic_avg(month, city_id = 6167865):
    return historic_min_avg[str(city_id)][str(month)], historic_max_avg[str(city_id)][str(month)]

def get_historic_extreme(month, city_id = 6167865):
    return historic_min_extreme[str(city_id)][str(month)], historic_max_extreme[str(city_id)][str(month)]
