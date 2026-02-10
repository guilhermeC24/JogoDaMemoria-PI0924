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
       
# Jogo
class JogoDaMemoria:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=TAMANHO, height=TAMANHO+50, bg="white")
        self.canvas.pack()

        # Criar quadrados
        self.quadrados = []
        tamanho = 100
        for i in range(2):
            for j in range(3):
                cor = CORES[i*3 + j]
                q = Quadrado(self.canvas, 50 + j*tamanho, 50 + i*tamanho, tamanho, cor)
                self.quadrados.append(q)