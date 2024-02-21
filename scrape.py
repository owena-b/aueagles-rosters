import requests
import csv
from bs4 import BeautifulSoup
from tkinter import *

from fixes import position_fixes, year_fixes, sport_fixes

URL = 'https://aueagles.com/sports/mens-basketball/roster'

payload = {'view': 2}
r = requests.get(URL, params=payload)

CSV_FILE = 'aueagles-mbb-roster.csv'

CSV_HEADERS = [
    'Jersey Number',
    'Name',
    'Position',
    'Height',
    'Academic Year',
    'Hometown',
    'State/Country',
    'High School',
    'Link'
]

table = BeautifulSoup(r.text, 'html.parser').find_all('table')[2]

with open(CSV_FILE, 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=CSV_HEADERS)

    writer.writeheader()

    for row in table.find_all('tr')[1:]:
        cells = row.find_all('td')

        jersey_no = cells[0].text.strip()

        link = cells[1].find('a').get('href')

        url = ''

        if link:
            url = f'https://aueagles.com{link}'

        name = cells[1].text.strip()

        pos_list = [cells[2].string.strip()]

        for pos in pos_list:
            pos = position_fixes.get(pos, pos)

        ft = cells[3].text.split('-')[0]
        inches = cells[3].text.split('-')[1]

        height = f'{ft} ft {inches} in'
        height = height.strip()

        yr_list = [cells[4].string.strip()]

        for yr in yr_list:
            yr = year_fixes.get(yr, yr)

        try:
            hometown = cells[5].text.split(' / ')[0].split(', ')[0]
            state = cells[5].text.split(' / ')[0].split(', ')[1]
            hs = cells[5].text.split(' / ')[1]

        except IndexError:
            hometown = None
            hs = None

        writer.writerow({
            'Jersey Number': jersey_no,
            'Name': name,
            'Position': pos,
            'Height': height,
            'Academic Year': yr,
            'Hometown': hometown,
            'State/Country': state,
            'High School': hs,
            'Link': url
        })

    print(f'Wrote {CSV_FILE}')
