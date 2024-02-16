from dotenv import load_dotenv
import os
import base64
import json
from requests import post, get
import urllib.parse

load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
BASE_URL = 'https://api.spotify.com/v1/'

auth_code = get(AUTH_URL, {
    'client_id': client_id,
    'response_type': 'code',
    'redirect_uri': 'https://open.spotify.com/collection/playlists',
    'scope': 'playlist-modify-private',
})

def get_token():
    auth_string = client_id + ':' + client_secret
    auth_bytes = auth_string.encode('utf-8')
    auth_base64 = str(base64.b64encode(auth_bytes), 'utf-8')

    url = 'https://accounts.spotify.com/api/token'

    headers = {
        'Authorization' : 'Basic ' + auth_base64,
        'Content-Type' : 'application/x-www-form-urlencoded' 
    }

    data = {'grant_type' : 'client_credentials'}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result['access_token']
    return token

def get_auth_header(token):
    return {'Authorization' : 'Bearer ' + token}

def search_for_artist(token, artist_name):
    url = 'https://api.spotify.com/v1/search'
    headers = get_auth_header(token)
    query = f'?q={artist_name}&type=artist&limit=1'

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)
    print(json_result)

def get_recently_played_tunes(token, before_date = None, after_date = None, limit = None):
    url = 'https://api.spotify.com/v1/me/player/recently-played'
    headers = get_auth_header(token)
    
    # Initialize parameters dictionary
    params = {}
    if before_date is not None:
        params['before'] = before_date
    if after_date is not None:
        params['after'] = after_date
    if limit is None:
        params['limit'] = 50

    result = get(url, headers=headers, params=params)
    json_result = json.loads(result.content)
    return json_result

    result = get(url, header = headers)
    json_result = json.loads(result.content)

# token = get_token()

print(get_token())