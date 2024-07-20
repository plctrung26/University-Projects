import pandas as pd
import bs4
import requests
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import selenium
import time
import copy

def get_product_links(url):
  url = copy.deepcopy(url)
  driver = webdriver.Chrome()
  driver.get(url)
  time.sleep(3)
  click_more = True
  while click_more:
      time.sleep(1)
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
      time.sleep(10)
      elements = driver.find_elements(By.XPATH, '//*[@id="main"]/div[1]/div/div[2]/div[2]/div[3]/div/div[2]/div/div/button')
      if len(elements) == 0:
          click_more = False
      else:
          print(len(elements))
          element = elements[0]
          driver.execute_script("arguments[0].click();", element)    
  html = driver.page_source
  soup = bs4.BeautifulSoup(html)
  driver.close()

  items = soup.findAll('a',{'target':'_blank'})
  list_link = []
  for item in items:
      list_link.append(item['href'])
  return list_link

def crawl_product_data(list_link):
  list_link = copy.deepcopy(list_link)
  for link_temp in list_link:
    filename = "item_" + str(count_item) +".csv"
    driver = webdriver.Chrome()
    driver.get(link_temp)
    time.sleep(30)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(30)
    button = driver.find_element(By.XPATH, '//*[@id="id-tong-quan"]/div[2]/button')
    driver.execute_script("arguments[0].click();", button)
    html = driver.page_source
    soup = bs4.BeautifulSoup(html)
    driver.close()
    
    columns= ["web", "shop_name", "watch_name", "price"]
    values = ["sendo"]

    values.append(soup.find("a",{"aria-label":"shop-name"}).get_text())
    values.append(soup.find("h1",{"class":"d7ed-ytwGPk d7ed-zrT4k2 d7ed-kUYEit d7ed-AHa8cD d7ed-mzOLVa"}).get_text())
    values.append(soup.find("span",{"class":"d7ed-ij7pjf d7ed-AHa8cD d7ed-giDKVr"}).get_text())
    
    if soup.find("table",{"class": "_96e1-t3iHfo d7ed-s1zNv_"})==None:
        exception.append(link_temp)
        count_item+=1
        continue
    table_values = soup.find("table",{"class": "_96e1-t3iHfo d7ed-s1zNv_"}).findAll('tr')
    for val in table_values:
        columns.append(val.findAll("td")[0].get_text())
        values.append(val.findAll("td")[1].get_text())

    df = pd.DataFrame({"column_name":columns, "value": values})
    df.to_csv("D:/DS105/watch_data/"+filename, index = False)
    count_item+=1

list_link = get_product_links("https://www.sendo.vn/tim-kiem?q=%C4%91%E1%BB%93ng%20h%E1%BB%93%20casio")
crawl_product_data(list_link)