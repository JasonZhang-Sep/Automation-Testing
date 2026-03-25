import traceback

file_path = './test_data.txt'

# 文件读取

with open(file_path, 'r', encoding='utf-8') as file:
        data = [line.rstrip() for line in file]
        print(data)


# 文件读取
# file = open(file_path, 'r', encoding='utf-8')
# print(file.read())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readlines())

# 文件写入
# file = open(file_path, 'w', encoding='utf-8')
# file.write('''这是新写入的第一行数据
# 这是新写入的第二行数据
# 这是新写入的第三行数据
# ''')
# file.close()

# 文件追加写入
# file = open(file_path, 'a', encoding='utf-8')
# file.write('这是追加的第四行数据')
#
# file = open('./test_data1.txt', 'w', encoding='utf-8')
# file.write('新文件新数据')

# 文件复制,将读取到的旧文件内容，写入新文件之中
# file = open(file_path, 'r', encoding='utf-8')
# file_new = open('./test_new.txt', 'w', encoding='utf-8')
# try:
#     content = file.read()
#     file_new.write(content)
# except Exception as e:
#     traceback.print_exc()
#
# finally:
#     file.close()
#     file_new.close()

# 非文本文件读取，不需要加编码格式
# file = open('./img.png', 'rb')
# print(file.read())

# 自定义异常类，继承于Exception类
class DocOperationError(Exception):
    pass
# 封装文件操作函数
def file_operation(file_path, mode, content=None, **kwargs):
    valid_modes = ['r', 'w', 'a', 'rb', 'wb', 'ab']
    if mode not in valid_modes:
        raise ValueError(f"'不支持的格式{mode}',支持的格式为:'{valid_modes}'")
    try:
        with open(file_path, mode, **kwargs) as file:
            if mode == 'r':
                # 读取文本文件
                return [line.rstrip() for line in file]  # 列表推导式
            elif mode == 'rb':
                # 读取二进制文件
                return file.read()
            elif mode in ['w', 'a']:
                # 写入文本文件
                if content is not None:
                    file.write(content)
                    return '文本文件写入成功'
                else:
                    return '请输入要写入的内容'
            elif mode in ['wb', 'rb']:
                # 写入二进制文件
                if content is not None:
                    file.write(content)
                    return '二进制文件写入成功'
                else:
                    return '请输入要写入的内容'
    except FileNotFoundError:
        raise FileNotFoundError(f"文件'{file_path}'不存在")
    except Exception as e:
        raise DocOperationError('文件操作出错，请重试') from e


content = '''外部数据1
外部数据2
外部数据3
外部数据4
'''
result = file_operation('./test_data1.txt', 'r',content= content, encoding='utf-8')
print(result)
