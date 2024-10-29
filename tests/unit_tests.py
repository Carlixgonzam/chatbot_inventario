import unittest
from actions.actions import ActionConsultarInventario

class TestActions(unittest.TestCase):
    def test_action_consultar_inventario(self):
        action = ActionConsultarInventario()
        response = action.run()
        self.assertIn("stock actual", response)

if __name__ == "__main__":
    unittest.main()
