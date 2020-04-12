from selenium import webdriver
import time

# With this code, we can see numbers of the people who has coronavirus(COVID-19).

browser = webdriver.Firefox()  # Firefox üzerinden gerçekleştirilecekse bu satır kullanılır

url = "https://www.worldometers.info/coronavirus/"

d_number = []
pageCount = 1

yenileme_sayisi = int(input("Belirli URL adresinin kaç defa yenileneceğini belirtiniz: "))

while pageCount <= yenileme_sayisi:
    browser.get(url)  # Sayfaya gidilir.
    elements =  browser.find_element_by_xpath("//*[@id='maincounter-wrap']/div/span")
    d_number.append(elements.text)
    

    time.sleep(4)  # Gidilen sayfada 2 saniye beklenir.
    print(pageCount, ". yenileme gerçekleşti.")
    pageCount += 1


print(d_number)
browser.close()  # Sayfa kapatılır.

with open("datas.txt","w",encoding = "UTF-8") as file:
    for d_numbers in d_number:
        file.write(d_numbers + "\n")