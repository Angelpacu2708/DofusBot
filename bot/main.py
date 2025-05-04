import time
from bot.coordinate_recognizer import CoordinateRecognizer
import pyautogui
from bot.miner import Miner


# Ruta de mapas que escogeremos
path = "assets/maps"
isLeft = None
isDown = None
last_coord = None

# Inicializar el reconocedor
recognizer = CoordinateRecognizer(coords_path=path)

# La ruta donde tienes las imágenes de los minerales
miner = Miner(nodes_path="assets/nodes/flower") 

def click_left():
    screen_width, screen_height = pyautogui.size()
    x = int(screen_width * 0.05)
    y = int(screen_height * 0.5)
    pyautogui.moveTo(x, y, duration=0.5)
    pyautogui.click()

def click_right():
    screen_width, screen_height = pyautogui.size()
    x = int(screen_width * 0.95)
    y = int(screen_height * 0.5)
    pyautogui.moveTo(x, y, duration=0.5)
    pyautogui.click()


while True:
    coord = recognizer.get_current_coordinate()

    if coord:
        coord = coord.split(".")[0]  # Limpiar nombre
        print("Coordenada detectada:", coord)

        # Solo si la coordenada ha cambiado
        if coord != last_coord:
            last_coord = coord


            # 🚨 NUEVO: buscar y recolectar nodos
            print("Buscando nodos para recolectar...")
            miner.find_and_collect_nodes()

            if coord == "3,-14":
                print("Mover derecha")
                isLeft = True

            elif coord == "10,-14":
                print("Mover izquierda")
                isLeft = False

            if isLeft:
                click_right()
            else:
                click_left()

    else:
        print("No se pudo detectar coordenada.")


    # Espera un poco antes de buscar otra vez
    time.sleep(2)

