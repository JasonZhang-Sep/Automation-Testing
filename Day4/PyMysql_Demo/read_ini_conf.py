import configparser
import pathlib


# 基于section获取ini配置文件中的配置项
def read(section_name):
    file = pathlib.Path(__file__).parents[0].resolve() / 'mysql_conf.ini'
    if not file.exists() or not file.is_file():
        raise FileNotFoundError(f'配置文件不存在:{file.name}')
    else:
        try:
            # 读取配置文件
            conf = configparser.ConfigParser()    # 通过模块名.类名()创建ConfigParser()对象,用于读取配置文件
            conf.read(file, encoding='utf-8')
            values = dict(conf.items(section_name))  # conf.items()返回的是一个元组列表,通过dict()转换成字典
            # 将values中的纯数字型字符串转为int类型
            for key, value in values.items():
                if value.isdigit():
                    values[key] = int(value)
            return values

        except configparser.NoSectionError:
            raise Exception(f'配置文件不存在该section:{section_name}')
        except Exception as e:
            raise Exception('配置读取错误') from e

print(read('test_env'))




