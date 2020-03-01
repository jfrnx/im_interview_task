import os
from datetime import date


def pull_today_csv(bucket_name):
    current_date = date.today().strftime("%Y%m%d")
    current_date = 20190620
    os.system("gsutil cp gs://{}/*{}.csv tmp/source.csv".format(bucket_name, current_date))


# def push(bucket_name, ):
#     os.system("gsutil cp tmp/source.csv gs://{}/*{}.csv ".format(bucket_name, current_date))
