import numpy as np
np.random.seed(1337)
import matplotlib.pyplot as plt
from scipy import signal
def save_pic(data_list,dir_path,select,num):
    if (select == 1):  # 选择保存填充图
        x = np.arange(0, len(data_list), 0.1)
        data_list = np.array(data_list)
        y1 = [-50] * len(data_list)
        plt.ylim(-50, 50)
        plt.plot(x, data_list, c='r')
        plt.fill_between(x, y1, data_list, facecolor="b", alpha=0.3)  # 填充两条线之间的图
    elif (select == 2):  # 选择保存频谱图
        data_numpy = np.array(data_list)
        print(len(data_list))
        plt.pcolormesh(t, f, Sxx)
        #去除图片白边
        plt.axis('off')
        fig = plt.gcf()
        fig.set_size_inches(7.0 / 3, 7.0 / 3)  # dpi = 300, output = 700*700 pixels
        plt.gca().xaxis.set_major_locator(plt.NullLocator())
        plt.gca().yaxis.set_major_locator(plt.NullLocator())
        plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
        plt.margins(0, 0)
        #去除图片白边
    plt.savefig(dir_path + ".jpg", transparent=True, dpi=300, pad_inches=0)
    plt.close('all')  # 关闭图 0