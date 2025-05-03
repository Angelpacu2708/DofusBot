import cv2
import pyautogui
import numpy as np
import os

class Detector:
    def __init__(self, threshold=0.8):
        self.threshold = threshold
        self.nodes_path = "assets/nodes/iron"

    def find_node(self):
        # Captura de pantalla en escala de grises
        screenshot = pyautogui.screenshot()
        screen = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

        for img_name in os.listdir(self.nodes_path):
            print(f"Buscando: {img_name}")
            if not img_name.lower().endswith(('.png', '.jpg', '.jpeg')): # Filtra solo imágenes
                continue

            template = cv2.imread(os.path.join(self.nodes_path, img_name), cv2.IMREAD_GRAYSCALE)
            if template is None:
                continue  # Por si la imagen está dañada o mal guardada

            result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
            loc = np.where(result >= self.threshold)
            for pt in zip(*loc[::-1]):
                w, h = template.shape[::-1]
                center_x = pt[0] + w // 2
                center_y = pt[1] + h // 2
                return (center_x, center_y)

        return None
      