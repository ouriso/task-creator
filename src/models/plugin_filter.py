from .plugin import Plugin
from ..plugins.plugin_filter_day import plugin_filter_day

registry = {
    'day': plugin_filter_day
}


class PluginFilter(Plugin):
    registry = registry
