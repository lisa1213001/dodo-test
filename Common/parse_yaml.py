import os.path

import yaml

def parse_yaml(file,section):
    file = os.path.join(os.path.dirname(os.path.dirname(__file__)),'Config',file)
    with open(file,'r',encoding='utf-8') as f:
        data = yaml.load(f,Loader=yaml.FullLoader)
        return data[section]


