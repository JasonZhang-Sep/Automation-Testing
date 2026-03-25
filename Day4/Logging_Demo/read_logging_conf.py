import logging.config
import pathlib

def get_logger():
    try:
        # 获取路径
        file = pathlib.Path(__file__).parents[0].resolve() / 'log_conf.ini'
        # print(file)
        # print(type(file))
        if not file.exists() or not file.is_file():
            raise FileNotFoundError(f'Log_file not found in:{file}')
        else:
            # 加载日志配置文件
            logging.config.fileConfig(file, encoding='utf-8')
            # 创建日志记录器
            logger = logging.getLogger()
            return  logger
    except Exception as e:
        raise Exception('日志配置文件出错') from e

log = get_logger()
log.debug('这是日志')
