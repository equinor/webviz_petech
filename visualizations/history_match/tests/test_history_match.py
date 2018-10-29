import unittest
import pandas as pd

from webviz_history_match import HistoryMatch


class TestHistoryMatch(unittest.TestCase):
    def setUp(self):
        pass

    def test_csv_equal_to_df(self):
        pass

    def test_depends_on_history_match_js(self):
        hm = HistoryMatch(pd.DataFrame({'obs_group_name': 42,
                                         'ensemble_name': 42,
                                         'realization': 42,
                                         'total_pos': 42,
                                         'total_neg': 42,
                                         'number_data_points': 42},
                                         index=[0]))

        self.assertTrue(any(
            (('src', '{root_folder}/resources/js/history_match.js')
             in e.attributes) for e in hm.header_elements))


if __name__ == '__main__':
    unittest.main()
