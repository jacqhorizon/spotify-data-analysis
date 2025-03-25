import requests
from urllib.parse import urlencode

API_KEY = '0dbefd6438ab68b6337f83c68ea8f234'
SECRET = '37c0307f58eadbf302b9a5d49cfbae91'


def get_lastfm_genre(artist_name):
    base_url = "https://ws.audioscrobbler.com/2.0/"
    params = {
        'method': 'artist.getTopTags',
        'artist': artist_name,
        'api_key': API_KEY,
        'autocorrect': '1',
        'format': 'json'
    }
    query_string = urlencode(params, safe=' ', encoding='utf-8').replace("+", "%20")
    url = f'{base_url}?{query_string}'

    headers = {
        'User-Agent': 'Data-Science-project'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        resp = response.json()
        tags = resp['toptags']['tag']
        if len(tags) > 0:
            return tags[0]['name']
        else:
            return None
    else:
        print({"error": f"Request failed with status code {response.status_code}"})
        return None

# # na_genres_df = na_genres_df[na_genres_df['artist_name'].unique()]
# for index, row in na_genres_df.iterrows():
#     print(index, row['artist_name'])
#     if row['artist_name']:
#         genre = get_lastfm_genre(row['artist_name'])
#         print(genre)
#         if genre:
#             na_genres_df.loc[index, 'genres'] = genre
# na_genres_df.to_csv('artists_missing_genres.csv', index=False)