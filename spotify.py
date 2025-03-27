import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import csv
import os
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

def authorize_sp():
    scope = "user-library-read"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,
                                                   client_id=CLIENT_ID,
                                                   client_secret=CLIENT_SECRET,
                                                   redirect_uri='http://127.0.0.1:3000'))
    return(sp)

def create_csvs(sp, quantity):
    results = sp.current_user_saved_tracks()
    count = 0
    artist_list = set()
    with open('tracks.csv', mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(['added_at', 'track_id', 'track_name', 'artist_id',
                        'artist_name', 'duration', 'explicit', 'popularity',
                         'album_type', 'album_id', 'album_name', 'album_release_date'])
        while results['next'] and count < quantity:
            count += len(results['items'])
            print(f'writing {len(results['items'])} items out of {count}')
            for idx, item in enumerate(results['items']):
                track = item['track']
                artist_list.add(track['artists'][0]['id'])
                writer.writerow([item['added_at'], track['id'], track['name'], track['artists'][0]['id'],
                                track['artists'][0]['name'], track['duration_ms'], track['explicit'], track['popularity'],
                                track['album']['album_type'], track['album']['id'], track['album']['name'], track['album']['release_date']])
            results = sp.next(results)

    with open('artists.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            ['id', 'artist_name', 'followers', 'genres', 'popularity'])
        for artist_id in artist_list:
            artist = sp.artist(artist_id)
            genre = 'null'
            if len(artist['genres']) > 0:
                genre = artist['genres'][0]
            print(f'writing info for {artist['name']}')
            writer.writerow([artist['id'], artist['name'],
                            artist['followers']['total'], genre, artist['popularity']])

sp=authorize_sp()
# create_csvs(sp, 500)