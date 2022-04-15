import os
import pytest
import datetime

"""
执行测试用例并生成、并查看报告  主入口
如果使用的是Pycharm 需要在Setting-Tools-Testing-Default test runner改为Unittests，不然无法生成报告
我也不晓得为啥，bug吧，生成的报告和直接用终端指定的pytest的一样，没啥问题
"""


#执行./Test/TestCase/下的所有测试用例 test_*.py 可以手动修改选定只执行那些测试用例
if __name__ == '__main__':
    now=datetime.datetime.now().strftime('%Y%m%d%H%M%S') 
    cwd = os.getcwd()
    report_dir = os.path.join(cwd, f'Report/{now}')
    pytest.main(['-s','./Test/TestCase/','--alluredir',report_dir])
    print(f'报告路径：https://github.com/lisa1213001/dodo-test/tree/main/Report/{now}')
    os.system(f'allure generate {report_dir} -o {report_dir} --clean')