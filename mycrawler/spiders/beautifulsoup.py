import requests
from bs4 import BeautifulSoup

session = requests.Session()
loginpage = session.get("https://www.researchgate.net/login")
request_token = BeautifulSoup(loginpage.text).form.find("input",{"name":"request_token"}).attrs["value"]
print (request_token)
params = {"request_token":request_token,
          "invalidPasswordCount":"0",
          'login': 'zz-sasharma@fullerton.edu', 
          'password': '23811986',
          "setLoginCookie":"yes"
          }
session.post("https://www.researchgate.net/login", data = params)
s = session.get("https://www.researchgate.net/search.Search.html?type=researcher&query=samit")
print (BeautifulSoup(s.text).header)


