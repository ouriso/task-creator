from src.plugins.plugin_filter_date import plugin_filter_date
from src.plugins.plugin_filter_day import plugin_filter_day

from .plugin import Plugin

registry = {
    'day': plugin_filter_day,
    'date': plugin_filter_date
}


class PluginFilter(Plugin):
    registry = registry
