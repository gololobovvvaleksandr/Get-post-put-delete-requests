import requests
BASE_URL = 'https://petstore.swagger.io/v2/pet/665'
response = requests.delete(f"{BASE_URL}")
print(response.json())
