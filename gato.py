#from funcionesgato  import * #funciones y reglas del juego
import tkinter as tk
from tkinter import messagebox
import random

class Gato:
    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Gato")
        #Los botones son colocados de manera que se lean de izquierda a derecha y de arriba a abajo
        self.jugador = "X"
        self.tablero = [[" " for _ in range(3)] for _ in range(3)]
        self.botones = [[None for _ in range(3)] for _ in range(3)]

        for i in range (3):
            for j in range (3):
                self.botones[i][j] = tk.Button(self.ventana, text = " ", font = "consolas 30", width=10
                                                    , height=5, command = lambda fila = i, col = j: self.Seleccionar(fila, col))
                self.botones[i][j].grid(row=i, column=j)
    
    def SeleccionarCompu(self):
        disponible = []
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == " ":
                    disponible.append((i, j))
        if disponible:
            fila, col = random.choice(disponible)
            self.tablero[fila][col] = self.jugador
            self.botones[fila][col]["text"] = self.jugador
            self.botones[fila][col]["state"] = "disabled"
            if self.condicionVictoria():
                messagebox.showinfo("Ganador", f"El jugador {self.jugador} gana")
            elif self.condicionEmpate():
                messagebox.showinfo("Empate", "Empate")

    def Seleccionar(self, fila, col):
        if self.tablero[fila][col] == " ":
            self.tablero[fila][col] = self.jugador
            self.botones[fila][col]["text"] = self.jugador
            self.botones[fila][col]["state"] = "disabled"
        if self.condicionVictoria():
            messagebox.showinfo("Ganador", f"El jugador {self.jugador} gana")
        elif self.condicionEmpate():
            messagebox.showinfo("Empate", "Empate")
        else:
            self.cambiarJugador()
            self.SeleccionarCompu()
            self.cambiarJugador()
    
    def condicionVictoria(self):
        # Verificar líneas horizontales
        for fila in self.tablero:
            if fila[0] == fila[1] == fila[2] != " ":
                return True
        
        # Verificar líneas verticales
        for col in range(3):
            if self.tablero[0][col] == self.tablero[1][col] == self.tablero[2][col] != " ":
                return True

        # Verificar diagonales
        if (self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != " " or
        self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != " "):
            return True

        # Si no se cumple ninguna condición de victoria
        return False
    
    def condicionEmpate(self):
        for fila in self.tablero:
            if " " in fila:
                return False
        return True
    
    def cambiarJugador(self):
        if self.jugador == "X":
            self.jugador = "O"
        else:
            self.jugador = "X"

    def run(self):
        self.ventana.mainloop()
        
if __name__ == "__main__":
    juego = Gato()
    juego.run()
