from selenium import webdriver
import time
import datetime
import pandas as pd
from matplotlib import pyplot as plt
now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))


# With this code, we can see numbers of the people who has coronavirus(COVID-19).

browser = webdriver.Firefox()  # Firefox üzerinden gerçekleştirilecekse bu satır kullanılır

url = "https://www.worldometers.info/coronavirus/"

d_number = []
time_srtftime = []
pageCount = 1

yenileme_sayisi = int(input("Belirli URL adresinin kaç defa yenileneceğini belirtiniz: "))

while pageCount <= yenileme_sayisi:
    browser.get(url)  # We can go to the URL with this code.
    elements =  browser.find_element_by_xpath("//*[@id='maincounter-wrap']/div/span")
    d_number.append(elements.text)
    time_srtftime.append(now.strftime("%Y-%m-%d %H:%M:%S"))
    

    time.sleep(4)  # We can wait in this URL for 4 seconds.
    print(pageCount, ". yenileme gerçekleşti.")
    pageCount += 1


print(d_number)
print(time_srtftime)
browser.close()  # Closing the browser.

plt.plot(d_number, time_srtftime,color='blue', linestyle='dashed', marker='o', markerfacecolor='black', markersize=5)
plt.title("Number of the Coronavirus Cases(COVID-19)\n")
plt.xlabel("Time")
plt.ylabel("Number of Cases")
plt.show()
