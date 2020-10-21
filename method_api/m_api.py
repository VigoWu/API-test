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


# HOST_M = 'http://10.50.40.216:8080'  # 测试后台地址       http://admin.yftest1.com      xf02地址：http://admin.yingfa10.com
HOST_M = 'http://admin.yingfa10.com-admin'  # 测试后台地址
M_API = {
    'adduser': '/member/memberuser/save',  # 后台新增用户
    'updateDamavalue': '/member/memberaddminusbet/updateDamaValue',  # 更新用户打码量
    'Rechargelist': '/member/memberrechargerecord/list',  # 后台充值列表
    'lockorder': '/member/memberrechargerecord/lockOrder/',  # 锁定订单
    'deal': '/member/memberrechargerecord/deal',  # 审核充值订单
    'Bchangelist': '/member/lotteryaccounchange/list',  # 会员账变列表
    'Dmchangelist': '/member/memberdamachangerecord/list',  # 打码量变化列表
    'wx_config_save': '/wx/wxafruleconfig/save',  # 新增配置
    'wx_config_update': '/wx/wxafruleconfig/update',  # 修改配置
    'wx_config_delete': '/wx/wxafruleconfig/delete',  # 删除配置
    'wx_config_list': '/wx/wxafruleconfig/list',  # 查询配置列表配置
    'wx_config_info': '/wx/wxafruleconfig/info/',  # 根据configId查询配置
    'add_quick_income': '/pay/adminduescaccount/save',  # 新增快速入款通道
    'add_bank_income': '/pay/adminduebankcard/save',  # 新增银行卡入款通道
    'bankcard_list': '/pay/adminduebankcard/list',  # 收款银行卡列表
    'scan_list': '/pay/adminduescaccount/list',  # 收款码列表

}

