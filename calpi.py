#coding=utf-8
from math import *
from multiprocessing import Process,Pool
import random,time,threading,os,multiprocessing.forkserver
def cal(num_cal):#计算抛入点数量
    print("进程{0}计算中......".format(os.getpid()))
    incircle=0
    for i in range(num_cal):
        x=random.random()
        y=random.random()
        if sqrt(pow(x,2)+pow(y,2))<1.0:
            incircle+=1
    return incircle
def startProcess(total,tNum):#创建进程开始执行
    results=[]
    pots=0
    pool=Pool(processes=tNum)
    total=int(total/tNum)
    for i in range(tNum):
        results.append(pool.apply_async(cal,args=(total,)))
    pool.close()
    pool.join()
    for i in results:
        pots=pots+i.get()
    return pots
def monte():
    x=int(input("请输入抛入点数量（数量越大结果越准）："))
    y=int(input("请输入调用进程数（最大为8）：")) 
    start=time.time()
    results=startProcess(x,y)
    print("程序运行时间为：{}秒".format(time.time()-start))
    return 4*results/x
def limit():
    n=int(input("请输入常数n（越大越精确）："))
    sum=0
    start=time.time()
    for i in range(n):
        sum=sum+1.0/((i+1)*(i+1))
    pi=sqrt(sum*6)
    print("程序运行时间为：{}秒".format(time.time()-start))
    return pi
def main():
    method=input("请输入1，2选择计算方法\n1.蒙特卡洛法：通过抛撒大量随机点计算\n2.利用极限公式计算\n")
    if method=='1':
        pi=monte()
    else:
        pi=limit()
    print("Π=",pi)
if __name__=="__main__":
    multiprocessing.freeze_support()
    main()
    os.system("pause")
        