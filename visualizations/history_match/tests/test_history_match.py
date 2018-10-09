import unittest
import pandas as pd

from webviz_history_match import HistoryMatch


class TestHistoryMatch(unittest.TestCase):
    def setUp(self):
        pass

    def test_csv_equal_to_df(self):
        pass

    def test_depends_on_history_match_js(self):
        hm = HistoryMatch([pd.DataFrame({'pos': 1, 'neg': 1}, index=['Obs. group 1'])], ['Iteration 1'])
        self.assertTrue(any(
            (('src', '{root_folder}/resources/js/history_match.js') in e.attributes)
            for e in hm.header_elements))

if __name__ == '__main__':
    unittest.main()

