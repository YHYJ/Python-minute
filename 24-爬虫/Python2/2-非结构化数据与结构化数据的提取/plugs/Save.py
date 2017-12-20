# -*- coding: utf-8 -*-


class SaveData:
    """存储抓取的数据"""
    def __init__(self, data_list, file_name, file_type=None, file_dir="./data/html/"):
        """
        :param data: 抓取的数据
        :param file_dir: 文件存储目录
        :param file_name: 文件名
        :param file_type: 文件类型
        """
        self.data_list = data_list
        self.file_dir = file_dir
        self.file_name = file_name
        self.file_type = file_type

    def save_to_file(self):
        """存储数据"""
        if self.file_type is None:
            full_file = "{}{}".format(self.file_dir, self.file_name)
            print "正在写入：{}".format(self.file_name)
        else:
            full_file = "{}{}.{}".format(self.file_dir, self.file_name, self.file_type)
            print "正在写入：{}.{}".format(self.file_name, self.file_type)
        try:
            with open(full_file, "a") as f:
                for data in self.data_list:
                    f.write(data)
                    f.write("\n\n")
                f.write("\n")
        except Exception as e:
            print("文件存储失败：{}".format(e))
        else:
            print "文件路径：<{}>\n".format(full_file)
