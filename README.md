# American University Athletics rosters

Python programs to scrape data tables from [AU Athletics' website](https://aueagles.com/) containing the rosters for its various NCAA Division I teams. Aimed at streamlining data collection for sports journalists.

It formats the data into a CSV for a single team in which each line is one player. The client can choose which team. The code also fixes abbreviations and height formatting, and it separates the hometown, state/country, and high school into their own columns.

**Teams:**\
[Men's Basketball](mbb-scrape.py) ([CSV](aueagles-mbb-roster.csv))\
[Women's Basketball](wbb-scrape.py) ([CSV](aueagles-wbb-roster.csv))

**A little about the methodology...**\
I created separate Python programs because tables on the Athletics website (even different genders of the same sport) indexed differently. Men's basketball, for example, had height in the fourth column from the left, but the women's team had height in the third column.