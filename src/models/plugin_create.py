from src.plugins.plugin_create_pocket import plugin_create_pocket

from .plugin import Plugin


class PluginCreate(Plugin):
    registry = {
        'pocket': plugin_create_pocket
    }
