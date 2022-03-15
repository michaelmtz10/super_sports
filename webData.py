from calendar import c
from cgitb import text
from urllib import response
from bs4 import BeautifulSoup
import requests
import re

url = 'https://cars.usnews.com/cars-trucks/browse?body_style=Sports%20Cars&year_min=2021&year_max=2021&sort=alpha&page=1'
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

print(response.status_code)
