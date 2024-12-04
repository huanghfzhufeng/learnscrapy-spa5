import json

class SPA5Pipeline:
    def __init__(self):
        self.data = []

    def open_spider(self, spider):
        # 使用 UTF-8 编码打开文件
        self.file = open('data.json', 'w', encoding='utf-8')
        self.file.write("[")

    def close_spider(self, spider):
        # 写入剩余数据
        if self.data:
            self.write_to_file(final_write=True)
        # 结束 JSON 数组
        self.file.write("]")
        self.file.close()

    def process_item(self, item, spider):
        item_dict = dict(item)
        self.data.append(item_dict)
        if len(self.data) >= 300:
            self.write_to_file()
        return item

    def write_to_file(self, final_write=False):
        for i, entry in enumerate(self.data):
            # 写入 JSON，保留中文格式
            json.dump(entry, self.file, ensure_ascii=False, indent=4)
            if not (final_write and i == len(self.data) - 1):
                self.file.write(",\n")
        self.data = []
