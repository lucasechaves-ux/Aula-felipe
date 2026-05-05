import tkinter as tk
import datetime
import random

# ===== FUNÇÃO PRINCIPAL DO APP =====
def executar():
    nome = entry_nome.get().capitalize()
    turma = entry_turma.get().upper()
    chamada = entry_chamada.get()

    agora = datetime.datetime.now()

    tecnologias = ["Python", "GitHub"]

    mensagens = [
        "Continue aprendendo! 💪",
        "Cada linha de código importa! 🚀",
        "Você está evoluindo! ✨",
        "GitHub é seu portfólio! 📁",
        "Python é só o começo! 🐍"
    ]

    numero_sorte = random.randint(1, 100)

    resultado = f"""
🐍 MEU PRIMEIRO APP PYTHON

👋 Olá, Mundo!
Bem-vindo ao GitHub!

👤 Sobre mim:
Nome: {nome}
Turma: {turma}
numero: N°{chamada}

⏰ Data e hora:
{agora.strftime('%d/%m/%Y às %H:%M:%S')}

🧮 Calculadora básica:
10 + 3 = {10 + 3}
10 - 3 = {10 - 3}
10 × 3 = {10 * 3}
10 ÷ 3 = {10 / 3:.2f}

💻 Tecnologias:
"""

    for i, tech in enumerate(tecnologias, 1):
        resultado += f"{i}. {tech}\n"

    resultado += f"""
🍀 Número da sorte: {numero_sorte}

💡 Mensagem do dia:
{random.choice(mensagens)}
"""

    text_resultado.delete("1.0", tk.END)
    text_resultado.insert(tk.END, resultado)

# ===== JANELA PRINCIPAL =====
janela = tk.Tk()
janela.title("Meu Primeiro App Python")
janela.geometry("600x600")
janela.configure(bg="#1e1e2f")

# ===== TÍTULO =====
titulo = tk.Label(
    janela,
    text="🐍 Meu Primeiro App Python",
    font=("Arial", 16, "bold"),
    fg="white",
    bg="#1e1e2f"
)
titulo.pack(pady=10)

# ===== INPUTS =====
frame = tk.Frame(janela, bg="#1e1e2f")
frame.pack(pady=10)

tk.Label(frame, text="Nome:", fg="white", bg="#1e1e2f").grid(row=0, column=0)
entry_nome = tk.Entry(frame)
entry_nome.grid(row=0, column=1)

tk.Label(frame, text="Turma:", fg="white", bg="#1e1e2f").grid(row=1, column=0)
entry_turma = tk.Entry(frame)
entry_turma.grid(row=1, column=1)

tk.Label(frame, text="Numero:", fg="white", bg="#1e1e2f").grid(row=2, column=0)
entry_chamada = tk.Entry(frame)
entry_chamada.grid(row=2, column=1)

# ===== BOTÃO =====
botao = tk.Button(
    janela,
    text="Executar Programa 🚀",
    command=executar,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 12, "bold")
)
botao.pack(pady=10)

# ===== ÁREA DE RESULTADO =====
text_resultado = tk.Text(janela, height=20, width=70)
text_resultado.pack(pady=10)

# ===== LOOP DO APP =====
janela.mainloop()