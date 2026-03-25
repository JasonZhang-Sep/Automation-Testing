import configparser
import pathlib

import yaml


# 获取文件路径
def get_file(file_name):
    file = pathlib.Path(__file__).parents[0].resolve() / file_name
    return file


# 读取ini文件
def read_ini_conf(file_name, section, option):
    conf = configparser.ConfigParser()
    conf.read(get_file(file_name), encoding='utf-8')
    values = conf.get(section=section, option=option)
    return values


# 写入ini文件
def write_ini_conf(file_name, section=None, option=None, value=None, **kwargs):
    '''
       :param file_name: 文件名
       :param section: section 名称（可选）
       :param option: option 名称（可选）
       :param value: 配置值（可选）
       :param kwargs: 批量数据 {section1: {option1: value1}，section2: {option2: value2}}
    '''
    conf = configparser.ConfigParser()
    conf.read(get_file(file_name), encoding='utf-8')
    # 如果是批量写入模式
    if kwargs:
        for sec, opts in kwargs.items():
            # 第一次循环：sec = 'section1'，opts = {option1: value1}
            # 第二次循环：sec = 'section2'，opts = {option2: value2}
            if not conf.has_section(sec):
                conf.add_section(sec)
            for opt, val in opts.items():
                conf.set(section=sec, option=opt, value=val)
    else:
        # 单个写入模式
        # 如果没有该section，则添加
        if not conf.has_section(section):
            conf.add_section(section)
        conf.set(section=section, option=option, value=value)

    with open(get_file(file_name), 'w', encoding='utf-8') as f:
        conf.write(f)


# 读取yaml文件
def read_yaml(file):
    with open(file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        return data

