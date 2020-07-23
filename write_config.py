import configparser
import logging


class config_rel():
    config = configparser.ConfigParser()

    def __init__(self, config_file):
        self.filename = config_file

    def write_config(self, config_info):
        try:
            for key, value in config_info.items():
                self.config[key] = value
                with open(self.filename, 'a')as configfile:
                    self.config.write(configfile)
        except:
            print('请检查传入的参数是否正确')

    def read_config(self, config_title):
        try:
            self.config.read(self.filename, encoding="utf-8")
            res = self.config.items(config_title)
            return res
        except configparser.NoSectionError as e:
            print("请先创建名为{}的文件再进行读取".format(self.filename))
        except configparser.DuplicateSectionError as e:
            print('您的配置文件{}中存在多个{}，请检查'.format(self.filename, config_title))

    def modify_config(self, section, option, value=None):
        self.config.read(self.filename)
        # self.config.add_section(section)
        if value:
            self.config.set(section, option, value)
        else:
            self.config.set(section, option)
        with open(self.filename, 'w')as f:
            self.config.write(f)


if __name__ == '__main__':
    config = config_rel('config.ini')

    con_dir = {'pytest': {'addopts': '-v -s --html=./report/report.html --alluredir ./report/result',
                          'testpaths': './scripts',
                          'python_files': 'test_weixin_selenium.py',
                          'python_classes': 'Test*',
                          'python_functions': 'test_*'
                          }}
    # config.write_config(con_dir)
    print(config.read_config('pytest'))

    import pymysql

    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='66231533', db='按时', charset='utf8')
    cursor = db.cursor()
    cursor.execute('select * from student')
    data = cursor.fetchall()
    print(data)
    # logger = logging.getLogger(__name__)
    # logger.setLevel(level=logging.INFO)
    # handler = logging.FileHandler("log.txt")
    # handler.setLevel(logging.INFO)
    # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # handler.setFormatter(formatter)
    # logger.addHandler(handler)
    #
    # logger.info("Start print log")
    # logger.debug("Do something")
    # logger.warning("Something maybe fail.")
    # logger.info("Finish")
