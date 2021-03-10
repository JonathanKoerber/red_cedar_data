
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



url = site+'/oauth/authorize?client_id='+app_id+'&redirect_uri='+callback_uri+'&response_type=code'

auth_code = session(url)
print(auth_code)

print("go to the following url on the browser and enter the code from the returned url: ")
#print("---  " + authorization_redirect_url + "  ---")

data = {'grant_type': 'authorization_code', 'redirect_uri': callback_uri}
print("requesting access token")
# token_url, data=data, verify=False, allow_redirects=False, auth=(client_id, client_secret)
# secets payload
payload = {
    'client_id': app_id,
    'client_secret': app_secret,
    'code': auth_code,
    'redirect_uri': callback_uri,
    'grant_type': "authorization_code"
}
access_token_response = requests.post(site+'/oauth/token', data=payload)
#access_token_response = requests.post(url)
print("response")
print(access_token_response.headers)

# we can now use the access_token as much as we want to access protected resources.
tokens = json.loads(access_token_response.text)
print("tokens", tokens)
access_token = tokens['access_token']
# print("access token: " + access_token)

api_call_headers = {'Authorization': 'Bearer ' + access_token}
api_call_response = requests.get(test_api_url, responce_type=api_key.secret.get('CODE'), headers=api_call_headers, verify=False)

print(api_call_response.text)