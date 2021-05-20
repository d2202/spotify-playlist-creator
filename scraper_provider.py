import requests

HOT_100_URL = "https://www.billboard.com/charts/hot-100/"


class ScraperProvider:
    """
    Provides scraping HOT_100_URL with particular date to find top-100 songs
    """

    def __init__(self, date: str):
        self.search_url = HOT_100_URL + date
        self.search_hot_100()

    def search_hot_100(self):
        response = requests.get(url=self.search_url)
        response.raise_for_status()
        page_data = response.text
        return page_data
