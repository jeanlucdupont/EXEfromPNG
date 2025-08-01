import sys
import numpy as np
from PIL import Image

def f_bitstream(data_bytes):
    return ''.join(f"{byte:08b}" for byte in data_bytes)

if len(sys.argv) != 4:
    print(f"Usage: python {sys.argv[0]} input.png payload.exe output.png")
    sys.exit(1)

with open(sys.argv[2], 'rb') as f:
    exedata     = f.read()

exebit          = f_bitstream(len(exedata).to_bytes(4, 'big') + exedata)  
pixels          = np.array(Image.open(sys.argv[1]))
h, w, bogus     = pixels.shape
if len(exebit) > h * w * 3:
    print("Picture is too small.")
    sys.exit(1)

rgbpixels       = pixels.reshape(-1, 3)
j               = 0
for i in range(len(rgbpixels)):
    for k in range(3):                            # RGB
        if j < len(exebit):
            rgbpixels[i][k] &= 0b11111110         # Remove LSB
            rgbpixels[i][k] |= int(exebit[j])     # Add LSB
            j += 1
        else:
            break
    if j >= len(exebit):
        break

stego           = rgbpixels.reshape((h, w, 3))
stegoimg        = Image.fromarray(stego.astype('uint8'))
stegoimg.save(sys.argv[3])

