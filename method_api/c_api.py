import datetime
import time
from .public_method import PublicMethod
from urllib.parse import urljoin


def getstarttime():
    '''获取当天开始时间戳'''
    today = datetime.date.today()
    yesterday_end_time = int(time.mktime(time.strptime(str(today), '%Y-%m-%d'))) - 1
    today_start_time = yesterday_end_time + 1
    return today_start_time


def getendtime():
    '''获取当天结束时间戳'''
    # 今天日期
    today = datetime.date.today()
    # 明天时间
    tomorrow = today + datetime.timedelta(days=1)
    # 今天结束时间戳
    today_end_time = int(time.mktime(time.strptime(str(tomorrow), '%Y-%m-%d'))) - 1
    return today_end_time


HOST_C = 'http://dj01.yftest1.com/melody'  # 测试客户端地址

C_API = {
    'login': '/api/v1/memberuser/login',  # 客户端登录
    'bankTransfer': '/api/v1/recharge/bankTransfer',  # 用户网银充值
    'scTransfer': '/api/v1/recharge/scTransfer',  # 扫码支付充值
    'transferOut': '/api/v1/dsfplayer/transferOut',  # 第三方转出
    'transferIn': '/api/v1/dsfplayer/transferIn',  # 第三方转入
    'dsf_balance': '/api/v1/dsfplayer/balance',  # 获取第三方余额
    'getBalance': '/api/v1/wallet/getBalance',  # 客户端获取余额
    'getEnabledDueScAccount': '/api/v1/recharge/getEnabledDueScAccount',  # 获取可扫码账户
    'getEnabledDueBankCard': '/api/v1/recharge/getEnabledDueBankCard',  # 获取可用收款银行卡

}


class CMethod(PublicMethod):
    def __init__(self, token):
        super().__init__()
        self.host_c = HOST_C
        self.headers_c = {
            'Accept - Language': 'zh - CN, zh;q = 0.9',
            'Content - Type': 'application / json;charset = UTF - 8',
            'User-Agent': 'Mozilla/5.0 (WindowsNT 10.0; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/83.0.4103.97Safari/ 537.36'
        }

    def c_login(self, username):
        '''
        客户端登录
        :param username:
        :return:
        '''
        location = self.host_c + C_API['login']
        data = {
            "memberAccount": username,
            "password": "a123456",
            "uuid": "954f0845-d6d9-42eb-b075-cb7e09bff556"
        }
        try:
            r = self.s.post(url=location, json=data, headers=self.headers_c)
            self.headers_c['x-auth-token'] = r.headers['x-auth-token']
            print('用户{}登录'.format(username))
            print(r.json())
            # print(r.headers['x-auth-token'])
        except Exception as e:
            print(type(e))

    def getEnabledDueScAccount(self):
        result = self.post_method(self.host_c, C_API['getEnabledDueScAccount'], payload=None,
                                  headers=self.headers_c)
        print('获取可扫码账户\n', result)
        return result

    def getEnabledDueBankCard(self):
        result = self.post_method(self.host_c, C_API['getEnabledDueBankCard'], payload=None,
                                  headers=self.headers_c)
        print('获取可用收款银行卡\n', result)
        return result

    def bankTransfer(self, payload):
        result = self.post_method(self.host_c, C_API['bankTransfer'], payload=payload,
                                  headers=self.headers_c)
        print('用户银行卡充值\n', result)
        return result

    def scTransfer(self, payload):
        result = self.post_method(self.host_c, C_API['scTransfer'], payload=payload,
                                  headers=self.headers_c)
        print('用户扫码充值\n', result)
        return result

    def transferOut(self, payload):
        result = self.post_method(self.host_c, C_API['transferOut'], payload=payload,
                                  headers=self.headers_c)
        print('从第三方转出\n', result)
        return result

    def transferIn(self, payload):
        result = self.post_method(self.host_c, C_API['transferIn'], payload=payload,
                                  headers=self.headers_c)
        print('从第三方转入\n', result)
        return result

    def getBalance(self):
        result = self.get_method(self.host_c, C_API['getBalance'], payload=None,
                                 headers=self.headers_c)
        print('获取余额\n', result)
        return result

    def dsf_balance(self):
        result = self.get_method(self.host_c, C_API['dsf_balance'], payload=None,
                                 headers=self.headers_c)
        print('获取第三方余额\n', result)
        return result
