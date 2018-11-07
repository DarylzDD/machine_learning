#! usr/bin/python
#coding=utf-8

import pandas
import urllib
#import urllib2

import tushare

class Http:
    @staticmethod
    def get(url, para):       # url like "http://192.168.81.16/cgi-bin/python_test/test.py", para like "ServiceCode=aaaa"
        params = urllib.urlencode(para)
        ret = urllib.urlopen("%s?%s"%(url, params))
        code = ret.getcode()
        ret_data = ret.read()
        return code, ret_data

    #@staticmethod
    #def post(url, data):        # url like "http://192.168.81.16/cgi-bin/python_test/test.py", data like "{'ServiceCode':'aaaa','b':'bbbbb'}"
    #    req = urllib2.Request(url=url,data=urllib.urlencode(data))
    #    res_data = urllib2.urlopen(req)
    #    res = res_data.read()
    #    return res

class Ifeng():
    @staticmethod
    def getAkdaily():
        code, res = Http.get("http://api.finance.ifeng.com/akdaily", {'code': 'sh601989', 'type': 'last'})
        res = eval(res)
        print("res: %s" % (type(res)))
        print(res)
        code, res = Http.get("http://api.finance.ifeng.com/akdaily", {'code': 'sz000858', 'type': 'last'})
        res = eval(res)
        print("res: %s" % (type(res)))
        print(res)

class Tushare():
    @staticmethod
    def test():
        tushare.set_token('4028ee0f1a5b4441c8e6b14b100e6e78ac8c510a1e1f128995c3033d1279d9fc')
        list_stock_basics = tushare.get_stock_basics()
        print("get_stock_basics list: %s" % (type(list_stock_basics)))
        print(list_stock_basics)
        print("----------------------------------------------------------")
        print("cols:")
        print(list_stock_basics.columns)
        print("----------------------------------------------------------")
        i = 0
        for row in list_stock_basics.itertuples(index=True, name='Pandas'):
            print("%s, %s" % (i, getattr(row, "name")))
            i += 1



if __name__=="__main__":
    print("start")
    # Ifeng.getAkdaily()
    Tushare.test()
