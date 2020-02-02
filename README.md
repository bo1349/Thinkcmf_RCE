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

### 显示帮助

python thinkcmf_exp.py -h 

### 检测漏洞是否存在

python thinkcmf_exp.py -u http://yourURL/

![](C:\Users\85793\Music\漏洞测试工具\ThinkCMF任意内容包含\检测漏洞.png)

### 上传冰蝎马

python thinkcmf_exp.py -u http://yourURL/ -p yourPassword

![上传冰蝎](C:\Users\85793\Music\漏洞测试工具\ThinkCMF任意内容包含\上传冰蝎.png)

<img src="C:\Users\85793\Music\漏洞测试工具\ThinkCMF任意内容包含\上传成功.png" alt="上传成功" style="zoom:50%;" />

### 无回显命令执行

python thinkcmf_exp.py -u http://yourURL/ -c yourCommand

![命令执行](C:\Users\85793\Music\漏洞测试工具\ThinkCMF任意内容包含\命令执行.png)

<img src="C:\Users\85793\Music\漏洞测试工具\ThinkCMF任意内容包含\执行成功.png" alt="执行成功" style="zoom:50%;" />