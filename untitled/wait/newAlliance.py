# -*- encoding=utf8 -*-
__author__ = "admin"

from airtest.core.api import *

auto_setup(__file__)

from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()

import re

#-----创建联盟----
#-----创建联盟，联盟名为空---------
shell("input tap 673.5 1002")
poco("UICamera").offspring("AllianceCreateUI(Clone)").child("BtnCreate").click()
assert poco("TopMessageBar(Clone)").child("Panel").child("Text").get_text() == "请输入联盟名字","联盟名修改为空"
poco("UICamera").offspring("AllianceCreateUI(Clone)").child("BackBtn").click()

#-----创建联盟，字符过短----------
shell("input tap 673.5 1002")
poco("UICamera").offspring("AllianceCreateUI(Clone)").child("NameInputField").wait(3).set_text('11111')
sleep(2)
poco("UICamera").offspring("AllianceCreateUI(Clone)").child("BtnCreate").click()
assert poco("TopMessageBar(Clone)").child("Panel").child("Text").get_text() == "字符太短","联盟名修改过短"
poco("UICamera").offspring("AllianceCreateUI(Clone)").child("BackBtn").click()

#-----创建联盟，字符过长----------
shell("input tap 673.5 1002")
poco("UICamera").offspring("AllianceCreateUI(Clone)").child("NameInputField").wait(3).set_text('啦啦啦啦啦啦啦0')
sleep(2)
poco("UICamera").offspring("AllianceCreateUI(Clone)").child("BtnCreate").click()
assert poco("TopMessageBar(Clone)").child("Panel").child("Text").get_text() == "字符太长","联盟名修改过长"
poco("UICamera").offspring("AllianceCreateUI(Clone)").child("BackBtn").click()

#-----创建联盟，特殊字符----------
shell("input tap 673.5 1002")
poco("UICamera").offspring("AllianceCreateUI(Clone)").child("NameInputField").wait(3).set_text('1@#（就这样')
sleep(2)
poco("UICamera").offspring("AllianceCreateUI(Clone)").child("BtnCreate").click()
assert poco("TopMessageBar(Clone)").child("Panel").child("Text").get_text() == "输入内容包含特殊字符","联盟名修改包含特殊字符"
poco("UICamera").offspring("AllianceCreateUI(Clone)").child("BackBtn").click()

#-----创建联盟，敏感字----------
shell("input tap 673.5 1002")
poco("UICamera").offspring("AllianceCreateUI(Clone)").child("NameInputField").wait(3).set_text('习大大')
sleep(2)
poco("UICamera").offspring("AllianceCreateUI(Clone)").child("BtnCreate").click()
assert poco("TopMessageBar(Clone)").child("Panel").child("Text").get_text() == "输入内容包含敏感字符","联盟名修改包含敏感字"
poco("UICamera").offspring("AllianceCreateUI(Clone)").child("BackBtn").click()

#-----创建联盟，和其他联盟名重复（重复用的联盟名是23232323）----------
shell("input tap 673.5 1002")
poco("UICamera").offspring("AllianceCreateUI(Clone)").child("NameInputField").wait(3).set_text('23232323')
sleep(2)
poco("UICamera").offspring("AllianceCreateUI(Clone)").child("BtnCreate").click()
assert poco("TopMessageBar(Clone)").child("Panel").child("Text").get_text() == "此联盟名已被占用","联盟名改成了和其他联盟名一样"
poco("UICamera").offspring("AllianceCreateUI(Clone)").child("BackBtn").click()

#-----创建联盟，正常，成功（要先用sql修改可能存在的即将修改的联盟名。且要确保宝石充足）----------
# sql: UPDATE t_alliance set alliance_name = '123123###' WHERE alliance_name = '999哦哦999';
shell("input tap 673.5 1002")
poco("UICamera").offspring("AllianceCreateUI(Clone)").child("NameInputField").wait(3).set_text('999哦哦999')
sleep(2)
poco("UICamera").offspring("AllianceCreateUI(Clone)").child("BtnCreate").click()
allianceName_now = poco("AllianceUI(Clone)").child("BackBtn").child("label").wait(3).get_text()
allianceName_now = re.match( r'(.*)联盟', allianceName_now).group(1)
assert allianceName_now == '999哦哦999','修改后的联盟名和修改时输入的联盟名不一致'
poco("UICamera").offspring("AllianceMainUI(Clone)").child("Top").child("btnConfig").click()
poco("PopupCamera").offspring("AllianceMemberTabWindow(Clone)").child("BtnExit").wait(3).click()
poco("PopupCamera").offspring("Level2").child("Alert(Clone)").child("BtnOK").wait(3).click()
assert poco("TopMessageBar(Clone)").child("Panel").child("Text").get_text() == "你已经退出联盟","退盟失败"