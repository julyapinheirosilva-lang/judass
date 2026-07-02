# =============================================
# NOVA CALCULADORA DE IMC - VERSÃO SIMPLES
# Perfeita para VS Code
# =============================================

# Importa os módulos necessários do Tkinter para criar a interface gráfica
import tkinter as tk
from tkinter import messagebox


def calcular():
    """
    Função principal que calcula o IMC com base nos valores inseridos.
    Trata erros de entrada e exibe o resultado com classificação e cor correspondente.
    """
    try:
        # Obtém os valores dos campos de entrada e converte vírgula para ponto (suporte a formato brasileiro)
        peso = float(entry_peso.get().replace(",", "."))
        altura = float(entry_altura.get().replace(",", "."))
        
        # Validação: valores devem ser positivos
        if peso <= 0 or altura <= 0:
            messagebox.showerror("Erro", "Os valores devem ser maiores que zero!")
            return
        
        # Cálculo do IMC: peso / (altura em metros)^2
        imc = round(peso / ((altura / 100) ** 2), 2)
        
        # Classificação do IMC conforme padrões da OMS
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
        
        # Atualiza os labels com o resultado e a cor correspondente
        label_resultado.config(text=f"IMC: {imc}", fg=cor)
        label_classificacao.config(text=resultado, fg=cor)
        
    except:
        # Captura erros de conversão (ex: letras em vez de números)
        messagebox.showerror("Erro", "Digite números válidos!")


# ====================== CRIAÇÃO DA JANELA PRINCIPAL ======================

# Inicializa a janela principal da aplicação Tkinter
janela = tk.Tk()
janela.title("Calculadora de IMC")
janela.geometry("450x450")  # Tamanho fixo da janela
janela.resizable(False, False)  # Impede redimensionamento
janela.configure(bg="#f0f0f0")  # Cor de fundo cinza claro

# Título principal da aplicação
tk.Label(janela, text="Calculadora de IMC", font=("Arial", 20, "bold"), 
         bg="#f0f0f0", fg="#333").pack(pady=20)

# Campos de entrada
# Label e Entry para Peso
tk.Label(janela, text="Peso (kg):", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
entry_peso = tk.Entry(janela, font=("Arial", 14), justify="center", width=20)
entry_peso.pack(pady=5)

# Label e Entry para Altura
tk.Label(janela, text="Altura (cm):", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
entry_altura = tk.Entry(janela, font=("Arial", 14), justify="center", width=20)
entry_altura.pack(pady=5)

# Botão principal para calcular
tk.Button(janela, text="CALCULAR", font=("Arial", 14, "bold"), bg="#4CAF50", 
          fg="white", height=2, width=20, command=calcular).pack(pady=20)

# Labels para exibir o resultado
# Label para o valor numérico do IMC
label_resultado = tk.Label(janela, text="IMC: ---", font=("Arial", 18, "bold"), 
                           bg="#f0f0f0")
label_resultado.pack(pady=10)

# Label para a classificação (ex: "Peso normal")
label_classificacao = tk.Label(janela, text="", font=("Arial", 16, "bold"), 
                               bg="#f0f0f0")
label_classificacao.pack(pady=5)

# Instrução para o usuário
tk.Label(janela, text="Pressione ENTER para calcular", font=("Arial", 10), 
         fg="gray", bg="#f0f0f0").pack(pady=10)

# Atalho de teclado: permite calcular pressionando ENTER
janela.bind("<Return>", lambda e: calcular())

# Inicia o loop principal da interface gráfica
janela.mainloop()