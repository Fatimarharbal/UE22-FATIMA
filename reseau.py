import requests as rq
reponse = rq.get("https://mines.bmarchand.fr/api/users/260")
print(reponse.content)
jsonn = {"token": "CqzX8917", "status": "presente"}

reponse = rq.patch("https://mines.bmarchand.fr/api/users/260", json = jsonn)
 