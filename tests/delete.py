import requests

header = {"x-api-key": "reqres_3ab6740f4672424f868ab877f5963061"}
url = "https://reqres.in/api/users/2"

response = requests.delete(url, headers=header)

print(response.status_code)
print(response.text)