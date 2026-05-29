# =============================================
# NOVA CALCULADORA DE IMC - VERSÃO SIMPLES
# Perfeita para VS Code
# =============================================

import tkinter as tk
from tkinter import messagebox


def calcular():
    try:
        peso = float(entry_peso.get().replace(",", "."))
        altura = float(entry_altura.get().replace(",", "."))
        
        if peso <= 0 or altura <= 0:
            messagebox.showerror("Erro", "Os valores devem ser maiores que zero!")
            return
        
        imc = round(peso / ((altura / 100) ** 2), 2)
        
        # Classificação
        if imc < 18.5:
            resultado = "Abaixo do peso"
            cor = "blue"
        elif imc < 25:
            resultado = "Peso normal"
            cor = "green"
        elif imc < 30:
            resultado = "Sobrepeso"
            cor = "orange"
        elif imc < 35:
            resultado = "Obesidade Grau I"
            cor = "red"
        elif imc < 40:
            resultado = "Obesidade Grau II"
            cor = "red"
        else:
            resultado = "Obesidade Grau III"
            cor = "darkred"
        
        # Mostra resultado
        label_resultado.config(text=f"IMC: {imc}", fg=cor)
        label_classificacao.config(text=resultado, fg=cor)
        
    except:
        messagebox.showerror("Erro", "Digite números válidos!")


# ====================== JANELA ======================

janela = tk.Tk()
janela.title("Calculadora de IMC")
janela.geometry("450x450")
janela.resizable(False, False)
janela.configure(bg="#f0f0f0")

# Título
tk.Label(janela, text="Calculadora de IMC", font=("Arial", 20, "bold"), 
         bg="#f0f0f0", fg="#333").pack(pady=20)

# Campos
tk.Label(janela, text="Peso (kg):", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
entry_peso = tk.Entry(janela, font=("Arial", 14), justify="center", width=20)
entry_peso.pack(pady=5)

tk.Label(janela, text="Altura (cm):", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
entry_altura = tk.Entry(janela, font=("Arial", 14), justify="center", width=20)
entry_altura.pack(pady=5)

# Botão
tk.Button(janela, text="CALCULAR", font=("Arial", 14, "bold"), bg="#4CAF50", 
          fg="white", height=2, width=20, command=calcular).pack(pady=20)

# Resultado
label_resultado = tk.Label(janela, text="IMC: ---", font=("Arial", 18, "bold"), 
                           bg="#f0f0f0")
label_resultado.pack(pady=10)

label_classificacao = tk.Label(janela, text="", font=("Arial", 16, "bold"), 
                               bg="#f0f0f0")
label_classificacao.pack(pady=5)

# Instrução
tk.Label(janela, text="Pressione ENTER para calcular", font=("Arial", 10), 
         fg="gray", bg="#f0f0f0").pack(pady=10)

# Atalho Enter
janela.bind("<Return>", lambda e: calcular())

janela.mainloop()