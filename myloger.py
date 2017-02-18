from logging.handlers import TimedRotatingFileHandler
from os import path

__author__ = "gqy"

import logging

# 当前的路径
_project_path = path.abspath(".")

_log_file_names = {}

# 定义handler的输出格式
_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')


# 获取loger
class GetSysLoger():
    def __init__(self, name):
        # 创建一个logger
        self._logger = logging.getLogger(name)
        self._logger.setLevel(logging.INFO)
        # 创建一个handler，用于输出到控制台
        _ch = logging.StreamHandler()
        _ch.setLevel(logging.INFO)
        _ch.setFormatter(_formatter)
        self._logger.addHandler(_ch)

    # 写入系统log文件中的log
    def logger_sys(self):
        # 系统log
        _sys_log_file = "sys_log.log"
        return self.logger_by_path(_sys_log_file)

    # 自定义 log 文件
    def logger_by_path(self, logfilename):
        if logfilename not in _log_file_names:
            print("该log 文件已经存在!  文件名为：" + logfilename)
            pass
        log_file_path = _project_path + logfilename
        # 创建一个handler，用于写入日志文件
        handler = TimedRotatingFileHandler(log_file_path, "MIDNIGHT", 1, 0)
        handler.setLevel(logging.INFO)
        handler.setFormatter(_formatter)
        self._logger.addHandler(handler)
        return self._logger

    # 获取普通log 只在控制台打印
    def logger_only(self):
        return self._logger
