# -*- coding: utf-8 -*-
"""
comments
author: diqiuzhuanzhuan
email: diqiuzhuanzhuan@gmail.com

"""
import os

root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(root_path, "data")

borrower_info_file = os.path.join(data_path, "user_info.csv")
assert(os.path.exists(borrower_info_file))

borrower_behavior_log_file = os.path.join(data_path, "user_behavior_logs.csv")
assert(os.path.exists(borrower_behavior_log_file))

borrower_taglist_file = os.path.join(data_path, "user_taglist.csv")
assert(os.path.exists(borrower_taglist_file))

listing_info_file = os.path.join(data_path, "listing_info.csv")
assert(os.path.exists(listing_info_file))

train_file = os.path.join(data_path, "train.csv")
assert(os.path.exists(train_file))