import os


class GCSUtil:
    """
    GCS utility class for how to interact with GCS
    """
    @staticmethod
    def pull(bucket_name, current_date, file_path):
        os.system("gsutil cp gs://{}/*{}.csv {}".format(bucket_name, current_date, file_path))

    @staticmethod
    def push(bucket_name, object_name, file_path):
        os.system("gsutil cp {} gs://{}/{}".format(file_path, bucket_name, object_name))
