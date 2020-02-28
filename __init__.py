import pandas
from task import Column
from task.DataCleanser import DataCleanser
pandas.options.mode.use_inf_as_na = True

data_frame = pandas.read_csv("tmp/20190620.csv")

DataCleanser.normalize_column_headings(data_frame)

date_columns = ['creative_date']
numeric_columns = ['deal_id', 'insertion_order_id', 'line_item_id', 'creative_id', 'creative_impressions', 'ctr_%', 'cpm_£', 'cpconv_£']

for column in date_columns:
    DataCleanser.clean_date_column(column, data_frame)

for column in numeric_columns:
    DataCleanser.clean_integer_column(column, data_frame)

data_frame.dropna(inplace=True)
no_creative_impressions = data_frame[data_frame['creative_impressions'] == 0].index
data_frame.drop(no_creative_impressions, inplace=True)

data_frame['clicks'] = data_frame['creative_impressions'] * data_frame['ctr_%']
data_frame['spend'] = (data_frame['creative_impressions'] / 1000 ) * data_frame['cpm_£']
data_frame['conversions'] = (data_frame['spend'] / data_frame['cpconv_£']).fillna(0)

data_frame['conversions']
data_frame.to_csv('tmp/test.csv')
print(data_frame.to_string())
