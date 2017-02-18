#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import path

import sys

from my_network import my_socket_server
from myloger import GetSysLoger


def run_main():
    # 启动socket 服务端
    logger.info("开始启动。。。。")
    logger.info("启动socket_server服务。。")
    my_socket_server.run_socket_server()


if __name__ == '__main__':
    logger = GetSysLoger(__file__).logger_sys()
    project_path = path.abspath(".")
    logger.info("项目路径为：" + project_path)
    sys.path.append(project_path)
    logger.info("添加路径成功")
    run_main()
