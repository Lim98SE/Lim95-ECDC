from random import randint as rand

import tkinter as tk

global string
global encoded
global decoded

def encode():
    text=input_text.get("1.0",tk.END)
    output=""
    random_bytes=rand(0,1024)
    output+=chr(random_bytes)
    for i in text:
        seed=rand(0,255)
        output+=chr(seed)
        output+=chr(ord(i)^seed)
    for i in range(random_bytes):
        output+=chr(rand(0,255))
    output_text.delete("1.0",tk.END)
    output_text.insert("1.0",output)
    
def decode():
    text=input_text.get("1.0",tk.END)
    output=""
    random_bytes=ord(text[0])
    text=text[1:len(text)-random_bytes]
    for i in range(len(text)):
        temp=i%2
        if temp==0:
            seed=ord(text[i])
        elif temp==1:
            output+=chr(ord(text[i])^seed)
    output_text.delete("1.0",tk.END)
    output_text.insert("1.0",output)

global input_text
global output_text
window = tk.Tk()
window.title("Lim95 ECDC")
window.geometry("600x900")
encode_button = tk.Button(text="Encode",command=encode)
decode_button = tk.Button(text="Decode",command=decode)
input_text = tk.Text()
output_text = tk.Text()
decoded_text = tk.Text()
input_text.pack()
output_text.pack()
encode_button.pack()
decode_button.pack()


