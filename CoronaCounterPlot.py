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
pageCount = 1
date_time = now.strftime("%Y-%m-%d %H:%M:%S")

a = 0

yenileme_sayisi = int(input("Number of the refreshing in URL: "))

while pageCount <= yenileme_sayisi:
    browser.get(url)  # We can go to the URL with this code.
    elements = browser.find_element_by_xpath("//*[@id='maincounter-wrap']/div/span")
    d_number.append(elements.text)    
    time_srtftime.append(a)
    

    time.sleep(4)  # We can wait in this URL for 4 seconds.
    print("Number of the refresh: {}".format(pageCount))
    pageCount += 1
    a += 4


print(d_number)
print(time_srtftime)
browser.close()  # Closing the browser.

plt.plot(time_srtftime, d_number,color='blue', linestyle='dashed', marker='o', markerfacecolor='black', markersize=5)
plt.title("Number of the Coronavirus Cases(COVID-19)\nStart time:{}".format(date_time))
plt.xlabel("Time Pass After Starting Time(Seconds)")
plt.ylabel("Number of Cases")
plt.show()