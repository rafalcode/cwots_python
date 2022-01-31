#!/usr/bin/python3
# Q. What is this script about?
# A. xhgsz: eXtract Human Genome SiZes: scraping a table from wikipedia and saving it as a neat CSV file
# Q. Are there any hardcoded values in it?
# A. Yes, I'm afraid there is .. .each wikiepdia page is different, and can have several tables in various place. You need to "know" the wikipedia page for this script.
# Q. Pandas' read_html() function is expressly made for this, why do you have to use the Wikipedia API as well?
# A. Well read_html() only sometimes works .... the tables in wikipedia are not uniform. So, it is only used on a subset of the page, the subset obtained via the API.
import pandas as pd
import csv
import requests

print("Note: This script is hard-coded to extract the first table in the Wikipedia Page \"Human genome\"")
print("      It would need to be edited (especially the correct table would need to be identified) for other pages.")

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"
TITLE="Human genome" # THis works probably lucky ... only one page found for this title.
PARAMS = {
    'action': "parse",
    'page': "Human genome",
    'section': 3,
    'format': "json"
}
res = S.get(url=URL, params=PARAMS)
data = res.json()
# print(data)

# df = pd.read_html(url)[9]
df = pd.read_html(data["parse"]["text"]["*"])[0]
df.to_csv('a0.csv',index=False)
# print(len(df))
