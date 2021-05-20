from bs4 import BeautifulSoup


class SoupHandler:
    """
    Handles raw page data to make list of top-100 songs titles
    """

    def __init__(self, raw_page_data):
        self.data = raw_page_data

    def return_songs_list(self):
        soup = BeautifulSoup(self.data, "html.parser")
        title_elements = soup.find_all(name="span",
                                       class_="chart-element__information__song text--truncate color--primary")
        songs_list = [song.getText() for song in title_elements]
        return songs_list
