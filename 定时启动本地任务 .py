import os
import datetime
import time
import pymysql

def sth():
        

	os.system("F:\各种脚本\hello.py")

def main(h=23, m=43):

    '''h表示设定的小时，m为设定的分钟'''

    while True:

        now = datetime.datetime.now()

        # 判断是否达到设定时间
        if now.hour==h and now.minute==m:
		
		 # 到达设定时间，结束内循环

            break

            # 不到时间就等20秒之后再次检测

        time.sleep(20)

        
    sth ()
		
	
if __name__ == '__main__':

	main()