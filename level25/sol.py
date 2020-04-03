import requests
import audiosegment
import functools 
from pydub.playback import play

#for i in range(25):
#    headers = {'Authorization': 'Basic YnV0dGVyOmZseQ==' }
#    myfile = requests.get("http://www.pythonchallenge.com/pc/hex/lake"+str(i+1)+".wav", headers = headers)
#    open(str(i)+".wav", 'wb').write(myfile.content)

#f1 = audiosegment.from_file("0.wav")
#f2 = audiosegment.from_file("1.wav")
#f3 = audiosegment.from_file("5.wav")

combined =[]
for x in range(5):
    waves = [audiosegment.from_file(str((x*5)+ y)+".wav") for y in range(5)]
    waves = [f.set_frame_rate(44.1) for f in waves]
    wave = functools.reduce(lambda a,b: a.overlay(b),waves)
    combined.append(wave)

#solution = functools.reduce(lambda a,b: a.append(b), combined)
#solution.export("solution.wav", format="wav")
for x in range(5):
    combined[x].export("new"+str(x)+".wav", format="wav")

#wave = functools.reduce(lambda a,b: a.overlay(b),combined)
#wave.export("all.wav",format = "wav")
