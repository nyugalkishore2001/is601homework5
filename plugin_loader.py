import importlib
import os
import inspect
from plugins.base_plugin import BasePlugin

class PluginLoader:
    def __init__(self, plugin_folder="plugins"):
        self.plugin_folder = plugin_folder
        self.plugins = self._load_plugins()

    def _load_plugins(self):
        """
        Load all plugins from the plugins folder.
        """
        plugins = {}
        for filename in os.listdir(self.plugin_folder):
            if filename.endswith(".py") and filename != "base_plugin.py":
                module_name = filename[:-3]  
                try:
                    module = importlib.import_module(f"plugins.{module_name}")
                    for name, obj in inspect.getmembers(module):
                        if inspect.isclass(obj) and issubclass(obj, BasePlugin) and obj != BasePlugin:
                            plugins[module_name] = obj()
                except Exception as e:
                    print(f"Error loading plugin '{module_name}': {e}")
        return plugins

    def get_plugin(self, plugin_name):
        
        return self.plugins.get(plugin_name)

    def list_plugins(self):
        
        return list(self.plugins.keys())