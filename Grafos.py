import tkinter as tk
from tkinter import Canvas, Label


class Grafo:
    def __init__(self, root):
        self.root = root
        self.root.title("Exemplo de Grafo")  # Dá nome à janela
        self.root.geometry("400x400")  # Define o tamanho inicial da janela

        # Criar um canvas para desenhar o grafo
        self.canvas = Canvas(self.root, width=400, height=400)
        self.canvas.pack()

        # Adicionar algumas vértices (usuários) para o exemplo
        self.adicionar_vertice(50, 50, "Usuário 1", "18 anos", "Python, Jogos")
        self.adicionar_vertice(150, 100, "Usuário 2",
                               "20 anos", "Jogos, Tecnologia")
        self.adicionar_vertice(250, 50, "Usuário 3",
                               "21 anos", "Tecnologia, Esportes")

        # Adiciona algumas arestas para o exemplo
        self.adicionar_aresta(50, 50, 150, 100)
        self.adicionar_aresta(150, 100, 250, 50)

    def adicionar_vertice(self, x, y, nome, idade, interesses):
        # Adiciona um círculo representando uma vértice
        self.canvas.create_oval(x-20, y-20, x+20, y+20, fill="blue")

        # Adiciona um rótulo com o nome do usuário
        nome_label = Label(self.canvas, text=nome)
        nome_label.place(x=x, y=y+30, anchor="center")

        # Informações adicionais abaixo do nome
        info_label = Label(self.canvas, text=f"Idade: {
                           idade}\nInteresses:\n{interesses}")
        info_label.place(x=x, y=y+60, anchor="center")

    def adicionar_aresta(self, x1, y1, x2, y2):
        # Adiciona uma linha representando uma aresta entre dois usuários
        self.canvas.create_line(x1, y1, x2, y2, fill="red")


if __name__ == "__main__":
    root = tk.Tk()
    app = Grafo(root)
    root.mainloop()
