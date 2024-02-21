# American University Athletics rosters

Python programs to scrape data tables from [AU Athletics' website](https://aueagles.com/) containing the rosters for its various NCAA Division I teams. Aimed at streamlining data collection for sports journalists.

It formats the data into a CSV for a single team in which each line is one player. The code also fixes abbreviations and height formatting, and it separates the hometown, state/country, and high school into their own columns.

**Teams:**\
[Men's Basketball](mbb-scrape.py) ([CSV](aueagles-mbb-roster.csv))\
[Women's Basketball](wbb-scrape.py) ([CSV](aueagles-wbb-roster.csv))

**How to use these files:**\
Click the CSV link for the team you want data on. On the right of the screen, below "History," you can download the raw file. It will download a CSV (comma-separated values) file, which you can import into the spreadsheet software of your choosing. In Google Sheets, you can import the CSV into a new or existing spreadsheet.

**A little about the methodology (for snooping data editors):**\
I created separate Python programs because tables on the Athletics website (even different genders of the same sport) were organized differently. Men's basketball, for example, had height in the fourth column from the left (indexed to 3), but the women's team had height in the fifth column (indexed to 4).