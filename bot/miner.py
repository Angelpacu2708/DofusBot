import os
import cv2
import numpy as np
import pyautogui
import time

class Miner:
    def __init__(self, nodes_path, threshold=0.85):
        self.nodes_path = nodes_path
        self.threshold = threshold
        self.templates = self.load_templates()

    def load_templates(self):
        templates = {}

        for filename in os.listdir(self.nodes_path):
            path = os.path.join(self.nodes_path, filename)

            # Ignorar carpetas
            if not os.path.isfile(path):
                continue

            # Solo imágenes
            if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                continue

            img = cv2.imread(path, 0)
            if img is None:
                continue

            node_name = filename.rsplit(".", 1)[0]
            templates[node_name] = img
            print(f"Cargado nodo: {node_name}")

        return templates

    def find_and_collect_nodes(self):
        # Capturar pantalla completa
        screenshot = pyautogui.screenshot()
        img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

        found = False

        for node_name, template in self.templates.items():
            res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

            if max_val >= self.threshold:
                found = True

                # Click en el nodo
                node_w, node_h = template.shape[::-1]
                center_x = max_loc[0] + node_w // 2
                center_y = max_loc[1] + node_h // 2

                pyautogui.moveTo(center_x, center_y, duration=0.5)
                pyautogui.click()
                print(f"Recolectando nodo: {node_name} en ({center_x}, {center_y})")

                # Esperar para no recolectar el mismo varias veces
                time.sleep(5)

        if not found:
            print("No se han encontrado nodos en este mapa.")