class MMethod(PublicMethod):
    def __init__(self, token):
        super().__init__()
        self.host_m = HOST_M
        self.headers_m = {
            'Accept - Language': 'zh - CN, zh;q = 0.9',
            'Content - Type': 'application / json;charset = UTF - 8',
            # 'Cookie': Cookie,
            'token': token,
            'User-Agent': 'Mozilla/5.0 (WindowsNT 10.0; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/83.0.4103.97Safari/ 537.36'
        }

    def add_quick_income(self, payload):
        result = self.post_method(self.host_m, M_API['add_quick_income'], payload, self.headers_m)
        print('后台新增快捷入款通道\n', result)
        return result

    def add_bank_income(self, payload):
        result = self.post_method(self.host_m, M_API['add_bank_income'], payload, self.headers_m)
        print('后台新增银行入款通道\n', result)
        return result

    def wx_config_info(self, configId):
        result = self.post_method(urljoin(self.host_m, str(configId)), M_API['wx_config_info'], payload=None,
                                  headers=self.headers_m)
        print('后台获取加好友配置信息\n', result)
        return result

    def wx_config_list(self, payload):
        result = self.get_method(self.host_m, M_API['wx_config_list'], payload=payload, headers=self.headers_m)
        print('后台获取加好友配置列表\n', result)
        return result

    def wx_config_delete(self, payload):
        result = self.post_method(self.host_m, M_API['wx_config_delete'], payload=payload,
                                  headers=self.headers_m)
        print('后台删除添加好友配置\n', result)
        return result

    def wx_config_update(self, payload):

        result = self.post_method(self.host_m, M_API['wx_config_update'], payload=payload,
                                  headers=self.headers_m)
        print('后台修改添加好友配置\n', result)
        return result

    def wx_config_save(self, payload):

        result = self.post_method(self.host_m, M_API['wx_config_save'], payload=payload,
                                  headers=self.headers_m)
        print('后台新增添加好友配置\n', result)
        return result

    def adduser(self, payload):
        # '''
        # 后台新增用户
        #         payload 格式{
        #   "chessProxyRpRate": 0,
        #   "elegameProxyRpRate": 0,
        #   "email": "string",
        #   "isEnable": 0,
        #   "memberAccount": "string",
        #   "memberLevelId": 0,
        #   "memberPassword": "string",
        #   "memberQq": "string",
        #   "memberType": 0,
        #   "memberWx": "string",
        #   "mobile": "string",
        #   "proxyMemberAccount": "string",
        #   "realName": "string",
        #   "realmanProxyRpRate": 0,
        #   "returnPointRate": 0,
        #   "sportsProxyRpRate": 0
        # }
        # '''
        # location = self.host_m + M_API['adduser']
        # # data = {
        # #     'chessProxyRpRate': '0.14',
        # #     'confirmMemberPassword': 'a123456',
        # #     'elegameProxyRpRate': '0.14',
        # #     'isEnable': '1',
        # #     'memberAccount': memberAccount,
        # #     'memberLevelId': memberLevelId,
        # #     'memberPassword': "a123456",
        # #     'memberType': memberType,
        # #     'realmanProxyRpRate': '0.14',
        # #     'returnPointRate': '7.5',
        # #     'sportsProxyRpRate': '0.14',
        # # }
        # try:
        #     r = self.s.post(url=location, json=payload, headers=self.headers_m)
        #     print('后台新增用户')
        #     print(r.json())
        # except Exception as e:
        #     print(type(e))
        result = self.post_method(self.host_m, M_API['adduser'], payload=payload,
                                  headers=self.headers_m)
        print('后台新增用户\n', result)
        return result

    def updateDamavalue(self, payload):
        # '''
        # 更新用户打码量
        # :param memberAccount:
        # :return:
        # '''
        # location = self.host_m + M_API['updateDamavalue']
        # data = {
        #     'memberAccount': memberAccount,
        #     'operationBetNum': '3000',
        #     'operationReason': 'test',
        #     'operationType': '3',
        #
        # }
        # try:
        #     r = self.s.post(url=location, json=data, headers=self.headers_m)
        #     print('更新用户{}打码量'.format(memberAccount))
        #     print(r.json())
        # except Exception as e:
        #     print(type(e))
        result = self.post_method(self.host_m, M_API['updateDamavalue'], payload=payload,
                                  headers=self.headers_m)
        print('更新用户打码量\n', result)
        return result

    def get_Rechargelist(self,payload):
        # '''
        # 获取当天充值待审核订单
        # :return:
        # '''
        # location = self.host_m + M_API['Rechargelist']
        # params = {
        #     'page': '1',
        #     'limit': '100',
        #     'startTime': str(getstarttime()),
        #     'endTime': str(getendtime()),
        #     'rechargeType': '2',
        #     'operationType': '2',
        #     'isQueryRegTime': '0'
        #
        # }
        # try:
        #     r = self.s.get(url=location, params=params, headers=self.headers_m)
        #     print('获取到天充值订单列表')
        #     print(r.json()['page']['list'])
        #     return r.json()['page']['list']
        # except Exception as e:
        #     print(type(e))
        result = self.get_method(self.host_m, M_API['Rechargelist'], payload=payload, headers=self.headers_m)
        print('后台获取充值订单列表\n', result)
        return result

    def lockOrder(self, orderid):
        # '''
        # 锁定用户充值订单
        # :param orderid:
        # :return:
        # '''
        # location = self.host_m + M_API['lockorder'] + str(orderid)
        # try:
        #     r = self.s.post(url=location, headers=self.headers_m)
        #     print('锁定订单')
        #     print(r.json())
        # except Exception as e:
        #     print(type(e))
        result = self.post_method(urljoin(self.host_m, str(orderid)), M_API['lockorder'], payload=None,
                                  headers=self.headers_m)
        print('锁定用户充值订单\n', result)
        return result

    def deal(self, payload):
        # '''
        # 审核订单
        # :param orderid:
        # :return:
        # '''
        # location = self.host_m + M_API['deal']
        # params = {
        #     'amount': '10000',
        #     'isProcess': '1',
        #     'rechargeRecordId': str(orderid),
        #     'remark': None,
        #
        # }
        # # try:
        # r = self.s.post(url=location, json=params, headers=self.headers_m)
        # print('审核订单充值')
        # print(r.json())
        # # except Exception as e:
        # #     print(type(e))
        result = self.get_method(self.host_m, M_API['deal'], payload=payload, headers=self.headers_m)
        print('后台获取充值订单列表\n', result)
        return result

    def get_Bchangelist(self, payload):
        # '''
        # 获取用户账变记录
        # :param memberAccount:
        # :return:
        # '''
        # location = self.host_m + M_API['Bchangelist']
        # params = {
        #     'page': '1',
        #     'limit': '100',
        #     'startTime': str(getstarttime()),
        #     'endTime': str(getendtime()),
        #     'memberAccount': memberAccount,
        # }
        # try:
        #     r = self.s.get(url=location, params=params, headers=self.headers_m)
        #     print('获取到当天账变列表')
        #     print(r.json()['page']['list'])
        #     return r.json()['page']['list']
        # except Exception as e:
        #     print(type(e))
        result = self.get_method(self.host_m, M_API['Bchangelist'], payload=payload, headers=self.headers_m)
        print('后台获取充值订单列表\n', result)
        return result

    def get_Dmchangelist(self, payload):
        # '''
        # 获取打码量变化列表
        # :param memberAccount:
        # :return:
        # '''
        # location = self.host_m + M_API['Dmchangelist']
        # params = {
        #     'page': '1',
        #     'limit': '100',
        #     'startTime': str(getstarttime()),
        #     'endTime': str(getendtime()),
        #     'memberAccount': memberAccount,
        # }
        # try:
        #     r = self.s.get(url=location, params=params, headers=self.headers_m)
        #     print('获取到当天打码量变动列表')
        #     print(r.json()['page']['list'])
        #     return r.json()['page']['list']
        # except Exception as e:
        #     print(type(e))
        result = self.get_method(self.host_m, M_API['Dmchangelist'], payload=payload, headers=self.headers_m)
        print('后台获取打码量变动列表\n', result)
        return result


