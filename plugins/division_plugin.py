from plugins.base_plugin import BasePlugin

class DivisionPlugin(BasePlugin):
    def execute(self, a, b):
        """
        Divide two numbers.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b