from django.shortcuts import render
import requests, json 
import datetime  
from datetime import date 
 


def index(request):
    return render(request, 'index.html')
# Create your views here.

def forcast(city_name):
    units = "&units=metric"
    api_key = "API_KEY"
    base = "api.openweathermap.org/data/2.5/forecast?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name + units
    #"api.openweathermap.org/data/2.5/forecast?appid=d659a0b19c7e0e6fb7d28dc9c90668b5&q=lucknow"
   
    full = requests.get(complete_url.format(city)).json()
    day = datetime.datetime.today()
    today_date = int(day.strftime('%d'))
    forcast_data_list = {}
    for c in range(0, full['cnt']):
        date_var1 = full['list'][c]['dt_txt']
        date_time_obj1 = datetime.datetime.strptime(date_var1, '%Y-%m-%d %H:%M:%S')
        if int(date_time_obj1.strftime('%d')) == today_date or int(date_time_obj1.strftime('%d')) == today_date+1:
            if int(date_time_obj1.strftime('%d')) == today_date+1:
                today_date += 1
            forcast_data_list[today_date] = {}
            forcast_data_list[today_date]['day']  = date_time_obj1.strftime('%A')
            forcast_data_list[today_date]['date'] = date_time_obj1.strftime('%d %b, %Y')
            forcast_data_list[today_date]['time'] = date_time_obj1.strftime('%I:%M %p')
            forcast_data_list[today_date]['FeelsLike'] = full['list'][c]['main']['feels_like']

            forcast_data_list[today_date]['temperature'] = full['list'][c]['main']['temp']
            forcast_data_list[today_date]['temperature_max'] = full['list'][c]['main']['temp_max']
            forcast_data_list[today_date]['temperature_min'] = full['list'][c]['main']['temp_min']

            forcast_data_list[today_date]['description'] = full['list'][c]['weather'][0]['description']
            forcast_data_list[today_date]['icon'] = full['list'][c]['weather'][0]['icon']

            today_date += 1
        else:
            pass
    
        context = { 'weather' : weather, 'forcast_data_list' : forcast_data_list}
    return  render(request, 'index.html', context)    



def getTemperature(request):
    x = datetime.datetime.now()
    current_date = x.date
    current_day = x.strftime("%A") 

  

    city_name = request.GET['textInput']
   
    city_name = 'Delhi'
    
  
    units = "&units=metric"

    api_key = "d659a0b19c7e0e6fb7d28dc9c90668b5"
    weather_url = "http://api.openweathermap.org/data/2.5/weather?"
    weather_complete_url = weather_url + "appid=" + api_key + "&q=" + city_name + units
    response = requests.get(weather_complete_url.format(city_name)).json()

    base_url = 'http://api.openweathermap.org/data/2.5/forecast?'

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name + units

    val = response["wind"]["deg"]
    compassSector = ["North", "NorthNorthEast", "NorthEast", "EastNorthEast", "East", "EastSouthEast", "SouthEast", "South", "SouthSouthWest", "SoutWest", "WestSouthWest", "West", "WestNorthWest", "NothWest", "NorthNorthWest", "North"];
    wind_direction = compassSector[round(val / 22.5) - 1];
    city_weather = {
        'city' : response['name'],
        'temperature' : response["main"]["temp"],
        'description' : response['weather'][0]['description'],
        'icon' : response['weather'][0]['icon'],
        'humidity' : response["main"]["humidity"],
        'wind' : response["wind"]["speed"],
        'wind_name' : wind_direction,
        'day' : current_day,
        'date' : current_date


    }
    #"api.openweathermap.org/data/2.5/forecast?appid=d659a0b19c7e0e6fb7d28dc9c90668b5&q=lucknow"
   
    full = requests.get(complete_url.format(city_name)).json()
    day = datetime.datetime.today() + datetime.timedelta(days=1)
    
    today_date = int(day.strftime('%d'))
    forcast_data_list = {}
    for c in range(0, full['cnt']):
        date_var1 = full['list'][c]['dt_txt']
        date_time_obj1 = datetime.datetime.strptime(date_var1, '%Y-%m-%d %H:%M:%S')
        if int(date_time_obj1.strftime('%d')) == today_date or int(date_time_obj1.strftime('%d')) == today_date + 1:
            if int(date_time_obj1.strftime('%d')) == today_date+1:
                today_date += 1
            forcast_data_list[today_date] = {}
            forcast_data_list[today_date]['day']  = date_time_obj1.strftime('%A')
            forcast_data_list[today_date]['date'] = date_time_obj1.strftime('%d %b, %Y')
            forcast_data_list[today_date]['time'] = date_time_obj1.strftime('%I:%M %p')
            forcast_data_list[today_date]['FeelsLike'] = full['list'][c]['main']['feels_like']

            forcast_data_list[today_date]['temperature'] = full['list'][c]['main']['temp']
            forcast_data_list[today_date]['temperature_max'] = full['list'][c]['main']['temp_max']
            forcast_data_list[today_date]['temperature_min'] = full['list'][c]['main']['temp_min']

            forcast_data_list[today_date]['description'] = full['list'][c]['weather'][0]['description']
            forcast_data_list[today_date]['icon'] = full['list'][c]['weather'][0]['icon']

            today_date += 1
        else:
            pass
    
        context = {'city_weather' : city_weather, 'forcast_data_list' : forcast_data_list}
    return  render(request, 'index.html', context)    

    # units = "&units=metric"
    # api_key = "d659a0b19c7e0e6fb7d28dc9c90668b5"
    # base_url = "http://api.openweathermap.org/data/2.5/weather?"
    # complete_url = base_url + "appid=" + api_key + "&q=" + city + units
    # response = requests.get(complete_url.format(city)).json()
    # 
    
    # city_weather = {
    #     'city' : response['name'],
    #     'temperature' : response["main"]["temp"],
    #     'description' : response['weather'][0]['description'],
    #     'icon' : response['weather'][0]['icon'],
    #     'humidity' : response["main"]["humidity"],
    #     'wind' : response["wind"]["speed"],
    #     'wind_name' : wind_direction,
    #     'day' : current_day,
    #     'date' : current_date


    # }
    # context = {'city_weather' : city_weather}
    # print('current_day' + current_day)

    # return render(request,'index.html', context)
  
