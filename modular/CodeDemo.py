# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: StudyTheCode
# author: "Lei Yong" 
# creation time: 2017/7/2 0002 14:56
# Email: leiyong711@163.com

import time
import json
import urllib2


def code_demo(username, password, image, typeid):
    # 验证码类型(typeid)1**0 纯数字,2**0 纯英文,3**0 英文数字混合,4**0 纯汉字,5000数字英文汉字混合
    # (*000任意长度混合,*010-*100对应1-10位组合)）

    # 参数协议分割标识
    boundary = '--%s' % hex(int(time.time() * 1000))

    # 制作协议包
    data = []
    header = {'Accept': '*/*',
              'Accept-Language': 'zh-cn',
              'Content-Type': 'multipart/form-data; boundary=%s' % hex(int(time.time() * 1000)),
              'Host': 'api.ruokuai.com'}
    data.append(boundary)
    data.append('Content-Disposition: form-data; name="username"\r\n')
    data.append(username)
    data.append(boundary)
    data.append('Content-Disposition: form-data; name="password"\r\n')
    data.append(password)
    data.append(boundary)
    data.append('Content-Disposition: form-data; name="typeid"\r\n')
    data.append(typeid)
    data.append(boundary)
    data.append('Content-Disposition: form-data; name="timeout"\r\n')
    data.append('90')
    data.append(boundary)
    data.append('Content-Disposition: form-data; name="softid"\r\n')
    data.append('84583')
    data.append(boundary)
    data.append('Content-Disposition: form-data; name="softkey"\r\n')
    data.append('7b891f29bbad4e009d473e319db4e1c0')
    data.append(boundary)
    data.append('Content-Disposition: form-data; name="image"; filename="%s"\r\n' % image)
    data.append(open(image, 'rb').read())
    data.append('%s--' % boundary)

    # 发送Post请求
    http_body = '\r\n'.join(data)
    req = urllib2.Request('http://api.ruokuai.com/create.json', headers=header)
    req.add_data(http_body)
    resp = urllib2.urlopen(req)
    # 获得结果
    qrcont = json.loads(resp.read())

    try:
        return qrcont['Result']
    except:
        return qrcont['Error']

if __name__ == '__main__':
    print code_demo('', '', '', '')  # 参数（用户名，密码，图片地址，验证码类型）
