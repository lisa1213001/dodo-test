import csv

def parse_csv(file):
    mylist = []
    with open(file,'r',encoding='utf-8') as f:
        data = csv.reader(f)
        for i in data:
            mylist.append(i)

        return mylist

if __name__ == '__main__':
    data = parse_csv('../Data/test_001_swap.csv')
    print(data)