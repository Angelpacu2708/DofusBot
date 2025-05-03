import pyautogui
import time

class CoordinateNavigator:
    def __init__(self, target_coords):
        self.target_coords = target_coords

        self.directions = {
            "up": (700, 50),
            "down": (700, 900),
            "left": (300, 500),
            "right": (1300, 500)
        }

    def decide_direction(self, current_coord):
        current_x, current_y = current_coord
        target_x, target_y = self.target_coords

        if current_x < target_x:
            return "right"
        elif current_x > target_x:
            return "left"
        elif current_y < target_y:
            return "down"
        elif current_y > target_y:
            return "up"
        else:
            return None

    def move_direction(self, direction):
        if direction in self.directions:
            x, y = self.directions[direction]
            pyautogui.moveTo(x, y, duration=0.5)
            pyautogui.click()
            print(f"Moviéndose hacia: {direction}")
            time.sleep(5)  # tiempo para que cargue mapa