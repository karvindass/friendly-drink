
from urllib2 import urlopen
from contextlib import closing
import json

def lctnwthrgt ():
    url= 'http://ip-api.com/json'
    response= urlopen(url)
    location = json.loads(response.read())

    url2= 'http://api.openweathermap.org/data/2.5/weather?lat=%7.4f&lon=%7.4f&APPID=c3dae359f90443db69dd233e25b9875d' %(location['lat'], location['lon'])
    sunny= urlopen(url2)
    wthrdata= json.loads(sunny.read())

    temp= wthrdata['main']
    sky= wthrdata['weather'][0]
    wnd= wthrdata['wind']

    temperature=1.8*(temp['temp']-273)+32

    return (temperature, wnd['speed'], sky['id'], str(location['city']) )


#weatherid:
#20X	thunder storm stuff
#30X	drizzle
#50X	rain
#60X    snow
#70X    Atmosphere conditions
