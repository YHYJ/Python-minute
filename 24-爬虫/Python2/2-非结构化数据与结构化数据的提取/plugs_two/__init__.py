# -*- coding: utf-8 -*-


def print_info():
    """打印提示信息"""
    de_code = raw_input("网页原始编码：")
    en_code = raw_input("期望编码(utf-8)：")
    a_page = int(raw_input("起始页码："))
    e_page = int(raw_input("结束页码："))
    filename = raw_input("文件名：")
    file_type = raw_input("文件类型(None)：")
    file_dir = raw_input("存储路径(./data/html/)：")
    return de_code, en_code, a_page, e_page, filename, file_type, file_dir