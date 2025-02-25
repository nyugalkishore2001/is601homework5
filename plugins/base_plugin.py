from abc import ABC, abstractmethod

class BasePlugin(ABC):
    """
    Base class for all plugins.
    """
    @abstractmethod
    def execute(self, *args, **kwargs):
        """
        Execute the plugin's functionality.
        """
        pass