from src.plugins.plugin_create_pocket import plugin_create_pocket

from .plugin import Plugin

registry = {
    'pocket': plugin_create_pocket
}


class PluginCreate(Plugin):
    registry = registry
