im_interview_task
-
The aim of this project is to download a file from a gcs cloud bucket for the current date (YYYYmmdd format), perform data cleaning, calculate the clicks, spend and conversions for the data and then upload this new set of data into another bucket in the current format and then grouped by week.

TODO:
- 
- Split reusable code into modules and split the config variables to only be accessed by the code that uses them
- Implement GCS utility methods for connecting to a bucket with a service account
- Extend unit test coverage
- Move logging config to separate config file
- Improve error handling
