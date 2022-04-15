import os
import pytest
import datetime
from pyvirtualdisplay import Display

display = Display(visible=0, size=(800, 600))
display.start()

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
    report_html_dir = os.path.join(cwd, f'docs')
    pytest.main(['-s','./Test/TestCase/','--alluredir',report_dir])
    print(f'报告路径：https://lisa1213001.github.io/dodo-test  (需要等待一段时间报告才会生成)')
    os.system(f'allure generate {report_dir} -o {report_html_dir} --clean')
    display.stop()
