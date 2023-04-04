import json
import flask
from flask import request

server = flask.Flask(__name__)  # 创建一个服务，把当前这个python文件当做一个服务


@server.route('/login', methods=['get', 'post'])  # @server.route()可以将普通函数转变为服务 登录接口的路径、请求方式
def login():
    username = request.values.get('username')  # 获取通过url请求传参的用户名

    pwd = request.values.get('pwd')  # 获取url请求传参的明文密码

    if username and pwd:  # 判断用户名、密码都不为空
        if username == 'admin' and pwd == '123456':
            res = {'code': 200, 'message': '登录成功'}
            return json.dumps(res, ensure_ascii=False)  # 将字典转换字符串
        else:
            res = {'code': -1, 'message': '账号密码错误！'}
            return json.dumps(res, ensure_ascii=False)
    else:
        res = {'code': 10001, 'message': '参数不能为空！'}
        return json.dumps(res, ensure_ascii=False)


if __name__ == '__main__':
    server.run(debug=True)
