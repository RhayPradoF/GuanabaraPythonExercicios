'''#Faça um programa em python que abra e reproduza o áudio de um arquivo em mp3.
import pygame

pygame.mixer.init()

pygame.mixer.music.load('nsyncbye (2024_09_01 10_18_47 UTC).mp3')
pygame.mixer.music.play()
x = input("Para parar a música aperte qualquer tecla do teclado! ")'''


import pygame
import tkinter as tk
from tkinter import filedialog, messagebox

def play_music():
    if file_path.get():
        pygame.mixer.music.load(file_path.get())
        pygame.mixer.music.play()
    else:
        messagebox.showwarning("Aviso", "Por favor, selecione um arquivo primeiro")

def stop_music():
    pygame.mixer.music.stop()

def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("Arquivos MP3", "*.mp3")])
    if filename:
        file_path.set(filename)

pygame.mixer.init()


root = tk.Tk()
root.title("MP3 Player")

file_path = tk.StringVar()


tk.Entry(root, textvariable=file_path, width=50).pack(pady=10)
tk.Button(root, text="Browse", command=browse_file).pack(pady=5)
tk.Button(root, text="Play", command=play_music).pack(pady=5)
tk.Button(root, text="Stop", command=stop_music).pack(pady=5)

root.mainloop()
