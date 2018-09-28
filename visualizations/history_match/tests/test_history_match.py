import unittest

from webviz_history_match import HistoryMatch


class TestHistoryMatch(unittest.TestCase):
    def setUp(self):
        pass

    def test_csv_equal_to_df(self):
        pass

    def test_depends_on_map_js(self):
        hm = HistorMatch({}, {})
        self.assertTrue(any('resources/js/history_match.js' in path
                            for path in hm.get_js_dep()))


if __name__ == '__main__':
    unittest.main()

