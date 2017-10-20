# zabbix_weixin_kapian

### 环境要求

#### python3 zabbix 3.4 微信企业号
##### 我刚刚学习python没多久，写的不是很好大神勿喷n(*≧▽≦*)n
个人博客
https://www.aityp.com

---
zabbix 从3.4版本后开始支持问题确认通知，效果如下

![image](https://typ.oss-cn-shanghai.aliyuncs.com/markdown/2017/10/zabbix_weixin_1.jpg)

## 使用方法

**pull代码**
```
yum install git -y
git clone  https://github.com/BigbigY/python-script.git
```
**更改脚本参数,需要把这三个参数改成你微信企业号的**

参数 | 说明
---|---
Toparty | 企业号部门id
CropID | 微信开发者CropID
Secret | 微信开发者Secret


![image](https://typ.oss-cn-shanghai.aliyuncs.com/markdown/2017/10/11.png)

## 注意
**开头环境选择，请设置成你自己的python解释器版本，因为我电脑上面有多个环境为了区分才写成这样**

![image](https://typ.oss-cn-shanghai.aliyuncs.com/markdown/2017/10/12.png)

**把脚本放到zabbix scripts下面，执行下面命令**
```
chown zabbix:zabbix zabbix_weixin_kapian.py
chmod +x zabbix_weixin_kapian.py
touch /tmp/weixin_zabbix.log
chown zabbix:zabbix /tmp/weixin_zabbix.log
```

**首先我们添加一个报警脚本**

![image](https://typ.oss-cn-shanghai.aliyuncs.com/markdown/2017/10/1.png)

**名称随便写这里我写'微信卡片通知'   
脚本名称写你放到服务器目录的名称**

![image](https://typ.oss-cn-shanghai.aliyuncs.com/markdown/2017/10/2.png)

**在用户里面添加报警媒介**


![image](https://typ.oss-cn-shanghai.aliyuncs.com/markdown/2017/10/3.png)

**类型:你刚才新建的脚本名称
收件人:企业微信用户名**
![image](https://typ.oss-cn-shanghai.aliyuncs.com/markdown/2017/10/4.png)
**配置---动作---编辑你的报警脚本---Acknowledgement operations   
默认收件人不用动   
默认信息可以使用我的模板**   
```
用户:{USER.FULLNAME} 
时间:{ACK.DATE} {ACK.TIME} 
确认了这个问题,信息如下:
{ACK.MESSAGE}
问题服务器IP:{HOSTNAME1}
问题ID:{EVENT.ID}
当前的问题是: {TRIGGER.NAME}
```
**然后添加一个操作**

![image](https://typ.oss-cn-shanghai.aliyuncs.com/markdown/2017/10/5.png)

**添加操作配置如下**

![image](https://typ.oss-cn-shanghai.aliyuncs.com/markdown/2017/10/6.png)

**我们停止测试服务器客户端,点击确认问题**

![image](https://typ.oss-cn-shanghai.aliyuncs.com/markdown/2017/10/8.png)

**确认随便写**

![image](https://typ.oss-cn-shanghai.aliyuncs.com/markdown/2017/10/9.png)

**企业号成功收到消息**

![image](https://typ.oss-cn-shanghai.aliyuncs.com/markdown/2017/10/10.png)


### LOG
log目录在`/tmp/weixin_zabbix.log`
在这里可以看到每条消息的发送情况
![image](https://typ.oss-cn-shanghai.aliyuncs.com/markdown/2017/10/13.png)

### QQ:1500698928
### 个人微信
![image](https://typ.oss-cn-shanghai.aliyuncs.com/markdown/2017/10/14.jpg)

### 问题调试方法
如果你的微信收不到消息可以使用以下方法进行调试
命令行调试脚本
```
python3 zabbix_weixin_kaping.py 你的企业号用户名 1 测试
```
查看日志输出
token获取失败，请检查key等配置信息
![image](https://typ.oss-cn-shanghai.aliyuncs.com/markdown/2017/10/15.png)