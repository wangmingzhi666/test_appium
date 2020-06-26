import yaml

def main():
    data = ['1', '2', '3', {'name': 'a', 'age': '12'}]
    with open('test.yml', 'w')as f:
        # data = yaml.load(f, Loader=yaml.FullLoader)
        yaml.dump(data, f, encoding='utf-8', allow_unicode=True)
        print(type(data))
        print(data)


if __name__ == '__main__':
    main()
    # ['1', '2', '3', {'name': 'a', 'age': '12'}]