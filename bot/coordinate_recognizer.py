import cv2
import numpy as np
import pyautogui
import os

class CoordinateRecognizer:

    def __init__(self, coords_path, threshold=0.85):
        self.coords_path = coords_path
        self.threshold = threshold
        self.templates = self.load_templates()

    def load_templates(self):
        templates = {}

        for filename in os.listdir(self.coords_path):
            path = os.path.join(self.coords_path, filename)

            # Ignorar carpetas, solo procesar archivos
            if not os.path.isfile(path):
                continue

            # Filtrar solo imágenes
            if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                continue

            # Leer imagen en gris
            img = cv2.imread(path, 0)

            # Validar que se haya cargado bien
            if img is None:
                print(f"Advertencia: No se pudo cargar la imagen {filename}. Saltando.")
                continue

            coord_name = filename.rsplit(".", 1)[0]  # Quitar extensión de forma más segura
            templates[coord_name] = img
            print(f"Cargada imagen de nodo: {coord_name}")

        return templates

    def get_current_coordinate(self):
        # Capturar TODA la pantalla
        screenshot = pyautogui.screenshot()
        img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

        best_match = None
        best_value = 0

        for coord_name, template in self.templates.items():
            # Redimensionar plantilla si es más grande que pantalla (por seguridad)
            if template.shape[0] > img.shape[0] or template.shape[1] > img.shape[1]:
                continue

            res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
            _, val, _, _ = cv2.minMaxLoc(res)

            if val > best_value:
                best_value = val
                best_match = coord_name

        if best_value >= self.threshold:
            return best_match  # Devuelve nombre del fichero como coordenada
        else:
            return None