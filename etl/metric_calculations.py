import pandas
from task.etl.column import Columns


class MetricsCalculator:
    @staticmethod
    def calculate_daily_metrics(data_frame):
        """
        Calculates the clicks, spend and conversions for a specific set of data
        Args:
            data_frame (pandas.DataFrame): a data frame containing creative date, creative impressions, ctr and cpm
        Return:
            data_frame (pandas.DataFrame): a data frame containing creative date, clicks, spend and conversions
        """
        temp_data_frame = pandas.DataFrame()
        temp_data_frame[Columns.creative_date.target_name] = data_frame[Columns.creative_date.target_name]

        temp_data_frame['clicks'] = calculate_clicks(data_frame[Columns.creative_impressions.target_name],
                                                     data_frame[Columns.ctr.target_name])

        temp_data_frame['spend'] = calculate_spend(data_frame[Columns.creative_impressions.target_name],
                                                   data_frame[Columns.cpm.target_name])

        temp_data_frame['conversions'] = calculate_conversions(temp_data_frame['clicks'],
                                                               data_frame[Columns.ctr.target_name]).fillna(0)

        return temp_data_frame


def calculate_clicks(creative_impressions, ctr):
    return creative_impressions * ctr


def calculate_spend(creative_impressions, cpm):
    return (creative_impressions / 1000) * cpm


def calculate_conversions(clicks, ctr):
    return clicks * (ctr / 100)


