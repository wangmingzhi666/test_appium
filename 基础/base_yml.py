import yaml


def yml_data_with_file(filename):
    with open('./data/'+filename+'.yml', 'r')as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

    return data


if __name__ == '__main__':
    print(yml_data_with_file('search_data')['data'])
