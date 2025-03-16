import tkinter as tk
import random
import spacy

# Cargar modelo de español de spaCy
nlp = spacy.load("es_core_news_sm")

# Nombre del chatbot
nombre_bot = "VetMickey"

# Mensaje de bienvenida con opciones
saludo = (
    "¡Oh, hola amigo! 😊 Soy VetMickey, tu asistente veterinario. ¡Qué alegría verte! 🎉 Pregunta sobre: \n"
    "🐶 *Vacunas* \n"
    "🐱 *Alimentación* \n"
    "🐾 *Enfermedades* \n"
    "🐾 *Desparasitación* \n"
    "🗓️ *Agendar cita* \n\n"
    "¡Ja ja! ¡Dime en qué puedo ayudarte! 🎙️"
)

# Respuestas variadas para cada tema
respuestas = {
    "vacunas": [
        "¡Ja ja! Oh, las vacunas son súper importantes. 🩺 ¿Cuándo fue la última de tu mascota?",
        "¡Oh, amigo! 🏥 La vacunación protege a tu mascota. ¿Necesitas ayuda con el calendario de vacunas?",
        "¡Guau! 🐶 Es clave vacunarlos a tiempo. ¿Quieres saber qué vacunas necesita?"
    ],
    "alimentación": [
        "¡Yupi! 🥩🐾 Una buena alimentación es clave. ¿Quieres recomendaciones según su edad?",
        "¡Oh, qué interesante! 🥕 Los perritos deben comer balanceado. ¿Sabes qué alimentos evitar?",
        "¡Mmm! 🍖 Los gatos y perros tienen necesidades distintas. ¿Sobre qué mascota quieres saber?"
    ],
    "enfermedades": [
        "¡Oh, cielos! 😲 Si tu mascota está enferma, es mejor llevarla al veterinario. ¿Tiene síntomas específicos?",
        "¡Vaya, amigo! 😢 La salud es lo primero. ¿Cómo se siente tu mascota?",
        "¡Oh, no! 🏥 Es importante actuar rápido. ¿Quieres saber signos de alerta?"
    ],
    "desparasitación": [
        "¡Guau! 🦠 Es clave desparasitarlos cada 3 meses. ¿Quieres saber qué productos usar?",
        "¡Qué locura! 🕷️ Los parásitos pueden afectar su salud. ¿Ya hiciste su última desparasitación?",
        "¡Oh, amigo! 🦟 Hay desparasitantes internos y externos. ¿Cuál te interesa más?"
    ],
    "cita": [
        "¡Fantástico! 🎉 ¿Qué día y hora te gustaría agendar?",
        "¡Oh, qué emoción! 🗓️ Puedo ayudarte con tu cita. ¿Prefieres en la mañana o en la tarde?",
        "¡Genial! 📅 Dime cuándo te gustaría y te confirmo la disponibilidad."
    ]
}

def entender_mensaje(mensaje):
    """Procesa el mensaje con spaCy y determina el tema"""
    doc = nlp(mensaje.lower())
    for token in doc:
        if token.lemma_ in ["vacuna", "vacunas", "vacunar"]:
            return "vacunas"
        if token.lemma_ in ["comida", "alimentación", "dieta", "alimentar"]:
            return "alimentación"
        if token.lemma_ in ["enfermedad", "síntoma", "problema", "malestar"]:
            return "enfermedades"
        if token.lemma_ in ["desparasitación", "parásito", "gusanos"]:
            return "desparasitación"
        if token.lemma_ in ["cita", "agendar", "turno", "consulta"]:
            return "cita"
    return None

def obtener_respuesta(mensaje):
    """Obtiene una respuesta basada en la comprensión del mensaje"""
    tema = entender_mensaje(mensaje)
    if tema:
        return random.choice(respuestas[tema]) + " ¡Entendido, amigo! 🎉"
    return "¡Oh cielos! No entiendo eso, amigo. 🎙️ ¿Puedes preguntarlo de otra forma? ¡Ja ja! 😅 ¿Tal vez quieras saber sobre vacunas, alimentación o agendar una cita?"

def enviar_mensaje():
    """Maneja la interacción del usuario con el chatbot"""
    mensaje_usuario = entrada_texto.get()
    if mensaje_usuario:
        respuesta_bot = obtener_respuesta(mensaje_usuario)
        historial_texto.insert(tk.END, "Tú: " + mensaje_usuario + "\n", "usuario")
        historial_texto.insert(tk.END, nombre_bot + ": " + respuesta_bot + "\n", "bot")
        entrada_texto.delete(0, tk.END)

# Crear la ventana de chat con Tkinter
ventana = tk.Tk()
ventana.title("VetMickey - Asistente Veterinario")

# Crear historial de chat
historial_texto = tk.Text(ventana, height=20, width=50)
historial_texto.tag_config("usuario", foreground="blue")
historial_texto.tag_config("bot", foreground="red")  # Rojo como la ropa de Mickey
historial_texto.pack()

# Mostrar el mensaje de bienvenida
historial_texto.insert(tk.END, nombre_bot + ": " + saludo + "\n", "bot")

# Crear campo de entrada y botón de enviar
entrada_texto = tk.Entry(ventana, width=50)
entrada_texto.pack()

boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_mensaje)
boton_enviar.pack()

ventana.mainloop()
