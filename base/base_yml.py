import csv
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


def write_data_to_csv(filename, data, rowname):
    with open("../data/"+filename+".csv", 'w', encoding='utf-8', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(rowname)
        for i in data:
            csv_writer.writerow(i)


def read_data_from_csv(filename):
    with open("../data/"+filename+".csv", 'r')as f:
        f_csv = csv.reader(f)
        data1 = [i for i in f_csv]
        del data1[0]
    return data1


if __name__ == '__main__':
    data = read_yml_data_with_file('generate')
    write_data_to_csv('test', data, ['username', 'password'])
    print(read_data_from_csv('test'))


