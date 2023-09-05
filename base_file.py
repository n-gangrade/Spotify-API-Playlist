# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 20:08:53 2023

@author: navdh
"""

import json
import requests
import secretsss
from pprint import pprint

class lastFMSpotify:
    def __init__(self):
        self.token = secretsss.spotify_token()
        self.api_key = secretsss.last_fm_api_key()
        self.user_id = secretsss.spotify_user_id()
        self.spotify_headers = {"Content-Type": "application/json", "Authorization": f"Bearer {self.token}"}
        self.playlist_id = ''
        
    def fetch_songs_from_lastfm(self):
        params = {'limit': 5, 'api_key': self.api_key}
        url = f'http://ws.audioscrobbler.com/2.0/?method=chart.gettoptracks&api_key={self.api_key}&format=json'
        response = requests.get(url, params=params)
        if (response.status_code != 200):
            print("ERROR")
        res = response.json()
        for item in res['tracks']['track']:
            song = item['name'].title()
            artist = item['artist']['name'].title()
            print(song, artist)
            self.get_uri_from_spotify(song, artist)
        
    def get_uri_from_spotify(self, song_name, artist):
        
        url = f'https://api.spotify.com/v1/search?query=track%3A{song_name}+artist%3A{artist}&type=track&offset=0&limit=10'
        
        response = requests.get(url, headers=self.spotify_headers)
        res = response.json()
        for item in res['tracks']['items']:
            pprint(item)
            print("\n\n")
    
    def create_spotify_playlist(self):
        data = {
            "name": "LastFM top songs",
            "description": "Songs from topcharts",
            "public": False
        }
    
    def add_songs_to_playlist(self):
        pass
    
    def list_songs_in_playlist(self):
        pass
        
d = lastFMSpotify()
d.fetch_songs_from_lastfm()
