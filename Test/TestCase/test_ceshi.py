import allure

@allure.feature("ceshi")
class TestCeshi:

    def setupclass(self):
        print("测试开始了")

    def teardownclas(self):
        print("测试结束了")

    @allure.story("这是测试1==1")
    def test_ceshi_001(self):
        print("这是测试用例1")
        assert 1 == 1
    @allure.story("这是测试1<1失败的情况")
    def test_ceshi_002(self):
        print("这是测试用例1")
        assert 1 < 1