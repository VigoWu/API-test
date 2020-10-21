import requests
from urllib.parse import urljoin


class PublicMethod:
    def __init__(self):
        self.s = requests.session()

    def get_method(self, domain, path, payload, headers):
        '''
        get方法模板
        :param domain: 域名
        :param path: API路径
        :param payload: 接口参数
        :param headers: 请求头
        :return: 接口返回结果
        '''
        url = urljoin(domain, path)
        try:
            r = self.s.get(url=url, params=payload, headers=headers)
            return r.json()
        except Exception as e:
            print(type(e))

    def post_method(self, domain, path, payload, headers):
        '''
        post方法模板
        :param domain: 域名
        :param path: API路径
        :param payload: 接口参数
        :param headers: 请求头
        :return: 接口返回结果
        '''
        url = urljoin(domain, path)
        try:
            r = self.s.post(url=url, json=payload, headers=headers)
            return r.json()
        except Exception as e:
            print(type(e))


if __name__ == '__main__':
    print(urljoin('http://www.baidu.com', '/123/'))
    a = urljoin('http://www.baidu.com', '/123/')
    print(urljoin(a,'1'))