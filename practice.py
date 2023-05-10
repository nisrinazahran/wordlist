import requests

api_key= '4246785f-f698-4a5a-93aa-76f13d6ee593'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

r = requests.get(url)
result = r.json()
print(result)