# American University Athletics rosters

Python programs to scrape data tables from [AU Athletics' website](https://aueagles.com/) containing the rosters for its various NCAA Division I teams. Aimed at streamlining data collection for sports journalists.

It formats the data into a CSV for a single team in which each line is one player. The code also fixes abbreviations and height formatting, and it separates the hometown, state/country, and high school into their own columns.

**Teams (their Python code and corresponding CSV files):**\
[Men's Basketball](old-scrapers/mbb-scrape.py) ([CSV](CSVs/aueagles-mbb-roster.csv))\
[Women's Basketball](old-scrapers/wbb-scrape.py) ([CSV](CSVs/aueagles-wbb-roster.csv))\
[Men's Soccer](old-scrapers/msoc-scrape.py) ([CSV](CSVs/aueagles-msoc-roster.csv))\
[Women's Soccer](old-scrapers/wsoc-scrape.py) ([CSV](CSVs/aueagles-wsoc-roster.csv))\
[Men's Cross Country](old-scrapers/xc-scrape.py) ([CSV](CSVs/aueagles-mxc-roster.csv))\
[Women's Cross Country](old-scrapers/xc-scrape.py) ([CSV](CSVs/aueagles-wxc-roster.csv))\
[Men's Track and Field](old-scrapers/tf-scrape.py) ([CSV](CSVs/aueagles-mtf-roster.csv))\
[Women's Track and Field](old-scrapers/tf-scrape.py) ([CSV](CSVs/aueagles-wtf-roster.csv))\
[Men's Swimming and Diving](old-scrapers/swim-dive-scrape.py) ([CSV](CSVs/aueagles-mswim-roster.csv))\
[Women's Swimming and Diving](old-scrapers/swim-dive-scrape.py) ([CSV](CSVs/aueagles-wswim-roster.csv))

**How to use these files:**\
Click the CSV link for the team you want data on. On the right of the screen, below "History," you can download the raw file. It will download a CSV (comma-separated values) file, which you can import into the spreadsheet software of your choosing. In Google Sheets, you can import the CSV into a new or existing spreadsheet.

**A little about the methodology (for snooping data editors):**\
CURRENTLY WIP.