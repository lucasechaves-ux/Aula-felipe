import streamlit as st
import datetime
import random
from zoneinfo import ZoneInfo

st.set_page_config(page_title="Meu Primeiro App Python", page_icon="🐍", layout="centered")

# ===== TÍTULO =====
st.title("🐍 Meu Primeiro App Python")
st.write("Bem-vindo ao GitHub!")

# ===== INPUTS =====
nome = st.text_input("Digite seu nome:")
turma = st.text_input("Digite sua turma:")
chamada = st.text_input("Digite seu número:")

# ===== BOTÃO =====
if st.button("Executar Programa 🚀"):

    agora = datetime.datetime.now(ZoneInfo('America/Sao_Paulo'))

    tecnologias = ["Python", "GitHub"]

    mensagens = [
        "Continue aprendendo! 💪",
        "Cada linha de código importa! 🚀",
        "Você está evoluindo! ✨",
        "GitHub é seu portfólio! 📁",
        "Python é só o começo! 🐍"
    ]

    numero_sorte = random.randint(1, 100)

    st.subheader("🐍 Resultado")

    st.write(f"👤 Nome: {nome.capitalize()}")
    st.write(f"🏫 Turma: {turma.upper()}")
    st.write(f"🔢 Número: N°{chamada}")

    st.write(f"⏰ Data e hora: {agora.strftime('%d/%m/%Y às %H:%M:%S')}")

    st.write("🧮 Calculadora básica:")
    st.write(f"10 + 3 = {10 + 3}")
    st.write(f"10 - 3 = {10 - 3}")
    st.write(f"10 × 3 = {10 * 3}")
    st.write(f"10 ÷ 3 = {10 / 3:.2f}")

    st.write("💻 Tecnologias:")
    for i, tech in enumerate(tecnologias, 1):
        st.write(f"{i}. {tech}")

    st.write(f"🍀 Número da sorte: {numero_sorte}")

    st.success(random.choice(mensagens))
