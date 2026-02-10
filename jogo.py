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
        
    def pressionar(self):
        self.canvas.itemconfig(self.retangulo, fill=self.cor)
        self.ativo = True

    def despressionar(self):
        self.canvas.itemconfig(self.retangulo, fill="white")
        self.ativo = False

    def foi_clicado(self, evento):
        x, y = evento.x, evento.y
        coords = self.canvas.coords(self.retangulo)
        return coords[0] <= x <= coords[2] and coords[1] <= y <= coords[3]