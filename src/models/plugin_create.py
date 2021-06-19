from .plugin import Plugin

from ..plugins.plugin_create_pocket import plugin_create_pocket

registry = {
    'pocket': plugin_create_pocket
}


class PluginCreate(Plugin):
    registry = registry
