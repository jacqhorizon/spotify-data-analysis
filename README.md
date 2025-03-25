# Spotify Data Analysis

1. Follow [These Instructions](https://developer.spotify.com/documentation/web-api/tutorials/getting-started) to get your Client ID and Client Secret

2. Set up your Anaconda environment

```{python}
conda env create -f requirements.yml
conda activate AD_450_final
```

3. Store your client id and secret in your virtual environment session

```{python}
export CLIENT_ID="client_id"
export CLIENT_SECRET="client_secret"
```

Files

spotify.py - gets last 500 saved tracks and their artists
