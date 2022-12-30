# добавление питомца
import requests
import json
info = {
"id": 665,
"category": {"id": 2,"name": "Cat"},
"name": "Demon",
"photoUrls": ["string"],
"tags": [{"id": 0,"name": "string"}],
"status": "available"
}
res_post_addNewPet = requests.post(f"https://petstore.swagger.io/v2/pet",
                                  headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                                  data = json.dumps(info, ensure_ascii=False))
print(f"Статус ответа от сервера на POST запрос добавление питомца: {res_post_addNewPet.status_code}")