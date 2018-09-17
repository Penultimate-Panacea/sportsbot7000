# coding=utf-8
"""Handles the Beautiful Soup Scraping from websites"""
from urllib.request import urlopen
from bs4 import BeautifulSoup

soup = BeautifulSoup(urlopen('http://www.juniatasports.net/sports/fh/2018-19/schedule').read(), 'html.parser')
teamstats = soup.find_all('div', class__='team-stats accent-bg')
print(teamstats)
