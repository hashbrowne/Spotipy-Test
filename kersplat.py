import spotipy
import spotipy.oauth2

#once you have your id and secret, place them in the instances below
CLIENT_ID = '' 
CLIENT_SECRET = ''
CLIENT_REDIRECT_URI = 'http://localhost:8888' #redirect url using generic local host
scp = spotipy.oauth2.SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

sp = spotipy.Spotify(client_credentials_manager=scp)

results = sp.search(q='The Strokes', limit=50)

for i, t in enumerate(results['tracks']['items']):
    print(' ', i, t['name'])
