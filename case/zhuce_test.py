# -*- coding: utf-8 -*-
# @Author  : shige
from bussiness.functionPublic import sign_in_tes
import unittest,time,os,ddt
from util import log
from selenium import webdriver
path=os.getcwd()
from util.gettestdata import fetch_test_cases
case_path=path+'\\data\\case.xlsx'
casedata=fetch_test_cases(case_path,1)
@ddt.ddt
class Testsign_in(unittest.TestCase):
    def setUp(self):
        self.logs = log.log_message()
        self.derve=webdriver.Firefox()
        self.sign_in_fun=sign_in_tes(self.derve)
    @ddt.data(*casedata)
    def test_sign_in_1(self,casedata):
        self.name=casedata['username']
        self.password=casedata['password']
        self.passwordque=casedata['nima2']
        self.shoujihao=casedata['shoujihao']
        self.youxiang=casedata['youxiang']
        self.suc=casedata['suc']
        self.assert_vale=casedata['assert_vale']
        self.re_data=self.sign_in_fun.sign_in(self.name,self.password,self.passwordque,self.shoujihao,self.youxiang,self.suc)
        self.derve.get_screenshot_as_file(path+'\\resultpang\\%s.png'%casedata[id])
        self.logs.info_log("input:name:%s password:%s,passwordque:%s,shoujihao:%s,youxiang:%s ,assert:%s"%(self.name,self.password,self.passwordque,self.shoujihao,self.youxiang,self.assert_vale))
        time.sleep(1)
        self.assertEqual(self.re_data, self.assert_vale)
    def tearDown(self):
        self.derve.quit()