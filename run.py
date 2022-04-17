import os
import pytest
import datetime
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--githubaction',  dest='githubaction', action='store_true', default=False)
parser.parse_args() 
args = parser.parse_args()
in_githubaction = args.githubaction

# 虚拟屏幕
display = None
def start_virtualdisplay_ifneeded():
    if in_githubaction:
        from pyvirtualdisplay import Display
        display = Display(visible=0, size=(1960, 1080))
        display.start()
def stop_virtualdisplay_ifneeded():
    if display != None:
        display.stop()



"""
执行测试用例并生成、并查看报告  主入口
如果使用的是Pycharm 需要在Setting-Tools-Testing-Default test runner改为Unittests，不然无法生成报告
我也不晓得为啥，bug吧，生成的报告和直接用终端指定的pytest的一样，没啥问题
"""


#执行./Test/TestCase/下的所有测试用例 test_*.py 可以手动修改选定只执行那些测试用例
if __name__ == '__main__':
    #本地不加载虚拟屏幕
    start_virtualdisplay_ifneeded()
    now=datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    cwd = os.getcwd()
    report_dir = os.path.join(cwd, f'Report/{now}')
    report_html_dir = os.path.join(cwd, f'docs/{now}')
    pytest.main(['-s','./Test/TestCase/','--alluredir',report_dir])
    os.system(f'allure generate {report_dir} -o {report_html_dir} --clean')
    if in_githubaction:
        print(f'报告路径：https://lisa1213001.github.io/dodo-test/{now}    (需要等待一段时间报告才会生成)')
    else:
        os.system(f'allure serve report_html_dir')
    
    stop_virtualdisplay_ifneeded()
