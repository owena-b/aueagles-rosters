# American University Athletics rosters

Python programs to scrape data tables from [AU Athletics' website](https://aueagles.com/) containing the rosters for its various NCAA Division I teams. Aimed at streamlining data collection for sports journalists.

It formats the data into a CSV for a single team in which each line is one player. The code also fixes abbreviations and height formatting, and it separates the hometown, state/country, and high school into their own columns.

**Teams (and corresponding CSV files):**\
Men's Basketball ([CSV](CSVs/aueagles-mbb-roster.csv))\
Women's Basketball ([CSV](CSVs/aueagles-wbb-roster.csv))\
Men's Soccer ([CSV](CSVs/aueagles-msoc-roster.csv))\
Women's Soccer ([CSV](CSVs/aueagles-wsoc-roster.csv))\
Men's Cross Country ([CSV](CSVs/aueagles-mxc-roster.csv))\
Women's Cross Country ([CSV](CSVs/aueagles-wxc-roster.csv))\
Men's Track and Field ([CSV](CSVs/aueagles-mtf-roster.csv))\
Women's Track and Field ([CSV](CSVs/aueagles-wtf-roster.csv))\
Men's Swimming and Diving ([CSV](CSVs/aueagles-mswim-roster.csv))\
Women's Swimming and Diving ([CSV](CSVs/aueagles-wswim-roster.csv))\
Field Hockey ([CSV](CSVs/aueagles-fh-roster.csv))\
Lacrosse ([CSV](CSVs/aueagles-lax-roster.csv))\
Volleyball ([CSV](CSVs/aueagles-vb-roster.csv))\
Wrestling ([CSV](CSVs/aueagles-wrestling-roster.csv))

**How to use these files:**\
Click the CSV link for the team you want data on. On the right of the screen, below "History," you can download the raw file. It will download a CSV (comma-separated values) file, which you can import into the spreadsheet software of your choosing. In Google Sheets, you can import the CSV into a new or existing spreadsheet. Remember, always double-check your data!

**A little about the methodology (for snooping data editors):**\
Originally, I wrote [several different](old-scrapers) Python programs, one for each sport. This helped me find the differences in each sport's web table, but I quickly realized it was a lot of repeated code. So, I took an object-oriented approach. I created a single Scraper class that was compatible with every sport, and relied on a number of if/else statements to correct for the differences in each table.

[main.py](main.py) simply creates Scraper-class objects for each sport then calls the scrape() method on each object. [oop_scrape.py](oop_scrape.py) houses the Scraper class and a bunch of dictionaries that allow it to work for all the sports. [fixes.py](fixes.py) contains dictionaries that correct abbreviations and misspellings in the source data.
