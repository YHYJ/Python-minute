# -*- coding: utf-8 -*-

"""http://www.neihan8.com/article/list_5_1.html"""
import re

from plugs.Save import SaveData
from plugs.Spider import Spider
from plugs.DataTreat import DataTreat


if __name__ == '__main__':
    """抓取数据"""
    de_code = raw_input("网页原始编码：")
    en_code = raw_input("期望编码(utf-8)：")
    a_page = int(raw_input("起始页码："))
    e_page = int(raw_input("结束页码："))
    filename = raw_input("文件名：")
    file_type = raw_input("文件类型(None)：")
    file_dir = raw_input("存储路径(./data/html/)：")
    raw_input("<INFO> 检查代码，回车执行")
    for page in range(a_page, e_page + 1):
        url = "http://www.neihan8.com/article/list_5_{}.html".format(page)
        print("正在抓取：{}".format(url))
        spider = Spider(url, de_code)
        data = spider.load_page()

        """数据处理"""
        pattern = re.compile(r'<div class="f18 mb20">(.*?)</div>',
                             re.S)  # re.S表示启用DOTALL模式，让.也可以匹配换行符
        pattern_content = re.compile(r"<.*?>|&.*?;|\s|　")
        '''匹配网页里的无用字符
            <> 表示匹配标签 <p> <br>
            &.*?; 表示HTML实体字符
            \s 表示英文的空白字符 \n
            　:表示 \u3000 全角空格
        '''
        data_tread = DataTreat(data, pattern, pattern_content)  # 数据处理类对象

        print("<INFO> 过滤数据ing...")
        data_list = data_tread.treat()   # 第一道处理手续

        no_saved_data = []
        print("<INFO> 修饰数据ing...")
        for data in data_list:
            ultimate_data = data_tread.treat_two(data)  # 处理完成
            no_saved_data.append(ultimate_data)

        """存储数据"""
        full_file_name = "{}_{}".format(filename, page)
        save = SaveData(no_saved_data, full_file_name)
        save.save_to_file()
