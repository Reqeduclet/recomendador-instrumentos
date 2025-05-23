import streamlit as st

preguntas = [
    {
        "texto": "¿Qué estilo de música te gusta más?",
        "opciones": {
            "Clásica": ["Violín", "Viola", "Violonchelo", "Piano", "Flauta travesera", "Clarinete"],
            "Pop/Rock": ["Guitarra", "Saxofón"],
            "Jazz": ["Saxofón", "Trompeta", "Trombón"],
            "Banda/Orquesta": ["Trompeta", "Trombón", "Tuba/Bombardino", "Clarinete", "Percusión clásica"],
            "Variado": "todos"
        }
    },
    {
        "texto": "¿Qué papel te gustaría tener en un grupo?",
        "opciones": {
            "Solista": ["Violín", "Trompeta", "Saxofón", "Piano"],
            "Acompañante": ["Viola", "Guitarra", "Piano", "Tuba/Bombardino", "Clarinete"],
            "Versátil": "todos"
        }
    },
    {
        "texto": "¿Qué te llama más la atención?",
        "opciones": {
            "El ritmo": ["Percusión clásica"],
            "Las melodías": ["Violín", "Viola", "Violonchelo", "Flauta travesera", "Clarinete", "Trompeta", "Trombón", "Saxofón"],
            "Los acordes": ["Piano", "Guitarra"],
            "El timbre": "todos"
        }
    },
    {
        "texto": "¿Cuál es tu edad?",
        "opciones": {
            "6–8": ["Violín", "Flauta travesera", "Clarinete", "Guitarra", "Piano"],
            "9–12": ["Violín", "Viola", "Flauta travesera", "Clarinete", "Guitarra", "Piano", "Saxofón", "Percusión clásica"],
            "13–17": [],
            "Adulto": []
        }
    },
    {
        "texto": "¿Puedes practicar en casa sin molestar?",
        "opciones": {
            "Sí": [],
            "No": ["Trompeta", "Trombón", "Tuba/Bombardino", "Percusión clásica"]
        },
        "penaliza": True
    },
    {
        "texto": "¿Qué presupuesto inicial podrías dedicar?",
        "opciones": {
            "<200 €": ["Guitarra", "Flauta travesera", "Piano"],
            "200–500 €": "todos",
            ">500 €": "todos"
        }
    },
    {
        "texto": "¿Tienes posibilidad de transportar el instrumento con frecuencia?",
        "opciones": {
            "Sí": [],
            "No": ["Violonchelo", "Tuba/Bombardino", "Piano", "Percusión clásica"]
        },
        "penaliza": True
    },
    {
        "texto": "¿Cómo te defines?",
        "opciones": {
            "Constante y paciente": ["Violín", "Viola", "Violonchelo", "Trompeta", "Trombón", "Tuba/Bombardino"],
            "Creativo y espontáneo": ["Guitarra", "Piano", "Saxofón"],
            "Disciplinado y metódico": ["Flauta travesera", "Clarinete", "Percusión clásica"],
            "Un poco de todo": "todos"
        }
    }
]

instrumentos = {
    "Violín": 0, "Viola": 0, "Violonchelo": 0, "Piano": 0, "Guitarra": 0,
    "Flauta travesera": 0, "Clarinete": 0, "Trompeta": 0,
    "Trombón": 0, "Tuba/Bombardino": 0, "Saxofón": 0, "Percusión clásica": 0
}

imagenes = {
    "Violín": "https://upload.wikimedia.org/wikipedia/commons/1/1b/Violin_VL100.png",
    "Viola": "https://upload.wikimedia.org/wikipedia/commons/6/66/Bratsche.jpg",
    "Violonchelo": "https://upload.wikimedia.org/wikipedia/commons/0/00/Cello_front_side.png",
    "Piano": "https://upload.wikimedia.org/wikipedia/commons/6/6b/Grand_piano_1.png",
    "Guitarra": "https://upload.wikimedia.org/wikipedia/commons/4/45/GuitareClassique5.png",
    "Flauta travesera": "https://upload.wikimedia.org/wikipedia/commons/2/28/Western_concert_flute_%28Yamaha%29.jpg",
    "Clarinete": "https://upload.wikimedia.org/wikipedia/commons/5/5f/Clarinet_bflat.png",
    "Trompeta": "https://upload.wikimedia.org/wikipedia/commons/c/c4/Trumpet_1.png",
    "Trombón": "https://upload.wikimedia.org/wikipedia/commons/5/55/Trombone.png",
    "Tuba/Bombardino": "https://upload.wikimedia.org/wikipedia/commons/b/b7/Tuba-byNeovitaha.jpg",
    "Saxofón": "https://upload.wikimedia.org/wikipedia/commons/e/e6/Alto_Saxophone_EFlat.jpg",
    "Percusión clásica": "https://upload.wikimedia.org/wikipedia/commons/b/b2/Timpani.jpg"
}

st.title("¿Qué instrumento musical es ideal para ti?")

if "paso" not in st.session_state:
    st.session_state.paso = 0
if "respuestas" not in st.session_state:
    st.session_state.respuestas = []

paso = st.session_state.paso

if paso < len(preguntas):
    pregunta = preguntas[paso]
    respuesta = st.radio(pregunta["texto"], list(pregunta["opciones"].keys()))
    if st.button("Siguiente"):
        st.session_state.respuestas.append(respuesta)
        st.session_state.paso += 1
        st.experimental_rerun()
else:
    for i, resp in enumerate(st.session_state.respuestas):
        entrada = preguntas[i]
        opcion = entrada["opciones"][resp]
        penaliza = entrada.get("penaliza", False)
        puntos = -2 if penaliza else 2
        if opcion == "todos":
            for inst in instrumentos:
                instrumentos[inst] += 1
        else:
            for inst in opcion:
                instrumentos[inst] += puntos

    top3 = sorted(instrumentos.items(), key=lambda x: x[1], reverse=True)[:3]
    st.subheader("Tus instrumentos ideales podrían ser:")
    for inst, pts in top3:
        st.markdown(f"### {inst}")
        st.image(imagenes[inst], width=300)
        st.write(f"Puntuación: {pts}")
    st.button("Volver a empezar", on_click=lambda: [st.session_state.clear(), st.experimental_rerun()])
