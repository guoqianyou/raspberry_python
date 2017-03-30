import socketserver
import time
from socketserver import BaseRequestHandler

from myloger import GetSysLoger

# log 引入
logger = GetSysLoger(__file__).logger_sys()


# socket 服务
class MySocketServere(BaseRequestHandler):
    def handle(self):
        logger.info("有客户端连接成功！ 客户端：" + self.client_address.__str__())
        conn = self.request
        while True:
            try:
                logger.info("开始接收数据,等待客户端发送数据。。。")
                data_size = conn.recv(1024)
                data_len = int(data_size.decode())
                logger.info("接收到的数据长度：" + data_len.__str__())
                received_size = 0  # 记录接收长度
                received_data = b''  # 声明空bytes
                while received_size != data_len:
                    data = conn.recv(1024)
                    received_size += len(data)
                    received_data += data  # 接收命令结果
                else:
                    logger.info("接收到的数据为： " + received_data.decode())

                send_data = "已经接收到！"
                logger.info("发送返回的数据：" + send_data)
                conn.send(str(len(send_data.encode())).encode('utf-8'))
                time.sleep(0.5)
                conn.send(send_data.encode('utf-8'))
                logger.info("发送完成！")
            except Exception as e:
                logger.warn("客户端断开了！", e)
                break


# 启动
def run_socket_server(port=8899):
    server = socketserver.ThreadingTCPServer(("0.0.0.0", port), MySocketServere)
    server.serve_forever()


if __name__ == '__main__':
    #  启动服务
    logger.info("zhunbei")
    server = socketserver.ThreadingTCPServer(("0.0.0.0", 8899), MySocketServere)
    server.serve_forever()
