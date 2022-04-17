# UI自动化测试框架

使用pytest、selenium的自动化测试框架，使用allure生成测试报告。


## 安装运行

### 克隆项目

```bash
git clone https://github.com/lisa1213001/dodo-test.git
```

### 安装依赖

Python使用3.x的版本，依赖的安装：

```bash
pip install pytest PyYAML selenium allure-pytest -i http://mirrors.aliyun.com/pypi/simple/
```

框架使用allure生成测试报告，需要安装allure和java环境，步骤如下：


1. allure运行需要java支持，首先安装java环境。安装时需要选择将java添加到path路径中。安装后在控制台使用java -version 查看java是否安装。`https://www.java.com/zh-CN/download/`。

2. 从GitHub上下载最新的安装包，`https://github.com/allure-framework/allure2/releases`。

    [![f87afecb464ec6d8250223344940e0e0.jpg](https://image.ppzxxz.xyz/images/2022/04/12/f87afecb464ec6d8250223344940e0e0.jpg)](https://image.ppzxxz.xyz/image/6xn)

3. 将安装包解压到顺眼的目录，然后把bin目录添加到系统的环境变量中。不加到环境变量也行，在执行的时候切换到allure.bat的路径下执行应该也可。

    [![667620cb98b1d5c70ba0b60f6bc88394.jpg](https://image.ppzxxz.xyz/images/2022/04/12/667620cb98b1d5c70ba0b60f6bc88394.jpg)](https://image.ppzxxz.xyz/image/Agi)

4. 安装pytest-allure插件，已经安装了就不用安装。

    ```bash
    pip install allure-pytest -i http://mirrors.aliyun.com/pypi/simple/
    ```



### 运行测试

```bash
python run.py
```

---

## 如何使用

### 项目结构

项目的结构如下，需要添加内容时，可往对应的结构上添加。

```bash
├── Base        # 扩展selenium的操作方法，例如封装元素查找等
├── Common      # 常用的工具方法，例如csv文件解析、yml文件解析、钱包操作等
├── Config      # 配置文件，项目的配置和三方资源放这儿
├── Data        # 测试用到的数据
├── Report      # 测试报告生产目录
├── Test        # 测试用例文件
    ├── PageElement       # 页面元素对象层，每个页面上相关的元素封装成一个文件，文件名格式"<页面名>_element.py"
    ├── PageOperate       # 页面元素操作层，每个页面上相关的业务逻辑封装成一个文件，文件名格式"<页面名>_page.py"
    └── TestCase          # 测试用例文件，文件名格式"test_<要测试的内容>.py"
└── run.py      # 程序主入口文件
```

### 配置文件

目前项目的配置文件有两个：

- Config/dodoex.yml:

    用于存放各个测试用例的页面地址

    ```yml
    website:
        url: <测试URL>
    ```

- Config/wallet.yml:
    
    存放钱包配置

    ```yml
    metamask:
        address: <账户地址>
        mnemonic: <账户助记词>
        password: <metamask密码>
    ```

### 编写测试用例和执行测试


下面简单描述下编写测试用例的步骤：

1. 首先编写该测试用例涉及到的页面元素和页面元素操作，这两类分别存放在 Test/PageElement 和 Test/PageOperate 目录下。
      - Test/PageElement：页面元素对象层，<页面名>_element.py
      - Test/PageOperate：页面元素操作层，<页面名>_page.py
   可参考项目中的 Test/PageElement/swap_element.py 和 Test/PageOperate/swap_page.py 文件。

2. 编写测试用例文件，测试用例基于pytest框架，存放在 Test/TestCase 目录下，命名格式为 test_*.py。每个测试用例有一个测试用例类，基本格式为：
   ```python
   class TestSwap:
    def setup_class(self):
        # 测试用例开始时需要执行的操作，启动浏览器打开页面等
        #实例化一个启动参数对象
        chrome_options = Options()
        #添加小狐狸插件
        chrome_options.add_extension(extension_path)
        #防止浏览器闪退
        chrome_options.add_experimental_option("detach",True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        dodoex_url = parse_yaml('dodoex.yml','website')['url']
        self.driver.get(dodoex_url)

        WalletOperate().connectWallet(self.driver)
        WalletOperate().changeMetamaskNetwork(self.driver)


    def teardown_class(self):
        # 测试用例结束时需要执行的操作
        pass
    
    def test_*(self):
        # 测试方法，test_*的格式
        pass
   ```
3. 编写好测试用例后，在项目根目录使用`python run.py`执行所有的测试用例并生成报告，报告生成在 Report/allure_report 目录下。生产报告后，框架会启动http服务，并自动打开浏览器查看报告。

---

## 项目计划

- [x] UI自动化测试
- [x] allure测试报告
- [x] 自动连接metamask
- [ ] 待续...

---

## Q&A

1. 小狐狸插件是如何加载的？
    
    小狐狸插件在 Config/extension_metamask.crx，测试用例启动时，会通过浏览器加载该插件。框架封装了插件的常用操作，可以在 Common/wallet_operate.py 中查看。

2. 如何向测试用例中传数据？
    
    在我们测试时，数据相关的内容（例如十多个代币的信息）不推荐直接写到测试用例中的，而是通过 pytest 的参数化实现。对于数据内容，以 csv 的格式将数据放到 Data 文件夹，之后在测试用例中读取，并通过 pytest.mark.parametrize 传给测试方法。可参考 test_swap 中的使用：
    
    ```python
    import pytest
    from Common.parse_csv import parse_csv

    data = parse_csv('./Data/test_001_swap.csv')

    class TestSwap:
        # ...
        @pytest.mark.parametrize(("token1","amount1","token2"),data)
        def test_swap(self,token1,amount1,token2):
            # ...
    ```

