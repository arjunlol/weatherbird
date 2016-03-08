import urllib.request
import datetime
import accounts
from city_id import city_id

weather_dir = 'historic_weather_data//'
env_canada_filename = {city_id['Toronto'] : 'historic_weather_data//toronto_city_almanac_extremes.csv',
                     city_id['Ottawa'] : 'historic_weather_data//ottawa_almanac_extremes.csv',
                     city_id['Vancouver'] : 'historic_weather_data//vancouver_almanac_extremes.csv',
                     city_id['Montreal'] : 'historic_weather_data//vancouver_almanac_extremes.csv'}

class HistoricInfoForCity:
    def __init__(self, city_id):
        self.city_id = city_id
        time_now = datetime.datetime.utcnow() - datetime.timedelta(hours=5)
        self.data_info = get_environment_canada_date_dict(env_canada_filename[self.city_id],time_now.month, time_now.day)
        print(self.data_info)
        self.max_avg = float(self.data_info['AvgMaxTemp'])
        self.min_avg = float(self.data_info['AvgMinTemp'])
        self.max_extrm =  float(self.data_info['HighestTemp'])
        self.min_extrm =  float(self.data_info['LowestTemp'])
        self.max_extrm_yr = int(self.data_info['HighestTempYear'])
        self.min_extrm_yr = int(self.data_info['LowestTempYear'])
        self.max_rain = float(self.data_info['GreatestRainfall'])
        self.max_rain_yr = int(self.data_info['GreatestRainfallYear'])
        self.max_snow = float(self.data_info['GreatestSnowfall'])
        self.max_snow_yr = int(self.data_info['GreatestSnowfallYear'])
        self.max_snow_accum = float(self.data_info['MostSnowOnGround'])
        self.max_snow_accum_yr = int(self.data_info['MostSnowOnGroundYear'])
        self.max_precip = float(self.data_info['GreatestPrecip'])
        self.max_precip_yr = int(self.data_info['GreatestPrecipYear'])

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

def convert_k_to_c(k):
    return k - 273.15

def get_current_min_max_tuple(city_id = 6167865):
    weather_html = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?id={0}&{1}".format(city_id,accounts.open_weather_map_api_key))
    weather = eval(weather_html.read())
    min_current = convert_k_to_c(weather['main']['temp_min'])
    max_current = convert_k_to_c(weather['main']['temp_max'])
    return round(min_current,1),round(max_current,1)
