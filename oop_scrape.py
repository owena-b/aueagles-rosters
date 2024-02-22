import requests
import csv
from bs4 import BeautifulSoup
from fixes import position_fixes, state_fixes, year_fixes

sports_dict = {
    'wbb': 'womens-basketball',
    'mbb': 'mens-basketball',
    'wsoc': 'womens-soccer',
    'msoc': 'mens-soccer',
    'mtf': 'track-and-field',
    'wtf': 'track-and-field',
    'wxc': 'cross-country',
    'mxc': 'cross-country',
    'wswim': 'swimming-and-diving',
    'mswim': 'swimming-and-diving',
    'fh': 'field-hockey',
    'lax': 'womens-lacrosse',
    'wrestling': 'wrestling',
    'vb': 'womens-volleyball',
    'test': 'mens-basketball'
}

sports_headers = {
    'wbb': ['Jersey_number', 'Name', 'Position', 'Height', 'Academic_year', 'Hometown', 'State_or_country',
            'High_school', 'Link'],
    'mbb': ['Jersey_number', 'Name', 'Position', 'Height', 'Academic_year', 'Hometown', 'State_or_country',
            'High_school', 'Link'],
    'wsoc': ['Jersey_number', 'Name', 'Position', 'Height', 'Academic_year', 'Hometown', 'State_or_country',
             'High_school', 'Previous_school', 'Link'],
    'msoc': ['Jersey_number', 'Name', 'Position', 'Height', 'Academic_year', 'Hometown', 'State_or_country',
             'High_school', 'Link'],
    'wtf': ['Name', 'Events', 'Academic_year', 'Hometown', 'State_or_country', 'High_school', 'Previous school',
            'Link'],
    'mtf': ['Name', 'Events', 'Academic_year', 'Hometown', 'State_or_country', 'High_school', 'Previous school',
            'Link'],
    'mxc': ['Name', 'Academic_year', 'Hometown', 'State_or_country', 'High_school', 'Previous school', 'Link'],
    'wxc': ['Name', 'Academic_year', 'Hometown', 'State_or_country', 'High_school', 'Previous school', 'Link'],
    'wswim': ['Name', 'Events', 'Academic_year', 'Hometown', 'State_or_country', 'High_school', 'Club team', 'Link'],
    'mswim': ['Name', 'Events', 'Academic_year', 'Hometown', 'State_or_country', 'High_school', 'Club team', 'Link'],
    'fh': ['Jersey_number', 'Name', 'Position', 'Height', 'Academic_year', 'Hometown', 'State_or_country',
           'High_school', 'Previous school', 'Link'],
    'lax': ['Jersey_number', 'Name', 'Position', 'Height', 'Academic_year', 'Hometown', 'State_or_country',
            'High_school', 'Previous school', 'Link'],
    'wrestling': ['Name', 'Academic_year', 'Hometown', 'State_or_country', 'High_school', 'Weight', 'Link'],
    'vb': ['Jersey_number', 'Name', 'Position', 'Height', 'Academic_year', 'Hometown', 'State_or_country',
           'High_school', 'Link'],
    'test': ['Jersey_number', 'Name', 'Position', 'Height', 'Academic_year', 'Hometown', 'State_or_country',
             'High_school', 'Link']
}

split_cols = {'wbb': 5, 'mbb': 5, 'wsoc': 5, 'msoc': 5, 'mtf': 3, 'wtf': 3, 'wxc': 2, 'mxc': 2, 'wswim': 3, 'mswim': 3,
              'fh': 5, 'lax': 5, 'wrestling': 2, 'vb': 5, 'test': 5}

table_idx = {'wbb': 2, 'mbb': 2, 'wsoc': 2, 'msoc': 2, 'mtf': 3, 'wtf': 2, 'wxc': 2, 'mxc': 3, 'wswim': 2, 'mswim': 3,
             'fh': 2, 'lax': 2, 'wrestling': 2, 'vb': 2, 'test': 2}


