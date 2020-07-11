import yaml
import json

def main():

    with open('data/search_data.yml', 'r')as f:
        data1 = yaml.load(f, Loader=yaml.FullLoader)
        # yaml.dump(data1, f, encoding='utf-8', allow_unicode=True)
        data1=json.dumps(data1)
        print(type(data1))
        print(data1)


if __name__ == '__main__':
    main()