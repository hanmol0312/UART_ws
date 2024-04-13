import serial
import time

s = serial.Serial('/dev/ttyUSB0', 2400)
st = time.time()
tts = """Finance Minister Arun Jaitley Tuesday hit out at former RBI governor Raghuram Rajan for predicting that the next banking crisis would be triggered by MSME lending, saying postmortem is easier than taking action when it was required. Rajan, who had as the chief economist at IMF warned of impending financial crisis of 2008, in a note to a parliamentary committee warned against ambitious credit targets and loan waivers, saying that they could be the sources of next banking crisis. Government should focus on sources of the next crisis, not just the last one.

In particular, government should refrain from setting ambitious credit targets or waiving loans. Credit targets are sometimes achieved by abandoning appropriate due diligence, creating the environment for future NPAs," Rajan said in the note." Both MUDRA loans as well as the Kisan Credit Card, while popular, have to be examined more closely for potential credit risk. Rajan, who was RBI governor for three years till September 2016, is currently.
$"""

for c in tts:
    s.write(c.encode())
    time.sleep(0.001)

print("Transmission done")

et = time.time()
tt = et - st
ds = len(tts.encode())
ts = ds / tt
print("Transmission speed: {:.2f} bytes/second".format(ts))

s.close()
