import time
from plugins.base_plugin import BasePlugin

class AdditionPlugin(BasePlugin):
    def execute(self, a, b):
        """
        Add two numbers with a delay.
        """
        time.sleep(5)  # Simulate a long-running task
        return a + b