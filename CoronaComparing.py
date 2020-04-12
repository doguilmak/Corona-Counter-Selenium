from selenium import webdriver
import time
import datetime
import pandas as pd
from matplotlib import pyplot as plt

now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# With this code, we can see numbers of the people who has coronavirus(COVID-19).

browser = webdriver.Firefox() # We are going to use Firefox browser for the code.

url = "https://www.worldometers.info/coronavirus/" # We are going to use this website for the getting datas.

d_number = []
time_srtftime = []

USA = []
China = []
Italy = []

pageCount = 1
date_time = now.strftime("%Y-%m-%d %H:%M:%S")

a = 0

yenileme_sayisi = int(input("Number of the refreshing in URL: "))
time_for_refresh = int(input("Time between refresh(as a second): "))

while pageCount <= yenileme_sayisi:
    browser.get(url)  # We can go to the URL with this code.
    #Total Number
    elements = browser.find_element_by_xpath("//*[@id='maincounter-wrap']/div/span")
    d_number.append(elements.text)  
    
    #Cases in USA
    numberofUSA = browser.find_element_by_xpath("//*[@id='main_table_countries_today']/tbody[1]/tr[2]/td[2]")
    USA.append(numberofUSA.text)
    
    #Cases in China
    numberofChina = browser.find_element_by_xpath("//*[@id='main_table_countries_today']/tbody[1]/tr[5]/td[2]")
    China.append(numberofChina.text)
    
    #Cases in Italy
    numberofItaly = browser.find_element_by_xpath("//*[@id='main_table_countries_today']/tbody[1]/tr[3]/td[2]")
    Italy.append(numberofItaly.text)
    
    time_srtftime.append(a)
    

    time.sleep(time_for_refresh)  # We can wait in this URL for 4 seconds.
    print("Number of the refresh: {}".format(pageCount))
    pageCount += 1
    a += time_for_refresh


browser.close()  # Closing the browser.

plt.subplot(2, 1, 1)
plt.plot(time_srtftime, d_number,color='blue', linestyle='dashed', marker='o', markerfacecolor='black', markersize=5)
plt.title("Number of the Coronavirus Cases(COVID-19)\nStart time:{}".format(date_time))
plt.xlabel("Time Pass After Starting Time(Seconds)")
plt.ylabel("Number of Cases(Total)")

plt.subplot(2, 1, 2)
plt.plot(time_srtftime, USA,color='blue', linestyle='dashed', marker='o', markerfacecolor='black', markersize=5)
plt.plot(time_srtftime, China,color='red', linestyle='dashed', marker='o', markerfacecolor='black', markersize=5)
plt.plot(time_srtftime, Italy,color='green', linestyle='dashed', marker='o', markerfacecolor='black', markersize=5)
plt.xlabel("Time Pass After Starting Time(Seconds)")
plt.ylabel("Number of Cases")
plt.legend(["USA", "China", "Italy"])

plt.show()