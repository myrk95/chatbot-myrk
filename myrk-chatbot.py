import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage

# ---------------------------
# ESTILO DE FONDO PRINCIPAL
# ---------------------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom, #A2DFF7, #66C2E0); /* degradado azul Mediterráneo */
        color: #000000;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------
# CONFIGURACIÓN DE PÁGINA
# ---------------------------
st.set_page_config(page_title="Chatbot Myrk")
st.title("Chatbot Myrk")
st.markdown("Holi , soy Myrk, tu asistente virtual")

# ---------------------------
# INICIALIZAR HISTORIALES
# ---------------------------
if "conversaciones" not in st.session_state:
    st.session_state.conversaciones = [[]]  # Lista de conversaciones
if "conversacion_activa" not in st.session_state:
    st.session_state.conversacion_activa = 0  # Índice de la conversación actual

# ---------------------------
# MENÚ LATERAL
# ---------------------------
with st.sidebar:
    st.header("Configuración del modelo")
    temperatura = st.slider("Temperatura", 0.0, 1.5, 0.7, 0.1)
    modelo = st.selectbox(
        "Modelo",
        ["gemini-2.5-flash", "gemini-1.5-flash"],
        index=0
    )
    st.header("Utilidad")
    # Botones de gestión de conversaciones
    if st.button("Nueva conversación"):
        st.session_state.conversaciones.append([])
        st.session_state.conversacion_activa = len(st.session_state.conversaciones) - 1

    if st.button("Eliminar conversación"):
        if st.session_state.conversaciones:
            st.session_state.conversaciones.pop(st.session_state.conversacion_activa)
            if len(st.session_state.conversaciones) == 0:
                st.session_state.conversaciones = [[]]
            st.session_state.conversacion_activa = min(st.session_state.conversacion_activa, len(st.session_state.conversaciones) - 1)

    if st.button("Limpiar conversación actual"):
        st.session_state.conversaciones[st.session_state.conversacion_activa] = []

    # Selector de conversaciones previas
    st.header("Conversaciones previas")
    if st.session_state.conversaciones:
        conv_index = st.radio(
            "Selecciona conversación",
            options=list(range(len(st.session_state.conversaciones))),
            format_func=lambda i: f"Conversación {i+1}",
            index=st.session_state.conversacion_activa
        )
        st.session_state.conversacion_activa = conv_index

    # Historial coloreado de la conversación activa
    st.header("📜 Historial de conversación")
    for msg in st.session_state.conversaciones[st.session_state.conversacion_activa]:
        if isinstance(msg, HumanMessage):
            st.markdown(
                f"<div style='background-color:#A7D8DE; padding:8px; border-radius:10px; margin-bottom:5px;'>"
                f"**Tú:** {msg.content}</div>", unsafe_allow_html=True)
        else:
            st.markdown(
                f"<div style='background-color:#F4E1C1; padding:8px; border-radius:10px; margin-bottom:5px;'>"
                f"**Asistente:** {msg.content}</div>", unsafe_allow_html=True)

# ---------------------------
# CREAR INSTANCIA DEL MODELO
# ---------------------------
chat_model = ChatGoogleGenerativeAI(
    model=modelo,
    temperature=temperatura
)

# ---------------------------
# INPUT DEL USUARIO
# ---------------------------
pregunta = st.chat_input("Escribe tu mensaje:")

if pregunta:
    # Guardar mensaje del usuario
    st.session_state.conversaciones[st.session_state.conversacion_activa].append(HumanMessage(content=pregunta))
    with st.chat_message("user"):
        st.markdown(f"<div style='background-color:#A7D8DE; padding:8px; border-radius:10px;'>{pregunta}</div>", unsafe_allow_html=True)

    # Convertir historial a formato Gemini
    historial_formateado = [
        {"role": "user", "content": m.content} if isinstance(m, HumanMessage)
        else {"role": "assistant", "content": m.content}
        for m in st.session_state.conversaciones[st.session_state.conversacion_activa]
    ]

    # Obtener respuesta
    respuesta = chat_model.invoke(historial_formateado)

    # Mostrar respuesta
    with st.chat_message("assistant"):
        st.markdown(f"<div style='background-color:#F4E1C1; padding:8px; border-radius:10px;'>{respuesta.content}</div>", unsafe_allow_html=True)

    # Guardar respuesta
    st.session_state.conversaciones[st.session_state.conversacion_activa].append(AIMessage(content=respuesta.content))
