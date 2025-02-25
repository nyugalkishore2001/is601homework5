from plugins.base_plugin import BasePlugin

class SubtractionPlugin(BasePlugin):
    def execute(self, a, b):
        """
        Subtract two numbers.
        """
        return a - b