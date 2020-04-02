import urllib.request
#offset= 2123456788
#aoffset=2123456744
offset=1152983631
i=100
while True:
    headers = {'Authorization': 'Basic YnV0dGVyOmZseQ==', 'Range': 'bytes='+str(offset)+'-', 'Transfer-Encoding': 'chunked'}
    req = urllib.request.Request('http://www.pythonchallenge.com/pc/hex/unreal.jpg',headers = headers)
    #req = urllib.request.Request('http://www.pythonchallenge.com/pc/hex/invader.html',headers = headers)
    res = urllib.request.urlopen(req)
    print(type(res))
    f = open("/Users/amitm/dev/personal/python-challange/level20/solution"+str(i)+".txt",'wb')
    response = res.read()
    print(res.getheaders())
    offset= offset - f.write(response)
    i+=1
    print(len((response)))
    #print(offset+1)
    #offset+=1

