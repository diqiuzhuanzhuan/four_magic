# -*- coding: utf-8 -*-
"""
comments
author: diqiuzhuanzhuan
email: diqiuzhuanzhuan@gmail.com

"""
from configuration import config
import pandas as pd
import time


class Borrower(object):
    table = None
    heads = None

    def __init__(self):
        self._import()
        self._transformation()

    def __str__(self):
        return "borrower"

    def __repr__(self):
        return "borrower"

    def _import(self):
        try:
            print("start read borrower information file {}".format(config.borrower_info_file))
            self.table = pd.read_csv(config.borrower_info_file)
            self.heads = list(self.table)
            print(list(self.table))
            "用户id，注册时间（精确到月份），性别，省份id，城市id，嵌入日期"
            all_id = self.table["user_id"].tolist()
            print(all_id.__len__(), set(all_id).__len__())
        except Exception as e:
            print("读取borrower信息失败：{}".format(e))

    def _transformation(self):
        """将reg_mon 变成自2000年第多少个月
            将gender编程男-->0, 女--> 1, 未知--> 2 的编码
        """

        def _transformation_reg_mon(reg_mon):
            base = 2000
            res = map(lambda row: row.split("-"), reg_mon)
            res = map(lambda row: (int(row[0]) - base) * 12 + int(row[1]), res)
            return list(res)

        def _transformation_gender(gender):
            """
            男编码为0，女编码为1，未知编码为2
            :param gender:
            :return:
            """
            flag = {"男": 0, "女": 1}
            res = map(lambda row: flag.get(row, 2), gender)
            return list(res)

        def _transformation_cell_province(cell_province):
            res = map(lambda row: int(row.replace("c", "")) if row != '\\N' else -1, cell_province)
            return list(res)

        def _transformation_id_province(id_province):
            res = map(lambda row: int(row.replace("c", "")) if row != '\\N' else -1, id_province)
            return list(res)

        def _transformation_id_city(id_city):
            res = map(lambda row: int(row.replace("c", "")) if row != '\\N' else -1, id_city)
            return list(res)

        def _transformation_insertdate(insertdate):
            """
                转换成整形的年月日形式，如"2018-03-01"转变为20180301, 我们只需要比较大小，所以无妨
            :param insertdate:
            :return:
            """
            base = time.mktime(time.strptime("2010-01-01", "%Y-%m-%d"))
            res = map(lambda row: int((time.mktime(time.strptime(row, "%Y-%m-%d")) - base)/(24*3600)), insertdate)
            return list(res)

        self.table["reg_mon"] = _transformation_reg_mon(self.table["reg_mon"].values)
        self.table["gender"] = _transformation_gender(self.table["gender"].values)
        self.table["cell_province"] = _transformation_cell_province(self.table["cell_province"].values)
        self.table["id_province"] = _transformation_id_province(self.table["id_province"].values)
        self.table["id_city"] = _transformation_id_city(self.table["id_city"].values)
        self.table["insertdate"] = _transformation_insertdate(self.table["insertdate"].values)
        print(self.table["insertdate"])

        def export():
            return self.table


class Lister(object):
    table = None
    heads = None

    def __init__(self):
        self._import()
        self._transformation()
        pass

    def __str__(self):
        return "Lister"

    def __repr__(self):
        return "Lister"

    def _import(self):
        try:
            print("start read list information file {}".format(config.listing_info_file))
            self.table = pd.read_csv(config.listing_info_file)
            self.heads = list(self.table)
            print(self.heads)

        except Exception as e:
            print("读取listing信息失败：{}".format(e))

    def _transformation(self):
        """

        :return:
        """
        def _transformation_auditing_date(auditing_date):
            base = time.mktime(time.strptime("2010-01-01", "%Y-%m-%d"))
            res = map(lambda row: int((time.mktime(time.strptime(row, "%Y-%m-%d")) - base)/(24*3600)), auditing_date)
            return list(res)

        self.table["auditing_date"] = _transformation_auditing_date(self.table["auditing_date"].values)
        print(self.table["auditing_date"])

    def export(self):
        return self.table


class Trainer(object):

    def __init__(self):
        self._import()
        self._transformation()
        pass

    def _import(self):
        try:
            print("start read train file {}".format(config.train_file))
            self.table = pd.read_csv(config.train_file)
            self.heads = list(self.table)
        except Exception as e:
            print("读取train 文件失败：{}".format(e))

    def _transformation(self):

        def _transformation_auditing_date(auditing_date):
            base = time.mktime(time.strptime("2010-01-01", "%Y-%m-%d"))
            res = map(lambda row: int((time.mktime(time.strptime(row, "%Y-%m-%d")) - base) / (24 * 3600)),
                      auditing_date)
            return list(res)

        def _transformation_due_date(due_date):
            base = time.mktime(time.strptime("2010-01-01", "%Y-%m-%d"))
            res = map(lambda row: int((time.mktime(time.strptime(row, "%Y-%m-%d")) - base) / (24 * 3600)),
                      due_date)
            return list(res)

        def _transformation_repay_date(repay_date):
            base = time.mktime(time.strptime("2010-01-01", "%Y-%m-%d"))
            res = map(lambda row: "2010-01-01" if row == "\\N" else row, repay_date)
            res = map(lambda row: int((time.mktime(time.strptime(row, "%Y-%m-%d")) - base) / (24 * 3600)),
                      res)
            return list(res)

        def _transformation_repay_amt(repay_amt):
            res = map(lambda row: 0 if row == "\\N" else row, repay_amt)
            return list(res)

        self.table["auditing_date"] = _transformation_auditing_date(self.table["auditing_date"].values)
        self.table["due_date"] = _transformation_due_date(self.table["due_date"].values)
        self.table["repay_date"] = _transformation_repay_date(self.table["repay_date"].values)
        self.table["repay_amt"] = _transformation_repay_amt(self.table["repay_amt"].values)
        print(self.table["auditing_date"])
        print(self.table["due_date"])
        print(self.table["repay_date"])
        print(self.table["repay_amt"])


class Director(object):

    def __init__(self):
        self.trainer_table = Trainer().table
        self.lister_table = Lister().table
        self.borrower_table = Borrower().table

    def create_feature(self):

        def _create_feature(user_id, listing_id, auditing_date):
            borrower_info = self.borrower_table[self.borrower_table["user_id"] == user_id]
            listing_info = self.lister_table[self.lister_table["listing_id"] == listing_id]
            if borrower_info[borrower_info["insertdate"] < auditing_date].__len__():
                borrower_feature = borrower_info.iloc[0]
                print("borrower_feature is {}".format(borrower_feature))
            else:
                print("error")
            if listing_info[listing_info["auditing_date"] < auditing_date].__len__():
                listing_feature = listing_info.iloc[0]
                print("list_feature is {}".format(listing_feature))
            else:
                print("error")

        res = map(lambda row: _create_feature(row[0], row[1], row[2]),
            zip(self.trainer_table["user_id"].values, self.lister_table["listing_id"].values, self.trainer_table["auditing_date"].values))
        print(list(res))


if __name__ == "__main__":
    Director().create_feature()
