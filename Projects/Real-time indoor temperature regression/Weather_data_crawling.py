from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
import bs4
import requests
import calendar
import os
import json
import copy

# Function to crawl data from link: https://www.timeanddate.com/weather/costa-rica/san-jose/historic?month={m}&year={year}
def crawl_weather_data(year, list_month):
  year = copy.deepcopy(year)
  list_month = copy.deepcopy(list_month)
  for m in list_month:
    for i in range(calendar.monthrange(2019, m)[1]):
        day = "0"*(2-len(str(i+1))) + str(i+1)
        month = "0"*(2-len(str(m))) + str(m)
        filename = year+month+day + ".json"
        print(filename,i)
        url = f"https://www.timeanddate.com/weather/costa-rica/san-jose/historic?month={m}&year={year}"
        driver = webdriver.Chrome()
        driver.get(url)
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div[5]/main/article/div[6]/div[3]/a[{i+1}]')))
        driver.execute_script("arguments[0].click();", element)
        sleep(5)
        html = driver.page_source
        driver.close()
        soup = bs4.BeautifulSoup(html)
        
        final_data = []
        date = []
        time=[]
        temp = []
        weather = []
        wind_speed = []
        humidity = []
        barometer = []
        visibility = []
        data = soup.find('table', {'id':'wt-his'}).find('tbody').findAll('tr')
        for j in data:
          date.append(filename[:-5])
          time.append(j.find("th").get_text())
          temp.append(j.findAll("td")[1].get_text())
          weather.append(j.findAll("td")[2].get_text())
          wind_speed.append(j.findAll("td")[3].get_text())
          humidity.append(j.findAll("td")[5].get_text())
          barometer.append(j.findAll("td")[6].get_text())
          visibility.append(j.findAll("td")[7].get_text())
        with open(filename, 'w') as file:
          json.dump([{'date':date,'time':time, 'temp': temp, 'weather': weather,\
                     'wind_speed': wind_speed,'humidity':humidity, 'barometer':barometer, 'visibility':visibility}\
                     for date,time, temp,weather,wind_speed,humidity,barometer,visibility\
                     in zip(date,time,temp, weather,  wind_speed,  humidity,barometer,visibility)], file)
        print(f"successfully created {filename}")

crawl_weather_data(2023, [9, 10, 11])