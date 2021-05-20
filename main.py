import datetime as dt
from scraper_provider import ScraperProvider


date_to = input("Which year you want to travel to? Type the date in YYYY-MM-DD: ").split("-")

try:
    year = int(date_to[0])
    month = int(date_to[1])
    day = int(date_to[2])
    date = dt.date(year=year, month=month, day=day)
except IndexError:
    print("Please, enter full date.")
except ValueError as err:
    print(f"Please, type correct data format. {err}.")
else:
    scrapper = ScraperProvider(str(date))
    data = scrapper.search_hot_100()
