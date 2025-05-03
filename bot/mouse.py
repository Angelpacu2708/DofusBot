import pyautogui
import time

# Obtener tamaño de la pantalla
screen_width, screen_height = pyautogui.size()

print("Mueve el mouse. Pulsa Ctrl + C para salir.")
try:
    while True:
        x, y = pyautogui.position()
        result = (x, y, screen_width, screen_height)
        print(f"Mouse y pantalla: {result}", end='\r')
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nPrograma terminado.")