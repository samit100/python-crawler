import requests
from bs4 import BeautifulSoup

# session = requests.Session()
# loginpage = session.get("https://www.researchgate.net/login")
# request_token = BeautifulSoup(loginpage.text).form.find("input",{"name":"request_token"}).attrs["value"]
# print (request_token)
# params = {"request_token":request_token,
#           "invalidPasswordCount":"0",
#           'login': 'zz-sasharma@fullerton.edu', 
#           'password': '23811986',
#           "setLoginCookie":"yes"
#           }
# session.post("https://www.researchgate.net/login", data = params)
# s = session.get("https://www.researchgate.net/institution/California_State_University_Fullerton/members?page=1")
s = requests.get("https://www.researchgate.net/institution/California_State_University_Fullerton/members?page=1")
pageBody = BeautifulSoup(s.text).body
#print(pageBody)

def match_class(target):                                                        
    def do_match(tag):                                                          
        classes = tag.get('class', [])                                          
        return all(c in classes for c in target)                                
    return do_match

allUrls = pageBody.find_all(match_class(["display-name"]))

file1 = open("facultyurls.txt","a") 
#file1.write(str(allUrls)) 


for m in allUrls:
    file1.write ("https://www.researchgate.net/"+str(m.attrs['href']))
    file1.write("\n")

file1.close() 

