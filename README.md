# American University Athletics rosters

Python programs to scrape data tables from [AU Athletics' website](https://aueagles.com/) containing the rosters for its various NCAA Division I teams. Aimed at streamlining data collection for sports journalists.

It formats the data into a CSV for a single team in which each line is one player. The code also fixes abbreviations and height formatting, and it separates the hometown, state/country, and high school into their own columns.

**Teams (their Python code and corresponding CSV files):**\
[Men's Basketball](mbb-scrape.py) ([CSV](CSVs/aueagles-mbb-roster.csv))\
[Women's Basketball](wbb-scrape.py) ([CSV](CSVs/aueagles-wbb-roster.csv))\
[Men's Cross Country](xc-scrape.py) ([CSV](CSVs/aueagles-mxc-roster.csv))\
[Women's Cross Country](xc-scrape.py) ([CSV](CSVs/aueagles-wxc-roster.csv))\
[Men's Track and Field](tf-scrape.py) ([CSV](CSVs/aueagles-mtf-roster.csv))\
[Women's Track and Field](tf-scrape.py) ([CSV](CSVs/aueagles-wtf-roster.csv))\
[Men's Swimming and Diving](swim-dive-scrape.py) ([CSV](CSVs/aueagles-mswim-roster.csv))\
[Women's Swimming and Diving](swim-dive-scrape.py) ([CSV](CSVs/aueagles-wswim-roster.csv))

**How to use these files:**\
Click the CSV link for the team you want data on. On the right of the screen, below "History," you can download the raw file. It will download a CSV (comma-separated values) file, which you can import into the spreadsheet software of your choosing. In Google Sheets, you can import the CSV into a new or existing spreadsheet.

**A little about the methodology (for snooping data editors):**\
I created separate Python programs because tables on the Athletics website (even different genders of the same sport) were organized differently. Men's basketball, for example, had height in the fourth column from the left (indexed to 3), but the women's team had height in the fifth column (indexed to 4).

The sports themselves had to be separated: Swimming and Diving had a column for "Events" and "Club Team", whereas Cross County and Track and Field did not. I was able to use one program for each of those three (Swim, XC, and T&F) instead of two, one for each gender (e.g. Basketball), by implementing variables for each gender's table and CSV file, then interating over the two tables. It added to the time complexity, but will be easier for the reporters (who may not know Python) to use after I am gone to create CSVs for future teams.