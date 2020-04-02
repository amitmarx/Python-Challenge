import requests
url = ''
for i in range(25):
    headers = {'Authorization': 'Basic YnV0dGVyOmZseQ==' }
    myfile = requests.get("http://www.pythonchallenge.com/pc/hex/lake"+str(i+1)+".wav", headers = headers)
    open(str(i)+".wav", 'wb').write(myfile.content)
