from pandas import to_numeric, to_datetime


class DataCleanser:
    @staticmethod
    def normalize_column_names(data_frame):
        """
        Cleans a data frame's column names in a standard way

        Args:
             data_frame (pandas.DataFrame): a pandas DataFrame object
        """
        data_frame.columns = data_frame.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

    @staticmethod
    def normalize_mapped_column_name(data_frame, source_name, target_name):
        """
        Renames a single column in a data frame from a specified source name to a desired name

        Args:
             data_frame (pandas.DataFrame): a pandas DataFrame object
             source_name (str): the starting name of the column to be changed
             target_name (str): the target name of the column to be changed
        """
        data_frame.rename(columns={source_name: target_name}, inplace=True)

    @staticmethod
    def clean_date_column(data_frame, column_name):
        """
        Cleans a column to only contain dates

        Args:
             data_frame (pandas.DataFrame): a pandas DataFrame object
             column_name (str): the column to be cleaned
        """
        data_frame[column_name] = to_datetime(data_frame[column_name], errors='coerce')

    @staticmethod
    def clean_numeric_column(data_frame, column_name):
        """
        Cleans a column to only contain numeric

        Args:
             data_frame (pandas.DataFrame): a pandas DataFrame object
             column_name (str): the column to be cleaned
        """
        data_frame[column_name] = to_numeric(data_frame[column_name], errors='coerce')

    @staticmethod
    def clean_zero_value_column(data_frame, column_name):
        """
        Cleans rows that contain a zero value in a specified column

        Args:
             data_frame (pandas.DataFrame): a pandas DataFrame object
             column_name (str): the column to be cleaned
        """
        no_creative_impressions = data_frame[data_frame[column_name] == 0].index
        data_frame.drop(no_creative_impressions, inplace=True)

