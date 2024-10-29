from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import pandas as pd

class ActionConsultarInventario(Action):
    def name(self):
        return "action_consultar_inventario"

    def run(self, dispatcher, tracker, domain):
        producto = tracker.get_slot('producto')
        # Datos de ejemplo; en producción se cargarían desde un archivo o base de datos
        stock = 500  # Simulación de stock actual
        punto_reorden = 200  # Punto de reorden

        dispatcher.utter_message(
            text=f"El stock actual de {producto} es {stock}. El punto de reorden es {punto_reorden}."
        )
        return []
