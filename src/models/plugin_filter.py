from src.plugins.plugin_filter_day import plugin_filter_day

from .plugin import Plugin

registry = {
    'day': plugin_filter_day
}


class PluginFilter(Plugin):
    registry = registry
