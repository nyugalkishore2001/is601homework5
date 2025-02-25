from plugins.base_plugin import BasePlugin

class MultiplicationPlugin(BasePlugin):
    def execute(self, a, b):
        """
        Multiply two numbers.
        """
        return a * b