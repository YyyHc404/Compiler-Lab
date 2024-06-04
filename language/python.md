## ctypes python内置库，调用动态链接库，操作C
- cdll 用于加载使用标准的 cdecl 调用约定导出函数的库。这意味着函数参数从右向左入栈，调用者负责清理堆栈。
- windll 用于加载使用 stdcall 调用约定导出函数的库。在 stdcall 调用约定中，函数参数也是从右向左入栈，但是由被调用者负责清理堆栈，而不是调用者。
-  oledll 也使用 stdcall 调用约定，并假定函数返回 Windows HRESULT 错误代码。 当函数调用失败时会使用错误代码自动引发 OSError 异常。
- 在 Linux 中，要求指定文件名 包括 扩展名来加载库，因此不能使用属性访问的方式来加载库。 应当使用 dll 加载器的 LoadLibrary() 
- 会同时导出同一个函数的 ANSI 版本和 UNICODE 版本。
- 有时候，dlls的导出的函数名不符合 Python 的标识符规范，比如 "??2@YAPAXI@Z"。此时，你必须使用 getattr() 方法来获得该函数。
- ctypes 使用 win32 结构化异常处理来防止由于在调用函数时使用非法参数导致的程序崩溃。

- (type * n)()语法可以创建一个包含n个type类型对象的数组
----
format 将字符串转为二进制
ord 将字符转为ascll码
----
## python 隔离环境 venv
python3 自带该模块
python -m venv ENV_DIR  

*环境使用*:
vevn:
- 激活:script中的active
- 退出环境:deactive
- 删除环境: 删除整个目录即可

conda:
- conda create -n your_env_name python=x.x
- activate your_env_name
- deactivate env_name
- 删除虚拟环境: conda remove -n your_env_name --all
- 删除某个环境的包: conda remove --name $your_env_name  $package_name 
- 环境中安装包 conda install -n your_env_name [package]

----
- wheel 是 Python 的一个二进制软件包格式，用于在安装时更快地安装软件包


--- 
## locust 
#### 约定
*配置文件*:
--config  
自动查找默认名:
~/.locust.conf./locust.conf./pyproject.toml 

*测试脚本文件*:
-f   多个测试脚本用 "," feng
自动查找默认名:
- locustfile1.py
- locustfile2.py
- more_files/locustfile3.py 

#### User类:
- 用户类表示系统的一种用户/方案
- *weight* =3  生成数量
- weight 固定生成数量，权重属性将被忽略；这些用户是在任何常规的、加权的用户之前产生的
- *wait_time*：
    每次任务执行后引入延迟
    - between（arg1,arg2）: 等待arg1~arg2之间的随机时间

    监控运行时间:
    - constant_throughput(X):每秒执行的任务运行数  运行次数=X * 用户数 ；相当于每个task 分配多少时间片
    - constant_pacing(X):每X执行一次 
    如果任务执行超过指定的wait_time，则在开始下一个任务之前等待时间将为0。
    可以直接在类上声明您自己的 wait_time 方法。返回一个int

- *environment*：用户正在其中运行的引用。使用它与环境或其runner包含的环境进行交互 例如self.environment.runner.quit()  停止运行程序


- *on_start* 和 on_stop 在开始运行/结束时将调用其方法

- *tasks*[{Task:int}或[task]]字典，包含一个或多个函数(任务)随机选择一个任务  int  发生概率比率；使用random.choice()从列表中选择一个

- *HttpSession*：client的一个子类；将请求结果报告给Locust（成功/失败、响应时间、响应长度、名称）和requests.Session一样保留cookie

添加的主要是将请求结果报告给Locust
#### 项目结构
- 项目根目录
    - common/
        - __init__.py
        - auth.py
        - config.py
    - locustfile.py
    - requirements.txt
---
*选项*:
- --web-port: PORT指定locust运行的端口，默认时8089，
- --web-host 运行的IP
- --host HOST指定被测试的域名或ip地址及端口，覆盖脚本中的请求url

- --tag 选择要执行的任务
添加类名只当使用哪些类
---



---
*API*:


 - client:
    - get(url,name):name 该测试属于哪个组，因为该框架是根据url进行分组的
    - post(url,json:字典)
    - rename_request 定义组
    返回response:
        - json()转为json键值对
        - text 返回的内容
        - elapsed.total_seconds 响应时间
        - failure 主动返回错误消息
        - 
-
*注释*:
- task(power) power是该任务的优先级，优先级越高越先执行

- tag 任务的标签
- @events.test_start[stop].add_listener   负载测试开始或停止时运行某些代码
---

相关知识:
- greenlet 微线程或协程


----
官方文档:
https://docs.locust.io/en/stable/quickstart.html