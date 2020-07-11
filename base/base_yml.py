import os
import yaml


# 负责yaml文件的读取
def read_yml_data_with_file(filename):
    with open('../data/'+filename+'.yml', 'r')as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data


# 负责yaml文件的写入
def write_yml_to_file(py_object, yaml_file):
    from ruamel import yaml
    with open('./data/'+yaml_file+'.yml', 'a', encoding='utf-8')as f:
        yaml.dump(py_object, f, Dumper=yaml.RoundTripDumper)


if __name__ == '__main__':
    # from scripts.test_tpshop import fake_data
    # write_yml_to_file(fake_data(10), 'generate')
    print(read_yml_data_with_file('generate'))


