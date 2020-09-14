from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from requests import Response

def get_weather(city):
    import requests
   

    web = 'https://openweathermap.org/data/2.5/weather?q='
    key = '&appid=439d4b804bc8187953eb36d2a8c26a02'
    

    
    json_data = requests.get(web + city + key).json()
    



    

    longitude = json_data ['coord']['lon']
    latitude = json_data ['coord']['lat']
    state_weather = json_data ['weather'][0]['main']
    des_weather = json_data ['weather'][0]['description']
    temp = json_data ['main']['temp']
    
    temp_min = json_data ['main']['temp_min']
    temp_max = json_data ['main']['temp_max']
    pressure = json_data ['main']['pressure']
    humidity = json_data ['main']['humidity']
    wind_speed = json_data ['wind']['speed']
    clouds = json_data ['clouds']['all']
    country = json_data ['sys']['country']
    city_name = json_data ['name']
    icon = json_data ['weather'][0]['icon']
    l1= 'Your city is '+city_name+ ' in '+ country+'\n ' 
    l2='Coordination of '+city_name+ ' is : Latitude: '+ str(latitude) + ' , Langtitude: '+ str(longitude)+'.\n' 
    l3='State of weather is '+des_weather+'.\n'
    l4='Temperature of '+city_name+ ' is '+str(temp)+ ' degree celsius.\n' 
    l4_1= 'Minimum tepmerature is ' + str(temp_min)+ ' degree celsius'
    l4_2= 'and maximun temperatue is '+str(temp_max)+' degree celsius.\n'
    l5='The humidity value of '+city_name+ ' is : '+str(humidity)+'.\n'
    l6='The pressure value of '+city_name+ ' is : '+str(pressure)+'.\n'
    l7='The clouds value of '+city_name+ ' is : '+str(clouds)+' and speed of wind is '+str(wind_speed)+' m/s.'
    destotal= l1+l2+l3+l4+l4_1+l4_2+l5+l6+l7
    final=(longitude,latitude,state_weather,des_weather,str(temp),str(temp_min),str(temp_max),str(pressure),
    str(humidity),str(wind_speed),str(clouds),country,city_name,icon,destotal)
    print (final)
    return final



def home(request):


 
    

        
     city= request.GET.get('city')
     print(city)
     city = str(city)
     city =city.capitalize()
     print(city)
     result= get_weather(city)

     
     if result[12] == city:
         context = {
            'longitude' : result[0],
            'latitude' : result[1],
            'state_weather': result[2],
            'des_weather': result[3],
            'temp': result[4],
            'temp_min': result[5],
            'temp_max': result[6],
            'pressure': result[7],
            'humidity': result[8],
            'wind_speed': result[9] + '  m/s',
            'clouds': result[10],
            'country': result[11],
            'city_name': result[12],
            'icon': result[13]+'.png',
            'destotal': result[14],
           }
         
     else:
         context = {
            'longitude' : "....",
            'latitude' : "....",
            'state_weather': "....",
            'des_weather': "....",
            'temp': "....",
            'temp_min': "....",
            'temp_max': "....",
            'pressure': "....",
            'humidity': "....",
            'wind_speed': "....",
            'clouds': "....",
            'country': "....",
            'city_name': "....",
            'icon': "....",
            'destotal': "....",
           } 
     
         
     return render(request,'core/index.html',context)
    
     
