#!/usr/bin/python3
# coding=utf-8
"""
Created on 2018年6月2日

@author: qcymkxyc

关于delicious数据集读取集
"""
import random


def read_tag(filename, skip_row=0):
    """读取标签数据集

    :param filename:  str
        文件名
    :param skip_row: int
        跳过的行数
    :return: tuple
        三元组(user_id,bookmark_id,tag_id)
    """
    with open(filename) as f:
        for i, line_data in enumerate(f):
            if i < skip_row:
                continue
            user_id, bookmark_id, tag_id = line_data.split("\t")[:3]
            yield int(user_id.strip()), int(bookmark_id.strip()), int(tag_id.strip())


def split_data(filename, k=0, cv_folder=10, seed=1, skip_row=1):
    """用cross validation分离训练集以及测试集

    :param filename: str
        文件名
    :param k: int
        cross validation 的第k轮
    :param cv_folder: int
        cross validation的总轮数
    :param seed: int
        random的seed
    :param skip_row: int
        跳过的行数
    :return: tuple
        训练集，测试集。均以三元组(user_id,bookmark_id,tag_id)形式返回
    """
    train_set = []
    test_set = []

    random.seed(seed)
    for sub_data in read_tag(filename, skip_row):
        if random.randint(0, cv_folder) == k:
            test_set.append(sub_data)
        else:
            train_set.append(sub_data)

    return train_set, test_set
