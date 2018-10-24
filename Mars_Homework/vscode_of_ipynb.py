from selenium import webdriver
import selenium
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

driver = webdriver.Chrome("C:/Users/Antediluvien/chromedriver/chromedriver.exe")  # Optional argument, if not specified will search path.
html_nasa=driver.get('https://mars.nasa.gov/news/');
html_nasa = driver.page_source
#url = 'https://mars.nasa.gov/news/'
soup_nasa = BeautifulSoup(html_nasa,'html.parser')

data_ul = soup_nasa.find_all("ul")

soup_nasa.find_all('a', href=True)

mydivs = soup_nasa.find_all("div", {"class": "content_title"})
news_title=mydivs[0].get_text()
news_title

list_text = soup_nasa.find_all("div", {"class": "list_text"})
news_paragraph =list_text[0].get_text()
news_paragraph

# Visit URL
driver = webdriver.Chrome("C:/Users/Antediluvien/chromedriver/chromedriver.exe")
html_jpl = driver.get('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars');
html_jpl = driver.page_source

soup_jpl = BeautifulSoup(html_jpl,'html.parser')
print(soup_jpl.prettify())

full_button_info=soup_jpl.find_all("a", {"id": "full_image"})
full_button_info

st = str(full_button_info)
import re
img_string = re.findall(r'data-link="(.*?)" data-title',st)
print(img_string)

string_form_of_link = ''.join(img_string)
full_link_for_image = ('https://www.jpl.nasa.gov' + string_form_of_link)
print(full_link_for_image)

html_of_latest_jpl_image = driver.get(full_link_for_image);
html_of_latest_jpl_image

soup_jpl_image = BeautifulSoup(full_link_for_image,'html.parser')
print(soup_jpl.prettify())

full_image_jpg_info=soup_jpl_image.find_all("a", {"id": "full_image"})
full_button_info

string_form_of_jpg = str(full_button_info)
import re
img_string_jpg = re.findall(r'data-fancybox-href="(.*?)" data-link',st)
print(img_string_jpg)

string_form_of_link_jpg = ''.join(img_string_jpg)
full_link_for_image_jpg = ('https://www.jpl.nasa.gov' + string_form_of_link_jpg)
full_link_for_image_jpg

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import tweepy as tp
import json as js

driver = webdriver.Chrome("C:/Users/Antediluvien/chromedriver/chromedriver.exe")  # Optional argument, if not specified will search path.
html_twitter=driver.get('https://twitter.com/marswxreport?lang=en');
html_twitter

consumer_key = 'tXyEgKL9boLPhR9suq9HHifyU'
consumer_secret = 'N9gMTaUFBjtrIKQOfEXNayGZlgl74sDdQJ6oBkacCgjm3Bt7vh'
access_token = '1010569721408716800-57jAfcMLM4Di3vaY9IHZEXCd1kauA4'
access_secret = 'PQPja7stMuoz4c0Umeeg1fL2SzPnIBcT6AQEzy6Ocj3F8'


auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth, parser=tp.parsers.JSONParser())

target_user_MarsWeather = ("@MarsWxReport")


# Loop through user
for user in target_user_MarsWeather:

    # Variables for holding Tweets
    MarsWeather_Tweets = []
    MarsWeather_TimeStamp = []

# Loop through twitter pages
    for x in range(0, 1):

        # Get all tweets from user feed
        public_tweets_Mars = api.user_timeline(target_user_MarsWeather, page=x)

        # Loop through all tweets
        for tweet in public_tweets_Mars:
            
            #Get Tweet Text and TimeStamp Data
            MarsWeather_Tweets.append(tweet['text'])
            MarsWeather_TimeStamp.append(tweet['created_at'])

latest_mars_weather=MarsWeather_Tweets[0]
latest_mars_weather

MarsWeather_TimeStamp[0]

driver = webdriver.Chrome("C:/Users/Antediluvien/chromedriver/chromedriver.exe")  # Optional argument, if not specified will search path.
mars_facts = driver.get('https://space-facts.com/mars/');
mars_facts = driver.page_source
mars_facts

soup_mars_facts = BeautifulSoup(mars_facts,'html.parser')
print(soup_mars_facts.prettify())

mars_table_info=soup_mars_facts.find_all("table", {"id": "tablepress-mars"})
mars_table_info

#FACTS FOR TABLE
step_1=pd.read_html(str(mars_table_info))
mars_facts_df = step_1[0]
mars_facts_df

#MARS HEMISPHERES
driver = webdriver.Chrome("C:/Users/Antediluvien/chromedriver/chromedriver.exe")  # Optional argument, if not specified will search path.
mars_hemisphere = driver.get('https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars');
mars_hemisphere = driver.page_source
mars_hemisphere
soup_mars_hemisphere = BeautifulSoup(mars_hemisphere,'html.parser')
print(soup_mars_hemisphere.prettify())

mars_buttons=soup_mars_hemisphere.find_all("a", {"class": "itemLink product-item"})
mars_buttons

mars_buttons[0]

mars_link_1=[]
mars_link_2=[]
mars_link_3=[]
mars_link_4=[]
for x in mars_buttons:
    if x == mars_buttons[0]:
        mars_link_1.append(mars_buttons[0]) # as there are 2 of each link due to the thumbnail and text both being clickable
    elif x == mars_buttons[2]:
        mars_link_2.append(mars_buttons[2])
    elif x == mars_buttons[4]:
        mars_link_3.append(mars_buttons[4])
    elif x == mars_buttons[6]:
        mars_link_4.append(mars_buttons[6])


