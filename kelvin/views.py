from django.shortcuts import render
import json
import urllib.request
from datetime import datetime

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=26222de21113b0fff9a0f7c977296b4a').read()
        json_data = json.loads(res)
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' +
                          str(json_data['coord']['lat']),
            "sunrise" : datetime.fromtimestamp(int(json_data['sys']['sunrise'])).strftime('%B %d, %Y %I:%M %p'),
            "sunset" : datetime.fromtimestamp(int(json_data['sys']['sunset'])).strftime('%B %d, %Y %I:%M %p'),
            "temp": str("{:.2f}".format(float(json_data['main']['temp']) - 273.15)) + '\u00B0C',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
            "icon": "https://openweathermap.org/img/wn/"+str(json_data['weather'][0]['icon'])+"@4x.png"
        }

    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city': city, 'data': data})
