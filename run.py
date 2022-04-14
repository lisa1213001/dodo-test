import os
import pytest

"""
执行测试用例并生成、并查看报告  主入口
如果使用的是Pycharm 需要在Setting-Tools-Testing-Default test runner改为Unittests，不然无法生成报告
我也不晓得为啥，bug吧，生成的报告和直接用终端指定的pytest的一样，没啥问题
"""


#执行./Test/TestCase/下的所有测试用例 test_*.py 可以手动修改选定只执行那些测试用例
if __name__ == '__main__':
    pytest.main(['-s','./Test/TestCase/','--alluredir','./Report/allure_report'])
    os.system('allure serve ./Report/allure_report')