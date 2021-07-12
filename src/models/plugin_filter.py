from src.plugins.plugin_filter_calendar import plugin_filter_calendar
from src.plugins.plugin_filter_date import plugin_filter_date
from src.plugins.plugin_filter_day import plugin_filter_day

from .plugin import Plugin


class PluginFilter(Plugin):
    registry = {
        'day': plugin_filter_day,
        'date': plugin_filter_date,
        'calendar': plugin_filter_calendar,
    }
