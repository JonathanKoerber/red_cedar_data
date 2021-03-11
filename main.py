
__author__ = 'bdm4'

import requests
import json
import subprocess
import sys

from requests import session

import api_key


authorize_url = api_key.secret.get('AUTHORIZE')
callback_uri = api_key.secret.get('CALL_BACK_URL')
app_id = api_key.secret.get('APPLICATION_ID')
app_secret = api_key.secret.get('SECRET')
auth_code = api_key.secret.get('CODE')
user_name = api_key.secret.get('USER_NAME')
password = api_key.secret.get('PASSWORD')

site = "https://www.inaturalist.org"
token_url = "https://www.inaturalist.org/users/api_token"
test_api_url = "https://api.inaturalist.org/"

# todo check to see token is null or old revoke ==>> use OR revoke.

# todo authorize redirect obtain auth_code get the ETag out to use as auth_code
url = site+'/oauth/authorize?client_id='+app_id+'&redirect_uri='+callback_uri+'&response_type=code'
auth_response = requests.get(url)

data = {'grant_type': 'authorization_code', 'redirect_uri': callback_uri}

# todo add auth_code to gain token
payload = {
    'grant_type': "client_credentials"
}
# return token
access_token_response = requests.post(site+'/oauth/token', data=payload, verify=False, allow_redirects=False, auth=(app_id, app_secret))

# we can now use the access_token as much as we want to access protected resources.
tokens = json.loads(access_token_response.text)
print("tokens", tokens)
access_token = tokens['access_token']
print(access_token_response.text)
