import pyautogui
import random
import time

class InputController:
    def click(self, coords):
        x, y = coords
        pyautogui.moveTo(x, y, duration=random.uniform(0.3, 0.7))
        ##pyautogui.click()
        time.sleep(random.uniform(0.5, 1.5))