if __name__ == '__main__':
    key = {
        'Cookie': 'JSESSIONID=0a754b73-2abc-4e53-b727-d1b7b1e1d09c; token=9d098d8d54cd4c58d278eb71f32b6ca0',
        'token': 'fdb3127c16578ad9b19f75f813a58398',
    }
    levellist = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '15', '16', '18']
    accounttypelist = ['2']
    # n = 0
    method = MMethod(token=key['token'])
    # for isEnableAddFriend in range(2):
    #     for isEnableAddFriendDirectLower in range(2):
    #         for isEnableAddFriendDirectProxy in range(2):
    #             for isEnableAddFriendLower in range(2):
    #                 for isEnableAddFriendProxy in range(2):
    #                     for isFreedomAddFriend in range(2):
    #                         print(isEnableAddFriend, isEnableAddFriendDirectLower, isEnableAddFriendDirectProxy,
    #                               isEnableAddFriendLower, isEnableAddFriendProxy, isFreedomAddFriend)
    #                         method.wx_config_update(configId=4, isEnableAddFriend=isEnableAddFriend,
    #                                                 isEnableAddFriendDirectLower=isEnableAddFriendDirectLower,
    #                                                 isEnableAddFriendDirectProxy=isEnableAddFriendDirectProxy,
    #                                                 isEnableAddFriendLower=isEnableAddFriendLower,
    #                                                 isEnableAddFriendProxy=isEnableAddFriendProxy,
    #                                                 isFreedomAddFriend=isFreedomAddFriend,
    #                                                 memberAccount='tester1')
    #
    # method.wx_config_save(1, 1, 1, 1, 1, 1, 1, 'tester7')
    # method.wx_config_update(346, 1, 1, 1, 1, 1, 1, 'tester6')
    # method.wx_config_delete(1)
    # method.wx_config_list(1, 10)
    # method.wx_config_info(17)

    # 创建玩家和代理用户
    # for level in range(10):
    #     for accounttype in accounttypelist:
    #         username = 'tester01' + str(level)
    #         method.adduser(username, level, accounttype)
    #         with open('account.txt', 'a+') as f:
    #             f.write(username+'\n')
    # n += 1
    # # 登录客户端，对每个玩家进行充值申请
    # with open('account.txt', 'r') as f:
    #     for user in f.readlines():
    #         loginuser = user.strip()
    #         method.c_login(loginuser)
    #         method.bankTransfer()
    # #
    # rechargelist = method.get_Rechargelist()
    # # 审核充值订单
    # # print(type(rechargelist[0]['status']))
    # for recharge in rechargelist:
    #     if recharge['status'] == 1:
    #         # method.lockOrder(str(recharge['rechargeRecordId']))
    #         method.deal(recharge['rechargeRecordId'])

    # 给用户降低体现所需打码量
    # with open('account.txt', 'r') as f:
    #     for user in f.readlines():
    #         memberAccount = user.strip()
    #         method.updateDamavalue(memberAccount)
