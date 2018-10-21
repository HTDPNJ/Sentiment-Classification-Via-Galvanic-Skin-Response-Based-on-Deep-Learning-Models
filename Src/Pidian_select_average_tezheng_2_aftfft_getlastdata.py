###从皮电每几个数值求了均值后,获取每个用户对应视频num的数据
import csv
import pandas as pd
import numpy as np
def get_last_sec_data(source_path,dis_path,num): ##源文件路径，目标文件路径，num表示最后几秒的数据/若num表示-1取得则是所有时间数据
    name_testtime_Filmname_list=[]
    csvfile = open(source_path, newline='')  # 打开文件
    csvReader = csv.reader(csvfile)  # 返回的可迭代类型
    data = []  # 用于存储该文件里的整个数据
    for content in csvReader:
        data.append(content)
    csvfile.close()  # 关闭文件
    # 存储文件
    csvFile = open(dis_path, 'a+', newline='')  # 创建被写入文件名，，否则会有多余空格,创建新文件用于写入处理后的数据
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(('INFO', 'Sex', 'Dawu',"QINGGAN","PD"))
    for i in range(1, len(data)):  # 获取姓名、测试次数、刺激视频姓名
        if(int (data[i][9])!=1):  #把过渡视频去掉
            subname_list = []
            subname_list.append(data[i][0])
            subname_list.append(data[i][6])
            subname_list.append(data[i][10])
            if subname_list not in name_testtime_Filmname_list:
                name_testtime_Filmname_list.append(subname_list)
    df = pd.read_csv(source_path)  # df是导入整个表数据
    for i in range(0, len(name_testtime_Filmname_list)):
        SAVE_LIST=[]
        relax = df[df.Person_name == name_testtime_Filmname_list[i][0]]  # 进行筛选控制 and df.Test_time== 2  and df.Has_blank==1
        relax = relax[relax.Test_time == int(name_testtime_Filmname_list[i][1])]
        relax = relax[relax.Set_id == name_testtime_Filmname_list[i][2]]
        relax = relax[relax.Film_name == name_testtime_Filmname_list[i][4]]
        print(pd_all_average[0])
        print(type(pd_all_average[0]))


        dawu=relax.Dawu.tolist()   #存储该条数据对应的大五人格
        qinggan=relax.QINGGAN.tolist()   #存储该条对应的情感评分
        sex=relax.Sex.tolist()   #性别
        SAVE_LIST.append(name_testtime_Filmname_list[i])
        if(len(sex)>0):
            SAVE_LIST.append(sex[0])
        if(len(dawu)>0):
            SAVE_LIST.append(dawu[0])
        if (len(qinggan) > 0):
            SAVE_LIST.append(qinggan[0])
        SAVE_LIST.append(save_pd)
        csvWriter.writerow(SAVE_LIST)
