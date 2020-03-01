from pandas import to_numeric, to_datetime


class DataCleanser:
    @staticmethod
    def normalize_column_names(data_frame):
        data_frame.columns = data_frame.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

    @staticmethod
    def normalize_mapped_column_name(data_frame, source_name, target_name):
        data_frame.rename(columns={source_name: target_name}, inplace=True)

    @staticmethod
    def clean_date_column(data_frame, column_name):
        data_frame[column_name] = to_datetime(data_frame[column_name], errors='coerce')

    @staticmethod
    def clean_integer_column(data_frame, column_name):
        data_frame[column_name] = to_numeric(data_frame[column_name], errors='coerce')

    @staticmethod
    def clean_zero_value_column(data_frame, column_name):
        no_creative_impressions = data_frame[data_frame[column_name] == 0].index
        data_frame.drop(no_creative_impressions, inplace=True)
