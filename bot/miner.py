from .detector import Detector
from .input_controller import InputController
from .navigator import Navigator
import time

class Miner:
    def __init__(self, route_path):
        self.detector = Detector()
        self.input_controller = InputController()
        self.navigator = Navigator(route_path)

    def run(self):
        while True:
            node_location = self.detector.find_node()

            if node_location:
                print("Nodo encontrado, recolectando...")
                self.input_controller.click(node_location)
                time.sleep(5)
            else:
                print("No hay nodos, moviéndose...")
                ## self.navigator.next_step()
                time.sleep(2)
