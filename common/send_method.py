# 封装接口请求方式
# 定义接口自动化测试的关键字类
import requests

class KeyDemo:
    # 定义get请求方法
    def get(self, url, headers=None, parama=None):
        return requests.get(url=url, headers=headers, paramas=parama)

    # 定义post方法
    def post(self, url, headers=None, parama=None):
        return requests.post(url=url, headers=headers, paramas=parama)

    # 校验字段获取方法
    def get_text(self):
        pass

    def test3_userinfo(self):
        # 将之前用例中获取的token进行调用，但同时又不要去调用用例的执行步骤
        pass
