# Lim95-ECDC
An encode/decode program in Python.

## How to Use
Type the text in the top box and click "encode".
If you want to decode, just paste the text into the top box and click "decode".

## How it Works
### Encoding
It first generates a number known as the NORB (the Number of Random Bytes). After that it begins the generation. It picks a seed between 0 and 255 and places it before each character. It then preforms an XOR on that seed and the character. Once it's done, it generates NORB amount of random characters to place at the end of the message. It also places the character that corresponds to the ASCII code of the NORB at the start of the file.

### Decoding
It first grabs the NORB and removes all of those pesky extra characters off the start and end. Then it uses a mod operator to choose if the current character is seed or character. Then it sets the seed or decodes using an XOR. Finally, it returns the output.
