import requests
import json
import urllib.parse

headers = {
    'Accept-Language': 'en-US,en;q=0.8',
    'Accept-Encoding': 'gzip',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; U; Linux x86_64; it; rv:1.9.0.8) Gecko/2009033100 Ubuntu/9.04 (jaunty) Firefox/3.0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Connection': 'keep-alive'
}

base_url = 'https://swapi.co/api'


def query_all(resource, search=None):

    if search:
        search = urllib.parse.quote(search)
        search_string = f'&search={search}'
    else:
        search_string = ''

    response = requests.get(f'{base_url}/{resource}/?format=json{search_string}', headers=headers)
    if response.status_code != 200:
        raise Exception('resource not found!')
    json_data = json.loads(response.content)
    results = json_data['results']

    while json_data['next']:
        response = requests.get(json_data['next'], headers=headers)
        if response.status_code != 200:
            raise Exception('resource not found!')
        json_data = json.loads(response.content)
        results += json_data['results']
    return results
