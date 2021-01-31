# HR API 
###  Configrations and Setup :left_speech_bubble: :

* To Test HR-API : 
- [x] Start container of DB Server by command:
```
docker run --name db-mariadb -e MYSQL_ROOT_PASSWORD=mariadb -e MYSQL_DATABASE=HRapp -p 3306:3306 -d mariadb

```
- [x] Edit Debug configration on PyCharm and add the Target to be : ~/HrAPI/run.py

________________________________________________________

# API Testing by Postman

### Test ``` /register ``` view :
- [x] open ``` templates/register.htm ``` Form by browser and insert candidate data

### Test ``` /list ``` view :
- [x] by Postman add X-ADMIN = 1 to give it authorization

### Test ``` /dowload/[id] ``` view :
- [x] by Postman add X-ADMIN = 1 to give it authorization
- [x] add id of the resume in the link 

### Setup  :+1: :
- [x] PyCharm Application
- [x] Python-3 
- [x] Flask
- [x] Docker container to run DB
- [x] Postman to test API End-points





