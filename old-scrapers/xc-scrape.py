import requests
import csv
from bs4 import BeautifulSoup

from fixes import year_fixes, state_fixes

URL = 'https://aueagles.com/sports/cross-country/roster'

payload = {'view': 2}
r = requests.get(URL, params=payload)

CSV_HEADERS = [
    'Name',
    'Academic Year',
    'Hometown',
    'State/Country',
    'High School',
    'Previous School',
    'Link'
]

wtable = BeautifulSoup(r.text, 'html.parser').find_all('table')[2]
mtable = BeautifulSoup(r.text, 'html.parser').find_all('table')[3]

MEN_CSV_FILE = '../CSVs/aueagles-mxc-roster.csv'
WOMEN_CSV_FILE = '../CSVs/aueagles-wxc-roster.csv'

t_to_c = {
    wtable: WOMEN_CSV_FILE,
    mtable: MEN_CSV_FILE
}

for table in [wtable, mtable]:
    CSV_FILE = t_to_c.get(table)
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=CSV_HEADERS)

        writer.writeheader()

        for row in table.find_all('tr')[1:]:
            cells = row.find_all('td')

            link = cells[0].find('a').get('href')

            url = ''

            if link:
                url = f'https://aueagles.com{link}'

            name = cells[0].text.strip()

            yr_list = [cells[1].string.strip()]

            for yr in yr_list:
                yr = year_fixes.get(yr, yr)

            try:
                hometown = cells[2].text.split(' / ')[0].split(', ')[0]
                region = [cells[2].text.split(' / ')[0].split(', ')[1]]
                for s in region:
                    state = state_fixes.get(s, s)
                hs = cells[2].text.split(' / ')[1]

            except IndexError:
                hometown = None
                state = None
                hs = None

            prev = cells[3].text.strip()

            writer.writerow({
                'Name': name,
                'Academic Year': yr,
                'Hometown': hometown,
                'State/Country': state,
                'High School': hs,
                'Previous School': prev,
                'Link': url
            })

        print(f'Wrote {CSV_FILE}')

