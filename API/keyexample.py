import requests

url = 'https://api.nettoolkit.com/v1/account/test-api-keys'
headers = {'X-API-KEY': 'test_Dw0SAjquHMU7U7VvRdORr6pXGS0eiq3CWIm64acg'}

response = requests.get(url, headers = headers)

print ("\n status:" , response.status_code)
print ("\n content:", response.content)
print ("\n text:", response.text)
print ("\n json:", response.json)