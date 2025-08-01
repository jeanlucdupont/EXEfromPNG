# EXEfromPNG – Payload steganography in PNG

This is a proof-of-concept that demonstrates how a Windows executable can be embedded inside a PNG image using simple steganography.

## How it works

1. An EXE is base64-encoded and appended to a valid PNG file.
2. The resulting image still displays as expected.
3. A small Python “downloader” fetches the image, extracts the embedded EXE, writes it to disk, and executes it.

##  Limitations

- This isn’t bulletproof stegano. Mo encryption or obfuscation.
- It's a PoC, not an attack framework.

##  Disclaimer

This is for educational purposes only. Don’t be a jerk.

##  The long horn
Photo by linzmeier1
https://pixabay.com/photos/longhorn-cattle-steer-texas-3394286/


<img width="1094" height="874" alt="image" src="https://github.com/user-attachments/assets/a7ee08e5-0fed-4e9f-8a6b-596d76e6daf2" />

