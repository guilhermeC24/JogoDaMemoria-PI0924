import tkinter as tk
import random

# Configurações
TAMANHO = 400
CORES = ["red", "green", "blue", "yellow", "orange", "purple"]

# Quadrado 
class Quadrado:
    def __init__(self, canvas, x, y, tamanho, cor):
        self.canvas = canvas
        self.cor = cor
        self.retangulo = canvas.create_rectangle(x, y, x+tamanho, y+tamanho, fill="white", outline="black")
        self.ativo = False