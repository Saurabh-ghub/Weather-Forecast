from django.shortcuts import render
import urllib.request
import json
# Create your views here.
def index(request):
    if request.method=='POST':
        city=request.POST.get('city')
     
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+ city + '&units=metric&appid=5bb52a468dde73a89314f2e7653fb9cc').read()
        data_list=json.loads(source)
        data={
            "city":city,
            "country_code":str(data_list['sys']['country']),
            "coordinate":str(data_list['coord']['lon'])+','+ str(data_list['coord']['lat']),
            "temp":str(data_list['main']['temp']) + ' Celsius',
            "pressure":str(data_list['main']['pressure']),
            "humidity":str(data_list['main']['humidity']),
            "main":str(data_list['weather'][0]['main']),
            "description":str(data_list['weather'][0]['description']),
            "icon":str(data_list['weather'][0]['icon']),
        }
    else:
        data={}
       
    return render(request,'index.html',data)
