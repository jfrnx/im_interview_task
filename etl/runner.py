import logging.config
import pandas
from task.etl import config
from task.etl.cloud_util import CloudUtil
from task.etl.column import Columns
from task.etl.data_cleanser import DataCleanser
from task.etl.metric_calculations import MetricsCalculator

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s|%(levelname)s|%(message)s", datefmt="%Y-%m-%dT%H:%M:%S", filename=config.log_file)
    logging.info("Starting process")

    logging.info("Pulling from bucket")
    CloudUtil.pull()
    logging.info("Successfully pulled from bucket")

    pandas.options.mode.use_inf_as_na = True
    try:
        source_data_frame = pandas.read_csv(config.source_file)
    except Exception:
        logging.error("File not found")
        exit(1)

    logging.info("Starting data cleansing")
    logging.info("Normalising data")
    for column in list(Columns):
        DataCleanser.normalize_mapped_column_name(source_data_frame, column.value, column.target_name)
        if column.data_type == "datetime":
            DataCleanser.clean_date_column(source_data_frame, column.target_name)
        elif column.data_type == "numeric":
            DataCleanser.clean_numeric_column(source_data_frame, column.target_name)
    logging.info("Finished normalising data")

    logging.info("Removing bad data")
    source_data_frame.dropna(inplace=True)
    DataCleanser.clean_zero_value_column(source_data_frame, Columns.creative_impressions.target_name)
    logging.info("Finished removing bad data")
    logging.info("Finished data cleansing")

    logging.info("Starting calculations for daily metrics")
    daily_output_data_frame = MetricsCalculator.calculate_daily_metrics(source_data_frame)
    daily_output_data_frame.to_csv(config.daily_file, index=False)
    logging.info("Finished calculations for daily metrics")

    logging.info("Starting calculations for weekly metrics")
    weekly_output_data_frame = daily_output_data_frame
    weekly_output_data_frame['week_and_year'] = weekly_output_data_frame['creative_date'].dt.week.astype(str) + "-" + weekly_output_data_frame['creative_date'].dt.year.astype(str)
    weekly_output_data_frame = weekly_output_data_frame.groupby(weekly_output_data_frame['week_and_year']).sum()
    weekly_output_data_frame.to_csv(config.weekly_file)
    logging.info("Finished calculations for weekly metrics")

    logging.info("Pushing to cloud")
    CloudUtil.push(config.daily_file, config.daily_object_name)
    CloudUtil.push(config.weekly_file, config.weekly_object_name)
    logging.info("Successfully pushed to cloud")
