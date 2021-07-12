import unittest

# 创建一个unittest测试用例管理框架
import configparser

from BeautifulReport import BeautifulReport
from ddt import ddt,file_data
from common.send_method import KeyDemo
import yaml
import requests
import time

@ddt
class ApiCases(unittest.TestCase):
    # 公共部分提取，作为初始化内容
    @classmethod
    def setUpClass(cls) -> None:
        cls.cookie = None
        conf = configparser.ConfigParser ()
        conf.read ( '../config/config.ini' )
        cls.url = conf.get ( 'DEFAULT', 'url' )
        cls.kd = KeyDemo()

    # 测试用例
    @file_data('../data/login.yaml')
    def test_1_api_login(self, **kwargs):
        # 实例化需要的内容
        url = self.url + kwargs['path']
        # 接口的测试
        res = self.kd.post(url=url, headers=kwargs['header'], json=kwargs['data'])
        # print(res.text)
        value = self.kd.get_text(res.text, 'msg')
        # print(value)
        # self.assertEqual(first='登录成功!!!', second=value, msg='登录失败')
        self.assertEqual(first=kwargs['text'], second=value, msg='登录失败' )
        c = res.cookies
        ApiCases.cookie = requests.utils.dict_from_cookiejar(c)
        print(self.cookie)

    # @file_data('../data/catalog_search')
    # def test_2_api_catalog_search(self, **kwargs):
    #     # 将之前用例中获取的cookie进行调用，但同时又不去调用用例的执行步骤
    #     print(self.cookie)
    #     # url = self.url + kwargs['path']
    #     # headers = kwargs['headers']
    #     # headers['Cookie']=self.cookie
    #     # print(url)
    #     # res = self.kd.post(url=url, headers=headers['Cookie'], data=kwargs['data'])
    #     # value = self.kd.get_text(res.text, 'msg')
    #     # value = res.text
    #     # print(value)
    #     # #self.assertEqual(kwargs['text'], value, '查询失败')



        # def test_2_api_get_cookie(self):
        #     @file_data ( '../data/login.yaml' )
        #     # 实例化需要的内容
        #
        #     conf = configparser.ConfigParser ()
        #     conf.read ( '../config/config.ini' )
        #     kd = KeyDemo ()
        #     url = conf.get ( 'DEFAULT', 'url' ) + kwargs['path']
        #     # 接口的测试
        #     res = kd.post ( url=url, data=kwargs['data'] )
        #     print ( res.text )

# if __name__ == '__main__':
#         # unittest.main()
#         test_suite = unittest.TestSuite ()  #实例化
#         # 按类加载全部testxxx测试用例
#         test_suite.addTest(unittest.makeSuite(ApiCases))
#         fmt = '{date}_TestReport.html'.format ( date=time.strftime ( '%Y%m%d%H%M%S' ) )
#         # # 生成报告的文件名格式20180329190544_TestReport.html
#         # report_html.report ( filename=fmt, description='用例描述', report_dir='report' )
#         result = BeautifulReport(test_suite)
#         result.report( filename='repoet.html', description='登录测试', report_dir='report1')


# 管理员用户登录 — 添加题库 - 添加试题 — 添加考试 - 验证添加成功
