import requests
from fpdf import FPDF
import datetime as dt

CITY = "Gothenburg"
LATITUDE = "57.7088"
LONGITUDE = "11.9745"
def getWeatherData(LATITUDE,LONGITUDE,hourInterval,dataPoints):




    BASE_URL = "https://api.met.no/weatherapi/locationforecast/2.0/compact?"
    headers = {'User-Agent': "MyTest 1.0"}
    URL = BASE_URL + "&lat=" + LATITUDE + "&lon=" + LONGITUDE

    response=requests.get(URL, headers=headers).json() #API call to get weatherdata

    airTemp = []
    windSpeed = []
    precipAmount = []
    symbolCode = []
    utcTime = []
    for i in range(dataPoints):
        airTemp += [response['properties']['timeseries'][hourInterval * i]['data']['instant']['details']['air_temperature']]
        windSpeed += [response['properties']['timeseries'][hourInterval * i]['data']['instant']['details']['wind_speed']]
        precipAmount += [response['properties']['timeseries'][hourInterval * i]['data']['next_1_hours']['details']['precipitation_amount']]
        symbolCode += [response['properties']['timeseries'][hourInterval * i]['data']['next_1_hours']['summary']['symbol_code']]
        utcTime += [response['properties']['timeseries'][hourInterval * i]['time']]

    return airTemp, windSpeed, precipAmount, symbolCode, utcTime;

airTemp, windSpeed,precipAmount,symbolCode,utcTime = getWeatherData(LATITUDE, LONGITUDE, 1, 10)

pageWidth = 120

pdf = FPDF(orientation = "portrait", format = (pageWidth , 300))
pdf.add_page()
pdf.set_font("Times",'',22)
pdf.cell(pageWidth, 10, "Weather Forecast "+CITY,border=1,align='C',center=True)
pdf.output("test.pdf")