mars_link_1_string = str(mars_link_1)
mars_link_1_string_html = re.findall(r'href="(.*?)"><img ',mars_link_1_string)
cerebus_link = mars_link_1_string_html
cerebus_link

cerebus_link_string = ''.join(cerebus_link)
full_link_for_cerebus = ('https://astrogeology.usgs.gov' + cerebus_link_string)
full_link_for_cerebus

mars_link_2_string = str(mars_link_2)
mars_link_2_string_html = re.findall(r'href="(.*?)"><img ',mars_link_2_string)
schiaparelli_link = mars_link_2_string_html
schiaparelli_link

schiaparelli_link_string = ''.join(schiaparelli_link)
full_link_for_schiaparelli = ('https://astrogeology.usgs.gov' + schiaparelli_link_string)
full_link_for_schiaparelli

mars_link_3_string = str(mars_link_3)
mars_link_3_string_html = re.findall(r'href="(.*?)"><img ',mars_link_3_string)
syrtis_major_link = mars_link_3_string_html
syrtis_major_link

syrtis_major_link_string = ''.join(syrtis_major_link)
full_link_for_syrtis_major = ('https://astrogeology.usgs.gov' + syrtis_major_link_string)
full_link_for_syrtis_major

mars_link_4_string = str(mars_link_4)
mars_link_4_string_html = re.findall(r'href="(.*?)"><img ',mars_link_4_string)
valles_marineris_link = mars_link_4_string_html
valles_marineris_link

valles_marineris_link_string = ''.join(valles_marineris_link)
full_link_for_valles_marineris = ('https://astrogeology.usgs.gov' + valles_marineris_link_string)
full_link_for_valles_marineris

driver = webdriver.Chrome("C:/Users/Antediluvien/chromedriver/chromedriver.exe")  # Optional argument, if not specified will search path.
cerebus_html = driver.get(full_link_for_cerebus);
cerebus_html = driver.page_source
soup_cerebus_html = BeautifulSoup(cerebus_html,'html.parser')
print(soup_cerebus_html.prettify())

cerebus_img_link_finder=soup_cerebus_html.find_all("div", {"class": "downloads"})
cerebus_img_link_finder

cerebus_img_link_finder_string = str(cerebus_img_link_finder)
cerebus_img_link_finder_string = re.findall(r'href="(.*?)"',cerebus_img_link_finder_string)
cerebus_img = cerebus_img_link_finder_string
cerebus_img=cerebus_img[0]
cerebus_img

driver = webdriver.Chrome("C:/Users/Antediluvien/chromedriver/chromedriver.exe") 
schiaparelli_html = driver.get(full_link_for_schiaparelli);
schiaparelli_html = driver.page_source
soup_schiaparelli_html = BeautifulSoup(schiaparelli_html,'html.parser')
print(soup_schiaparelli_html.prettify())

schiaparelli_img_link_finder=soup_schiaparelli_html.find_all("div", {"class": "downloads"})
schiaparelli_img_link_finder

schiaparelli_img_link_finder_string = str(schiaparelli_img_link_finder)
schiaparelli_img_link_finder_string = re.findall(r'href="(.*?)"',schiaparelli_img_link_finder_string)
schiaparelli_img = schiaparelli_img_link_finder_string
schiaparelli_img = schiaparelli_img[0]
schiaparelli_img

driver = webdriver.Chrome("C:/Users/Antediluvien/chromedriver/chromedriver.exe") 
syrtis_major_html = driver.get(full_link_for_syrtis_major);
syrtis_major_html = driver.page_source
soup_syrtis_major_html = BeautifulSoup(syrtis_major_html,'html.parser')
print(soup_syrtis_major_html.prettify())

syrtis_major_img_link_finder=soup_syrtis_major_html.find_all("div", {"class": "downloads"})
syrtis_major_img_link_finder

syrtis_major_img_link_finder_string = str(syrtis_major_img_link_finder)
syrtis_major_img_link_finder_string = re.findall(r'href="(.*?)"',syrtis_major_img_link_finder_string)
syrtis_major_img = syrtis_major_img_link_finder_string
syrtis_major_img = syrtis_major_img[0]
syrtis_major_img

driver = webdriver.Chrome("C:/Users/Antediluvien/chromedriver/chromedriver.exe") 
valles_marineris_html = driver.get(full_link_for_valles_marineris);
valles_marineris_html = driver.page_source
soup_valles_marineris_html = BeautifulSoup(valles_marineris_html,'html.parser')
print(soup_valles_marineris_html.prettify())

valles_marineris_img_link_finder=soup_valles_marineris_html.find_all("div", {"class": "downloads"})
valles_marineris_img_link_finder

valles_marineris_img_link_finder_string = str(valles_marineris_img_link_finder)
valles_marineris_img_link_finder_string = re.findall(r'href="(.*?)"',valles_marineris_img_link_finder_string)
valles_marineris_img = valles_marineris_img_link_finder_string
valles_marineris_img = valles_marineris_img[0]
valles_marineris_img

hemisphere_image_urls = [
    {"Cerebus": "Cerebus Hemisphere", "img_url":cerebus_img},
    {"Schiaparelli": "Schiaparelli Hemisphere", "img_url": schiaparelli_img},
    {"Syrtis Major": "Syrtis Major Hemisphere", "img_url": syrtis_major_img},
    {"Valles Marineris": "Valles Hemisphere", "img_url": valles_marineris_img},
]
hemisphere_image_urls