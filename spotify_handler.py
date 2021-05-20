import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

SPOTIFY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = "http://example.com"


class SpotifyHandler:
    """
    Connects with Spotify to create and add tracks to a particular playlist for user
    """

    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri=SPOTIFY_REDIRECT_URI,
            client_id=SPOTIFY_CLIENT_ID,
            client_secret=SPOTIFY_CLIENT_SECRET,
            show_dialog=True,
            cache_path="token.txt"
        )
        )
        self.user_id = self.sp.current_user()["id"]
        self.song_uris = []

    def create_songs_uri_list(self, songs_list, year):
        for song in songs_list:
            result = self.sp.search(q=f"track:{song} year:{year}", type="track")
            try:
                uri = result["tracks"]["items"][0]["uri"]
                self.song_uris.append(uri)
            except IndexError:
                print(f"{song} doesn't exist in Spotify. Skipping.")

    def create_playlist(self, date:str):
        playlist = self.sp.user_playlist_create(self.user_id, f"{date}  Billboard 100",
                                                public=False)
        playlist_id = playlist["id"]
        self.sp.user_playlist_add_tracks(user=self.user_id, playlist_id=playlist_id, tracks=self.song_uris)
