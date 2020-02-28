from pandas import to_numeric
from pandas import to_datetime


class DataCleanser:
    @staticmethod
    def normalize_column_headings(data_frame):
        data_frame.columns = data_frame.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

    @staticmethod
    def clean_date_column(column_name, data_frame):
        data_frame[column_name] = to_datetime(data_frame[column_name], errors='coerce')

    @staticmethod
    def clean_integer_column(column_name, data_frame):
        data_frame[column_name] = to_numeric(data_frame[column_name], errors='coerce')
