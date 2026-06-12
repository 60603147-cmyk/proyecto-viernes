import turtle
import time

# ==========================================
# 1. CONFIGURACIÓN DE LA PANTALLA
# ==========================================
ventana = turtle.Screen()
ventana.bgcolor("#f0fdf4")  # Fondo verde claro
ventana.title("Flor Animada en Python")
ventana.setup(width=600, height=600)
ventana.tracer(0)  # Desactiva la animación automática para controlar los fotogramas manualmente

# Crear el objeto que dibujará la flor
flor = turtle.Turtle()
flor.hideturtle()  # Esconde la flecha del cursor
flor.speed(0)       # Máxima velocidad de procesamiento

# ==========================================
# 2. FUNCIONES DE DIBUJO
# ==========================================
def dibujar_petalo(t, radio):
    """Dibuja un pétalo usando dos arcos de círculo."""
    for _ in range(2):
        t.circle(radio, 90)
        t.left(90)

def dibujar_escena(t, rotacion):
    """Dibuja toda la flor con un ángulo de rotación específico."""
    t.clear()  # Borra el fotograma anterior
    
    # Dibujar el tallo
    t.penup()
    t.goto(0, -250)
    t.setheading(90)
    t.pendown()
    t.color("#15803d")  # Verde oscuro
    t.pensize(6)
    t.forward(250)
    
    # Dibujar los 8 pétalos rotados
    t.pensize(2)
    for i in range(8):
        t.penup()
        t.goto(0, 0)  # Centro de la flor
        t.pendown()
        t.color("#ff4081", "#ff6496")  # Borde y relleno rosa
        t.begin_fill()
        # Sumamos la 'rotacion' actual para que los pétalos giren en cada fotograma
        t.setheading(i * 45 + rotacion)
        dibujar_petalo(t, 80)
        t.end_fill()
        
    # Dibujar el centro amarillo de la flor
    t.penup()
    t.goto(0, -25)  # Bajamos un poco para centrar el círculo en el origen (0,0)
    t.setheading(0)
    t.color("#f59e0b", "#fcd34d")  # Borde y relleno amarillo
    t.pendown()
    t.begin_fill()
    t.circle(25)
    t.end_fill()

# ==========================================
# 3. BUCLE PRINCIPAL DE LA ANIMACIÓN
# ==========================================
angulo_actual = 0

try:
    while True:
        dibujar_escena(flor, angulo_actual)
        ventana.update()  # Refresca la pantalla con el nuevo dibujo
        
        time.sleep(0.02)  # Pausa de 0.02 segundos (crea una tasa de aprox. 50 fotogramas por segundo)
        angulo_actual += 1  # Incrementa el ángulo para que la flor gire continuamente
        
except turtle.Terminated:
    # Evita que Python lance un error cuando cierras la ventana manualmente
    print("Animación cerrada correctamente.")