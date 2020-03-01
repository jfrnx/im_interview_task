from enum import Enum


class Columns(Enum):
    creative_date = "Creative Date", "creative_date", "datetime"
    deal_id = "Deal ID", "deal_id", "numeric"
    insertion_order_id = "Insertion Order ID", "insertion_order_id", "numeric"
    line_item_id = "Line Item ID", "line_item_id", "numeric"
    creative_id = "Creative ID", "creative_id", "numeric"
    creative_impressions = "Creative Impressions", "creative_impressions", "numeric"
    ctr = "CTR (%)", "ctr", "numeric"
    cpm = "CPM (£)", "cpm", "numeric"
    cpconv = "CPConv (£)", "cpconv", "numeric"

    def __new__(cls, source_name, target_name, data_type):
        """
        Define columns in the data structure

        Args:
            source_name (str): source column name of the data structure
            target_name (str): desired column name of new data structure
            data_type (str): type of data the column should contain (datetime, numeric)
        """

        obj = object.__new__(cls)
        obj._value_ = source_name
        obj.target_name = target_name
        obj.data_type = data_type
        return obj
