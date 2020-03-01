import unittest
import pandas
from task.etl.data_cleanser import DataCleanser


class DataCleanserTest(unittest.TestCase):

    def test_successful_normalize_column_names(self):
        source_data_frame = pandas.DataFrame(columns=['Column Name with (parenthesis)'])
        target_data_frame = pandas.DataFrame(columns=['column_name_with_parenthesis'])

        DataCleanser.normalize_column_names(source_data_frame)

        self.assertEqual(source_data_frame.columns, target_data_frame.columns)

    def test_successful_normalize_mapped_column_name(self):
        source_name = 'Column name 1'
        target_name = 'column_name_1'
        source_data_frame = pandas.DataFrame(columns=[source_name])
        target_data_frame = pandas.DataFrame(columns=[target_name])

        DataCleanser.normalize_mapped_column_name(source_data_frame, source_name, target_name)

        self.assertEqual(source_data_frame.columns, target_data_frame.columns)


if __name__ == '__main__':
    unittest.main()
