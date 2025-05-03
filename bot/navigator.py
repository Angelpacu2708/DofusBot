import json
import time
import random
from .input_controller import InputController

class Navigator:
    def __init__(self, route_path):
        self.input_controller = InputController()
        with open(route_path, "r") as f:
            self.route = json.load(f)
        self.current_index = 0

    def next_step(self):
        if self.current_index >= len(self.route):
            self.current_index = 0

        coords = self.route[self.current_index]
        print(f"Moviéndose a {coords}")
        self.input_controller.click(coords)
        self.current_index += 1
        time.sleep(random.uniform(2, 4))