class Scraper:
    def __init__(self, sport: str):
        self.sport = sport
        self.url = f'https://aueagles.com/sports/{sports_dict.get(sport)}/roster?view=2'
        self.csv = f'CSVs/aueagles-{sport}-roster.csv'
        self.headers = sports_headers.get(sport)
        self.__payload = {'view': 2}
        self.__r = requests.get(self.url, params=self.__payload)
        self.table = BeautifulSoup(self.__r.text, 'html.parser').find_all('table')[table_idx.get(sport)]
        self.col = split_cols.get(sport)
        self.dict = {}

    def make_dict(self):
        target_i = self.headers.index('State_or_country')
        h_list = self.headers[:target_i]
        for i in h_list:
            self.dict.update({i: h_list.index(i)})

    def scrape(self):
        self.make_dict()

        with open(self.csv, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=self.headers)

            writer.writeheader()

            for row in self.table.find_all('tr')[1:]:
                cells = row.find_all('td')

                if self.sport in ['wbb', 'mbb', 'msoc', 'wsoc', 'fh', 'lax', 'vb', 'test']:
                    Jersey_number = cells[0].text.strip()

                Link = cells[self.dict.get('Name')].find('a').get('href')
                url = ''
                if Link:
                    url = f'https://aueagles.com{Link}'

                Name = cells[self.dict.get('Name')].text.strip()

                if self.sport in ['wbb', 'mbb', 'msoc', 'wsoc', 'fh', 'lax', 'vb', 'test']:
                    pos_list = [cells[self.dict.get('Position')].string.strip()]
                    for pos in pos_list:
                        Position = position_fixes.get(pos, pos)

                if self.sport in ['mtf','wtf','mswim','wswim']:
                    Events = cells[self.dict.get('Event')].string.strip()

                if self.sport in ['wbb', 'mbb', 'msoc', 'wsoc', 'fh', 'lax', 'vb', 'test']:
                    Height = cells[self.dict.get('Height')].text.strip()

                yr_list = [cells[self.dict.get('Academic_year')].string.strip()]
                for yr in yr_list:
                    Academic_year = year_fixes.get(yr, yr)

                Hometown = cells[self.dict.get('Hometown')].text.split(' / ')[0].split(', ')[0]
                region = [cells[self.dict.get('Hometown')].text.split(' / ')[0].split(', ')[1]]
                for s in region:
                    State = state_fixes.get(s, s)
                High_school = cells[self.dict.get('Hometown')].text.split(' / ')[1]

                if self.sport == 'wrestling':
                    Weight = cells[self.dict.get('Hometown')+1].string.strip()

                if self.sport in ['wsoc', 'mtf', 'wtf', 'mxc', 'wxc', 'fh', 'lax']:
                    Previous_school = cells[self.dict.get('Hometown')+1].string.strip()

                if 'swim' in self.sport:
                    Club_team = cells[self.dict.get('Hometown')+1].string.strip()

                if self.sport in ['mbb', 'wbb', 'msoc', 'vb']:
                    writer.writerow({
                        'Jersey_number': Jersey_number,
                        'Name': Name,
                        'Position': Position,
                        'Height': Height,
                        'Academic_year': Academic_year,
                        'Hometown': Hometown,
                        'State_or_country': State,
                        'High_school': High_school,
                        'Link': url
                    })
                elif self.sport in ['wsoc', 'fh', 'lax']:
                    writer.writerow({
                        'Jersey_number': Jersey_number,
                        'Name': Name,
                        'Position': Position,
                        'Height': Height,
                        'Academic_year': Academic_year,
                        'Hometown': Hometown,
                        'State_or_country': State,
                        'High_school': High_school,
                        'Previous_school': Previous_school,
                        'Link': url
                    })
                elif 'tf' in self.sport:
                    writer.writerow({
                        'Name': Name,
                        'Events': Events,
                        'Academic_year': Academic_year,
                        'Hometown': Hometown,
                        'State_or_country': State,
                        'High_school': High_school,
                        'Previous_school': Previous_school,
                        'Link': url
                    })
                elif 'xc' in self.sport:
                    writer.writerow({
                        'Name': Name,
                        'Academic_year': Academic_year,
                        'Hometown': Hometown,
                        'State_or_country': State,
                        'High_school': High_school,
                        'Previous_school': Previous_school,
                        'Link': url
                    })
                elif 'swim' in self.sport:
                    writer.writerow({
                        'Name': Name,
                        'Events': Events,
                        'Academic_year': Academic_year,
                        'Hometown': Hometown,
                        'State_or_country': State,
                        'High_school': High_school,
                        'Club_team': Club_team,
                        'Link': url
                    })
                elif self.sport == 'wrestling':
                    writer.writerow({
                        'Name': Name,
                        'Weight': Weight,
                        'Academic_year': Academic_year,
                        'Hometown': Hometown,
                        'State_or_country': State,
                        'High_school': High_school,
                        'Link': url
                    })

            print(f'Wrote {self.csv}')
