from flask import Flask, jsonify

import sqlite3

import pandas as pd

import numpy as np

import datetime as dt

import selenium

from bs4 import BeautifulSoup

app = Flask(__name__)
import vscode_of_ipynb
from vscode_of_ipynb import *
list_of_imports = [news_title,news_paragraph,full_link_for_image]
latest_mars_weather
MarsWeather_TimeStamp
mars_facts_df
full_link_list = [full_link_for_cerebus,full_link_for_schiaparelli,full_link_for_syrtis_major, full_link_for_valles_marineris]

@app.route("/")
def home():
    for x in list_of_imports:
        return x

@app.route("/pictures")
def page_1():
    for x in full_link_list:
        return x
def df():
    return mars_facts_df


if __name__ == "__main__":
    app.run()
