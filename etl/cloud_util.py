from datetime import date
from task.etl import config
from task.etl.gcs_util import GCSUtil


class CloudUtil:
    @staticmethod
    def pull():
        """
        Current cloud implementation for pulling from a bucket, uses current date to pull
        """
        current_date = get_current_date()
        GCSUtil.pull(config.source_bucket_name, current_date, config.source_file)

    @staticmethod
    def push(file_path, object_name):
        """
        Current cloud implementation for pulling from a bucket, appends current date to front of object name

        Args:
            file_path (str): path to the file to be pushed to a bucket
            object_name (str): name assigned to the object being pushed to a bucket
        """
        current_date = get_current_date()
        GCSUtil.push(config.target_bucket_name, current_date + "_" + object_name, file_path)


def get_current_date():
    return date.today().strftime("%Y%m%d")
