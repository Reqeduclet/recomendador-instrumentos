import streamlit as st

instrumentos = {
    "Violín": 0, "Viola": 0, "Violonchelo": 0, "Piano": 0, "Guitarra": 0,
    "Flauta travesera": 0, "Clarinete": 0, "Trompeta": 0,
    "Trombón": 0, "Tuba/Bombardino": 0, "Saxofón": 0, "Percusión clásica": 0
}

def puntuar(lista, puntos):
    for inst in lista:
        instrumentos[inst] += puntos

st.title("¿Qué instrumento musical es ideal para ti?")

# --- SECCIÓN 1: Gustos e intereses ---
r1 = st.selectbox("1. ¿Qué estilo de música te gusta más?",
                  ["Clásica", "Pop/Rock", "Jazz", "Banda/Orquesta", "Variado"])
if r1 == "Clásica":
    puntuar(["Violín", "Viola", "Violonchelo", "Piano", "Flauta travesera", "Clarinete"], 2)
elif r1 == "Pop/Rock":
    puntuar(["Guitarra", "Saxofón"], 2)
elif r1 == "Jazz":
    puntuar(["Saxofón", "Trompeta", "Trombón"], 2)
elif r1 == "Banda/Orquesta":
    puntuar(["Trompeta", "Trombón", "Tuba/Bombardino", "Clarinete", "Percusión clásica"], 2)
elif r1 == "Variado":
    puntuar(list(instrumentos.keys()), 1)

r2 = st.selectbox("2. ¿Qué papel te gustaría tener en un grupo?",
                  ["Solista", "Acompañante", "Versátil", "No lo sé"])
if r2 == "Solista":
    puntuar(["Violín", "Trompeta", "Saxofón", "Piano"], 2)
elif r2 == "Acompañante":
    puntuar(["Viola", "Guitarra", "Piano", "Tuba/Bombardino", "Clarinete"], 2)
elif r2 == "Versátil":
    puntuar(list(instrumentos.keys()), 1)

r3 = st.selectbox("3. ¿Qué te llama más la atención?",
                  ["El ritmo", "Las melodías", "Los acordes", "El timbre"])
if r3 == "El ritmo":
    puntuar(["Percusión clásica"], 2)
elif r3 == "Las melodías":
    puntuar(["Violín", "Viola", "Violonchelo", "Flauta travesera", "Clarinete", "Trompeta", "Trombón", "Saxofón"], 2)
elif r3 == "Los acordes":
    puntuar(["Piano", "Guitarra"], 2)
elif r3 == "El timbre":
    puntuar(list(instrumentos.keys()), 1)

# --- SECCIÓN 2: Edad y físico ---
r4 = st.selectbox("4. ¿Cuál es tu edad?",
                  ["6–8", "9–12", "13–17", "Adulto"])
if r4 == "6–8":
    puntuar(["Violín", "Flauta travesera", "Clarinete", "Guitarra", "Piano"], 2)
elif r4 == "9–12":
    puntuar(["Violín", "Viola", "Flauta travesera", "Clarinete", "Guitarra", "Piano", "Saxofón", "Percusión clásica"], 1)

r5 = st.selectbox("5. ¿Tienes manos o brazos especialmente pequeños o grandes?",
                  ["Muy pequeños", "Muy grandes", "Normales"])
if r5 == "Muy pequeños":
    puntuar(["Violín", "Flauta travesera", "Clarinete"], 2)
elif r5 == "Muy grandes":
    puntuar(["Trombón", "Tuba/Bombardino"], 2)

r6 = st.selectbox("6. ¿Tienes buena capacidad pulmonar?",
                  ["Sí", "No", "No lo sé"])
if r6 == "Sí":
    puntuar(["Flauta travesera", "Clarinete", "Trompeta", "Trombón", "Tuba/Bombardino", "Saxofón"], 2)
elif r6 == "No":
    puntuar(["Flauta travesera", "Clarinete", "Trompeta", "Trombón", "Tuba/Bombardino", "Saxofón"], -2)

# --- SECCIÓN 3: Práctica y condiciones ---
r7 = st.selectbox("7. ¿Puedes practicar en casa sin molestar?",
                  ["Sí", "No"])
if r7 == "No":
    puntuar(["Trompeta", "Trombón", "Tuba/Bombardino", "Percusión clásica"], -2)

r8 = st.selectbox("8. ¿Qué presupuesto inicial podrías dedicar?",
                  ["<200 €", "200–500 €", ">500 €"])
if r8 == "<200 €":
    puntuar(["Guitarra", "Flauta travesera", "Piano"], 2)
elif r8 == "200–500 €":
    puntuar(list(instrumentos.keys()), 1)
elif r8 == ">500 €":
    puntuar(list(instrumentos.keys()), 2)

r9 = st.selectbox("9. ¿Tienes posibilidad de transportar el instrumento con frecuencia?",
                  ["Sí", "No"])
if r9 == "No":
    puntuar(["Violonchelo", "Tuba/Bombardino", "Piano", "Percusión clásica"], -2)

# --- SECCIÓN 4: Personalidad ---
r10 = st.selectbox("10. ¿Cómo te defines?",
                   ["Constante y paciente", "Creativo y espontáneo", "Disciplinado y metódico", "Un poco de todo"])
if r10 == "Constante y paciente":
    puntuar(["Violín", "Viola", "Violonchelo", "Trompeta", "Trombón", "Tuba/Bombardino"], 2)
elif r10 == "Creativo y espontáneo":
    puntuar(["Guitarra", "Piano", "Saxofón"], 2)
elif r10 == "Disciplinado y metódico":
    puntuar(["Flauta travesera", "Clarinete", "Percusión clásica"], 2)
elif r10 == "Un poco de todo":
    puntuar(list(instrumentos.keys()), 1)

# --- Resultados ---
if st.button("Mostrar mis instrumentos recomendados"):
    top = sorted(instrumentos.items(), key=lambda x: x[1], reverse=True)[:3]
    st.subheader("Tus instrumentos ideales podrían ser:")
    for inst, pts in top:
        st.write(f"**{inst}** (puntuación: {pts})")
