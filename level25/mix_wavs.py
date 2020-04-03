import wave
import numpy as np

from pydub import AudioSegment
from pydub.playback import play

# sound1 = AudioSegment.from_file("7.wav")
# sound2 = AudioSegment.from_file("12.wav")
# sound3 = AudioSegment.from_file("13.wav")
# sound4 = AudioSegment.from_file("11.wav")
# sound5 = AudioSegment.from_file("17.wav")
#
# output = sound1.overlay(sound2, position=0)
# output = output.overlay(sound3, position=0)
# output = output.overlay(sound4, position=0)
# output = output.overlay(sound5, position=0)
#
# # save the result
# output.export("mixed_sounds.wav", format="wav")
def grouplen(sequence, chunk_size):
    return list(zip(*[iter(sequence)] * chunk_size))

wavs_num = 25
frame_num = 10800
wav_list, wav_read_list = list(), list()
img = np.zeros((300,300,3),dtype=np.uint8)
for idx in range(wavs_num):
    row = int(idx/5)*60
    col = (idx % 5)*60
    wav_list.append(wave.open('{0}.wav'.format(idx), 'rb'))
    wav_read_list.append(wav_list[idx].readframes(frame_num))
    group3 = grouplen(wav_read_list[idx], 3)
    for rgb in group3:
        img[row][col] = rgb
        col+=1
        if(col%60 == 0):
            col-=60
            row+=1
import cv2
cv2.imshow("foo",img)
cv2.waitKey(0)
