import yaml

def main():

    with open('test.yml', 'r')as f:
        data1 = yaml.load(f, Loader=yaml.FullLoader)
        # yaml.dump(data, f, encoding='utf-8', allow_unicode=True)
        print(type(data1))
        print(data1)


if __name__ == '__main__':
    main()