# 说明：
本工具适用于Thinkcmf任意内容包含漏洞，提供一般检测，一键上传冰蝎马，以及无回显命令执行功能。ThinkCMF是一款基于PHP+MYSQL开发的中文内容管理框架，底层采用ThinkPHP3.2.3构建。

本工具仅限安全从业者在法律法规允许的范围内使用，违规使用后果自负。

# 适用版本：
ThinkCMF X1.6.0
ThinkCMF X2.1.0
ThinkCMF X2.2.0
ThinkCMF X2.2.1
ThinkCMF X2.2.2
ThinkCMF X2.2.3

ThinkCMF源码下载地址https://gitee.com/thinkcmf/ThinkCMFX/releases

# 使用说明:
### 检测漏洞是否存在
python thinkcmf_exp.py -u http://yourURL/
![image](https://github.com/bo1349/Thinkcmf_RCE/blob/master/%E6%A3%80%E6%B5%8B%E6%BC%8F%E6%B4%9E.png)

### 上传冰蝎马
python thinkcmf_exp.py -u http://yourURL/ -p yourPassword
![image](https://github.com/bo1349/Thinkcmf_RCE/blob/master/%E4%B8%8A%E4%BC%A0%E5%86%B0%E8%9D%8E.png)
![image](https://github.com/bo1349/Thinkcmf_RCE/blob/master/%E4%B8%8A%E4%BC%A0%E6%88%90%E5%8A%9F.png)

### 无回显命令执行
python thinkcmf_exp.py -u http://yourURL/ -c yourCommand
![image](https://github.com/bo1349/Thinkcmf_RCE/blob/master/%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C.png)
![image](https://github.com/bo1349/Thinkcmf_RCE/blob/master/%E6%89%A7%E8%A1%8C%E6%88%90%E5%8A%9F.png)
