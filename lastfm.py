import requests
from urllib.parse import urlencode

API_KEY = '0dbefd6438ab68b6337f83c68ea8f234'
SECRET = '37c0307f58eadbf302b9a5d49cfbae91'


def get_lastfm_genre(artist_name):
    base_url = "https://ws.audioscrobbler.com/2.0/"
    params = {
        'method': 'artist.getInfo',
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
        tags = resp['artist']['tags']['tag']
        if len(tags) > 0:
            return tags[0]['name']
        else:
            return None
    else:
        print({"error": f"Request failed with status code {response.status_code}"})
        return None

inspect = {"artist":{"name":"noturgf","url":"https://www.last.fm/music/noturgf","image":[{"#text":"https://lastfm.freetls.fastly.net/i/u/34s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"small"},{"#text":"https://lastfm.freetls.fastly.net/i/u/64s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"medium"},{"#text":"https://lastfm.freetls.fastly.net/i/u/174s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"large"},{"#text":"https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png","size":"extralarge"},{"#text":"https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png","size":"mega"},{"#text":"https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png","size":""}],"streamable":"0","ontour":"0","stats":{"listeners":"527063","playcount":"5449735"},"similar":{"artist":[{"name":"fam0uz","url":"https://www.last.fm/music/fam0uz","image":[{"#text":"https://lastfm.freetls.fastly.net/i/u/34s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"small"},{"#text":"https://lastfm.freetls.fastly.net/i/u/64s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"medium"},{"#text":"https://lastfm.freetls.fastly.net/i/u/174s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"large"},{"#text":"https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png","size":"extralarge"},{"#text":"https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png","size":"mega"},{"#text":"https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png","size":""}]},{"name":"Mckyyy","url":"https://www.last.fm/music/Mckyyy","image":[{"#text":"https://lastfm.freetls.fastly.net/i/u/34s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"small"},{"#text":"https://lastfm.freetls.fastly.net/i/u/64s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"medium"},{"#text":"https://lastfm.freetls.fastly.net/i/u/174s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"large"},{"#text":"https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png","size":"extralarge"},{"#text":"https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png","size":"mega"},{"#text":"https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png","size":""}]},{"name":"LucidBeatz","url":"https://www.last.fm/music/LucidBeatz","image":[{"#text":"https://lastfm.freetls.fastly.net/i/u/34s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"small"},{"#text":"https://lastfm.freetls.fastly.net/i/u/64s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"medium"},{"#text":"https://lastfm.freetls.fastly.net/i/u/174s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"large"},{"#text":"https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png","size":"extralarge"},{"#text":"https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png","size":"mega"},{"#text":"https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png","size":""}]},{"name":"LUNACYCL","url":"https://www.last.fm/music/LUNACYCL","image":[{"#text":"https://lastfm.freetls.fastly.net/i/u/34s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"small"},{"#text":"https://lastfm.freetls.fastly.net/i/u/64s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"medium"},{"#text":"https://lastfm.freetls.fastly.net/i/u/174s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"large"},{"#text":"https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png","size":"extralarge"},{"#text":"https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png","size":"mega"},{"#text":"https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png","size":""}]},{"name":"Baltra","url":"https://www.last.fm/music/Baltra","image":[{"#text":"https://lastfm.freetls.fastly.net/i/u/34s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"small"},{"#text":"https://lastfm.freetls.fastly.net/i/u/64s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"medium"},{"#text":"https://lastfm.freetls.fastly.net/i/u/174s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"large"},{"#text":"https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png","size":"extralarge"},{"#text":"https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png","size":"mega"},{"#text":"https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png","size":""}]}]},"tags":{"tag":[]},"bio":{"links":{"link":{"#text":"","rel":"original","href":"https://last.fm/music/noturgf/+wiki"}},"published":"15 Apr 2024, 14:46","summary":"noturgf is a Spotify artist and makes cover songs. Their goal is to make the best possible content to wow their audience. With over 7 million monthly listeners noturgf has been an impact on the music community for her taste in music. She mainly focuses on Hip-hop and rap. <a href=\"https://www.last.fm/music/noturgf\">Read more on Last.fm</a>","content":"noturgf is a Spotify artist and makes cover songs. Their goal is to make the best possible content to wow their audience. With over 7 million monthly listeners noturgf has been an impact on the music community for her taste in music. She mainly focuses on Hip-hop and rap. <a href=\"https://www.last.fm/music/noturgf\">Read more on Last.fm</a>. User-contributed text is available under the Creative Commons By-SA License; additional terms may apply."}}}
print(len(inspect['artist']['tags']['tag']))