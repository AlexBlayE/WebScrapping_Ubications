import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time
import re

# variables
web_path = r"https://www.google.com/maps/"
csv_path = r".\CSV\populations.csv"
municipis = pd.read_csv(csv_path)["Municipi"]
comarques = pd.read_csv(csv_path)["Comarca"]
long = []  # longitude
lat = []  # latitude

# functions
def search_ubication(url):
    first_sentence = re.search(r"!3d(.*?)!16", url)  # this is to search a regular expression in the google maps url

    if first_sentence != None:
        return first_sentence.group(1).split("!4d")

    else:
        return ["NaN", "NaN"]


# driver and driver options and services
options = Options()
options.add_argument("--headless")

service = Service(log_path=r".\Logs\geckodriver.log")

driver = webdriver.Firefox(options=options, service=service)

# accept cockies
driver.get(web_path)
boto_cockies = driver.find_element(By.CLASS_NAME, "lssxud")
boto_cockies.click()
time.sleep(1.5)

try:
    
    count = 1
    # iterate cities
    for municipi, comarca in zip(municipis, comarques):
        # search input
        buscador = driver.find_element(By.ID, "searchboxinput")
        buscador.clear()

        # put in searchinput the keys
        buscador.send_keys(municipi + ", " + comarca)

        # click search
        click_buscar = driver.find_element(By.ID, "searchbox-searchbutton")
        click_buscar.click()
        time.sleep(3.5) 

        # take url
        url = driver.current_url

        # take ubication from url
        ubication = search_ubication(url)

        print(municipi)
        print(ubication)
        print(str(count) + "/" + str(municipis.shape[0]))
        print()
        count = count + 1

        long.append(ubication[0])
        lat.append(ubication[1])

    # add ubications to dataframe
    ubication_df = pd.DataFrame({"Longitud": long, "Latitud": lat})
except:

    ubication_df = pd.DataFrame({"Longitud": long, "Latitud": lat})
    pass

# create a csv with ubications
ubication_df.to_csv(r".\CSV\ubications.csv", sep=",", index=False)

driver.quit()
