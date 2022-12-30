import requests
import json

new_info = {
"id": 665,
"category": {"id": 2,"name": "Dog"},
"name": "Demon",
"photoUrls": ["string"],
"tags": [{"id": 0,"name": "string"}],
"status": "available"
}
response = requests.put(f"https://petstore.swagger.io/v2/pet/665",
    headers={'accept': 'application/json', 'Content-Type': 'application/json'},
    data=json.dumps(new_info, ensure_ascii=False))
print(response.status_code)
print(response.json())