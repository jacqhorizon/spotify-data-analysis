# Spotify Data Analysis

## Files

**analysis.ipynb** - data cleaning and analysis, the meat and potatoes

**spotify.py** - gets last 500 saved tracks and their artists from Spotify

**lastfm.py** - gets genre associated with artist name from Last FM

**tracks.csv** - last 500 saved tracks

**artists.csv** - artists for corresponding tracks

**artists_missing_genres.csv** - the genres that Spotify didn't have

## Anaconda Environment

Set up your Anaconda environment

```{python}
conda env create -f requirements.yml
conda activate AD_450_final
```

## Generating the Data

### Spotify

I followed [These Instructions](https://developer.spotify.com/documentation/web-api/tutorials/getting-started) to get my Client ID and Client Secret

I stored the client id and secret in my virtual environment session like so:

```{python}
export CLIENT_ID="client_id"
export CLIENT_SECRET="client_secret"
```

### LastFM

I followed [These Instructions](https://www.last.fm/api/authentication) to get my LastFM API Key.

I stored the LastFM API Key in my virtual environment session like so:

```{python}
export LASTFM_API_KEY="lastfm_api_key"
```
