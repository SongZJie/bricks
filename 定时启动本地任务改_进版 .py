import os
import datetime
import time
import pymysql

def sth(path):
   

    os.system("\"%s\"" % path)

def main():
   
    path = input("输入打开文件的路径和名称\n>>>")
    print("分别输入定时的小时和时间")

    
    
    h_s=input("输入小时：\n>>>")
    m_s=input("输入分钟：\n>>>")
    h = int(h_s)
    m = int(m_s)

    '''h表示设定的小时，m为设定的分钟'''
	

    while True:

        now = datetime.datetime.now()

        # 判断是否达到设定时间
        if now.hour==h and now.minute==m:
		
		 # 到达设定时间，结束内循环

            break

            # 不到时间就等20秒之后再次检测

        time.sleep(20)

       
    sth (path)
		
	
if __name__ == '__main__':

    main()
