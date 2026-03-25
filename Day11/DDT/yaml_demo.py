import yaml


# 读取yaml文件
def read_yaml(file):
    with open(file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        return data


print(read_yaml('./dict_demo.yaml'))
print(read_yaml('./list_demo.yaml'))
