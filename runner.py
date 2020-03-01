import pandas
from task.DataCleanser import DataCleanser
from task.Column import Columns
from task.CloudUtil import pull_today_csv
from task import config


def calculate_clicks(column1, column2):
    return column1 * column2


def calculate_spend(column1, column2):
    return (column1 / 1000) * column2


def calculate_conversions(column1, column2):
    return column1 / column2


def calculate_daily_metrics(data_frame):
    temp_data_frame = pandas.DataFrame()
    temp_data_frame[Columns.creative_date.target_name] = data_frame[Columns.creative_date.target_name]

    temp_data_frame['clicks'] = calculate_clicks(data_frame[Columns.creative_impressions.target_name],
                                                 data_frame[Columns.ctr.target_name])
    # //source_data_frame['creative_impressions'] * source_data_frame['ctr']

    temp_data_frame['spend'] = calculate_spend(data_frame[Columns.creative_impressions.target_name],
                                               data_frame[Columns.cpm.target_name])
    # (source_data_frame['creative_impressions'] / 1000 ) * source_data_frame['cpm']

    temp_data_frame['conversions'] = calculate_conversions(temp_data_frame['spend'],
                                                           data_frame[Columns.cpconv.target_name]).fillna(0)
    # (daily_output_data_frame['spend'] / source_data_frame['cpconv']).fillna(0)
    return temp_data_frame


def calculate_weekly_metrics(data_frame):

    return data_frame


if __name__ == "__main__":
    pull_today_csv(config.source_bucket_name)

    pandas.options.mode.use_inf_as_na = True
    source_data_frame = pandas.read_csv("tmp/source.csv")

    for c in list(Columns):
        DataCleanser.normalize_mapped_column_name(source_data_frame, c.value, c.target_name)
        if c.data_type == "datetime":
            DataCleanser.clean_date_column(source_data_frame, c.target_name)
        elif c.data_type == "numeric":
            DataCleanser.clean_integer_column(source_data_frame, c.target_name)

    source_data_frame.dropna(inplace=True)
    DataCleanser.clean_zero_value_column(source_data_frame, Columns.creative_impressions.target_name)

    daily_output_data_frame = calculate_daily_metrics(source_data_frame)
    weekly_output_data_frame = calculate_weekly_metrics(daily_output_data_frame)

    daily_output_data_frame.to_csv('tmp/daily.csv', index=False)
    weekly_output_data_frame.to_csv('tmp/weekly.csv', index=False)
