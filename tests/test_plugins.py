from datetime import datetime as dt
from datetime import timedelta
from unittest import TestCase

from src.plugins.plugin_filter_day import plugin_filter_day
from src.plugins.plugin_filter_repeat import plugin_filter_repeat


class TestPlugins(TestCase):
    def test_plugin_repeat(self):
        today = dt.today()
        delta = timedelta(days=2)
        day = today.strftime('%d').replace('0', '')
        month = today.strftime('%m').replace('0', '')

        params_1 = {
            'from_date': (today - delta).strftime('%Y-%m-%d'),
            'to_date': (today + delta).strftime('%Y-%m-%d'),
            'days': day,
            'months': month
        }
        result = plugin_filter_repeat(**params_1)
        self.assertTrue(result)

        params_2 = {
            'to_date': (today + delta).strftime('%Y-%m-%d'),
            'days': '1-31',
            'months': str(int(month) - 2)
        }
        result = plugin_filter_repeat(**params_2)
        self.assertFalse(result)

    def test_plugin_day(self):
        test_all = 'Sun,Mon-Fri,Sat'
        test_any = 'any'
        test_wrong = 'wro'

        self.assertTrue(plugin_filter_day(test_all))
        self.assertTrue(plugin_filter_day(test_any))
        self.assertFalse(plugin_filter_day(test_wrong))
