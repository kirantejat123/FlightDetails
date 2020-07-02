from django.db.models import QuerySet
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from app36.models import vistara
from .models import vistara, makemytrip,yatra


class flightDetails(View):
    def post(self, request):
        date = request.POST.get("date")
        print(date)
        print(type(date))
        airlines = request.POST.get("airline")

        if airlines=="vistara" :
            from requests import get
            from selenium import webdriver
            import urllib3
            from bs4 import BeautifulSoup
            driver = webdriver.Chrome(executable_path=r'C:\Users\kiran\Desktop\chromedriver.exe')
            url = "https://www.airvistara.com/trip/flight-status?departureStation=DEL&arrivalStation=BOM&flightDate=4/12/2018"
            driver.get(url)
            # print(response.text)
            html_soup = BeautifulSoup(driver.page_source, "html.parser")
            # print(html_soup)

            # html_page=html_soup.prettify()
            # container=html_soup.find_all("div",class_="content-container margcontainerpress mmargbtm20 clearfix")
            # # print(container)
            # containers1=html_soup.findAll("div",class_="col-md-12 table-responsive tablewithflight")
            # # print(containers)
            soupdata = html_soup.findAll("div", class_="panel panel-default")
            # print(container2)
            # data=container2[0].text
            totaldata1=[]
            for data in soupdata:
                f_data1 = data.findAll("span")
                f_number = f_data1[0].text
                f_origin = f_data1[1].text
                f_destination = f_data1[2].text
                f_departuretime = f_data1[3].text
                res = vistara(f_no=f_number, f_origin=f_origin, f_destPlace=f_destination, f_destTime=f_departuretime)
                res.save()
            totaldata1= vistara.objects.all()
            return render(request, "home.html", {"vistara": totaldata1})

        elif airlines=="MakeMyTrip":
            from selenium import webdriver
            import urllib3
            from bs4 import BeautifulSoup
            driver = webdriver.Chrome(executable_path=r'C:\Users\kiran\Desktop\chromedriver.exe')
            url = "https://flights.makemytrip.com/makemytrip/search/O/O/E/1/0/0/S/V0/DEL_BOM_04-12-2018?contains=false&remove="
            driver.get(url)
            # print(response.text)
            soup = BeautifulSoup(driver.page_source, "html.parser")
            soup_data = soup.findAll('div',class_='clearfix listing_row append_bottom8 sponsored_list_wrapper shadow_genrator_1 c-listing_row c-listing_row--versionI ng-scope')
            totaldata=[]
            for i in soup_data:
                span_data = i.findAll("span")
                f_name = span_data[5].text
                f_number = span_data[4].text
                f_departuretime = span_data[8].text
                f_destination = span_data[9].text
                f_arrivaltime = span_data[11].text
                f_arrivalplace = span_data[12].text
                res = makemytrip(f_name=f_name, f_number=f_number, f_departuretime=f_departuretime,
                                 f_departureplace=f_destination, f_arrivaltime=f_arrivaltime,
                                 f_arrivalplace=f_arrivalplace)
                res.save()
            totaldata = makemytrip.objects.all()
            return render(request, "home.html", {"makemytrip": totaldata})
        elif airlines == "yatra":
            from selenium import webdriver
            import urllib3
            from bs4 import BeautifulSoup
            driver = webdriver.Chrome(executable_path=r'C:\Users\kiran\Desktop\chromedriver.exe')
            url = "https://flight.yatra.com/air-search-ui/dom2/trigger?type=O&viewName=normal&flexi=0&noOfSegments=1&origin=DEL&originCountry=IN&destination=BOM&destinationCountry=IN&flight_depart_date=04/12/2018&ADT=1&CHD=0&INF=0&class=Economy&source=fresco-flights&version=1.38"
            driver.get(url)
            # print(response.text)
            soup = BeautifulSoup(driver.page_source, "html.parser")
            soupdata=soup.findAll('div',class_="js-flightRow js-flightItem")
            for i in soupdata:
                f_data=i.findAll("small")
                f_name=f_data[0].text
                f_number=f_data[1].text
                span_data=i.findAll("span")
                f_departuretime = span_data[4].text
                f_arrivaltime = span_data[5].text
                res=yatra(f_name=f_name,f_number=f_number,f_departuretime=f_departuretime,f_arrivaltime=f_arrivaltime)
                res.save()
            totaldata=yatra.objects.all()
            return render(request, "home.html", {"yatra": totaldata})
