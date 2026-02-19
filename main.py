import random
import os
num1 = 0
num2 = 0
with open("config/randomscope","r") as f:#读取配置文件
    num = f.readlines()
    num1 = num[0][:-1]
    num1 = int(num1)
    num2 = num[1]
    num2 = int(num2)
    f.close()
print("num1:",num1,"\nnum2:",num2)
endnum = random.randint(num1,num2)
print("最终随机数:",endnum)
endnum = os.path.join("video" , str(endnum) + ".mp4")
print("最终文件名:",endnum)
os.startfile(endnum)