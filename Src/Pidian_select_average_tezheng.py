#从滤波完，并且将皮电减去均值的数据；；每几个求一个平均值，缩小维度
import csv
import pandas as pd
import numpy
import json
from more_itertools import chunked
def get_average(source_path,dis_path,num):  #文件的路径，存储文件的路径，num表示每几个数据取一个平均值;若num是-1表示每一秒的数据求一个平均值
        csvfile = open(source_path, newline='')  # 打开文件
        csvReader = csv.reader(csvfile)  # 返回的可迭代类型
        data = []  # 用于存储该文件里的整个数据
        for content in csvReader:
            data.append(content)
        csvfile.close()  # 关闭文件

        csvFile = open(dis_path, 'a+', newline='')  # 创建被写入文件名，，否则会有多余空格,创建新文件用于写入处理后的数据
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(('Person_name', 'Sex', 'Age', 'Height', 'Weight', 'Phone', 'Test_time', 'Dawu',
                            'Set_id', 'Has_blank', 'Film_name', 'Film_time', 'film_time_second', 'Start_time',
                            'SECOND_TIME', 'second_time_second',
                            'CURRTIME', 'MAIBO', 'PIDIAN', 'CurrFell', 'QINGGAN', 'XIUZ_PD_DATA', 'PD_AFT_BUTTER',
                            'PD_AVERAGE', 'XIUZ_MB_DATA', "PD_BLANK_AVERAGE", "PD_SUB_AVERAGE","PD_PERNUM_SUB_AVERAGE"))
        for i in range(1, len(data)):  # len(data)
            index=len(data[i])  #定位PD_SUB_AVERAGE所在位置
            tem_list_pd = list(map(float, tem_pd))
            if(num!=-1):
                per_aver_list=[sum(x) / len(x) for x in chunked(tem_list_pd, num)]
            else:
                per_aver_list=sum(tem_list_pd)/len(tem_list_pd)
            print(per_aver_list)
            data[i].append(per_aver_list)
            csvWriter.writerow(data[i])