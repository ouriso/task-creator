from src.plugins.plugin_filter_repeat import plugin_filter_repeat
from src.plugins.plugin_filter_day import plugin_filter_day

from .plugin import Plugin

registry = {
    'day': plugin_filter_day,
    'repeat': plugin_filter_repeat
}


class PluginFilter(Plugin):
    registry = registry
