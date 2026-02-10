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
                       
        self.sequencia = []
        self.sequencia_jogador = []
        self.nivel = 1
        self.mostrar_sequencia = True

        self.label = tk.Label(root, text="Nível: 1", font=("Arial", 16))
        self.label.pack()

        self.canvas.bind("<Button-1>", self.ao_clicar)
        self.root.after(1000, self.jogar_nivel)

    def jogar_nivel(self):
        if self.mostrar_sequencia:
            self.sequencia.append(random.randint(0, len(self.quadrados)-1))
            self.label.config(text=f"Nível: {self.nivel}")
            self.mostrar_sequencia = False
            self.sequencia_jogador = []
            self.mostrar_sequencia_cpu()
                     
    def mostrar_sequencia_cpu(self):
        for idx in self.sequencia:
            self.quadrados[idx].pressionar()
            self.root.update()
            self.root.after(500)
            self.quadrados[idx].despressionar()
            self.root.update()
            self.root.after(300)