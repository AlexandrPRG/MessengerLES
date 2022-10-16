import yaml


def yaml_save(data: dict):
    with open('file.yaml', 'w', encoding='utf-8') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True)


if __name__ == '__main__':
    data_dict = {'list': ['p', 'o', 2, 'm'],
                 'int': 5,
                 'dict_inn': {'1в': "1в", "2д": "2д"},}
    yaml_save(data_dict)
    with open('file.yaml', encoding='utf-8') as f:
        content = yaml.load(f, Loader=yaml.FullLoader)
    print(content)
