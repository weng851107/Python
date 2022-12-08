import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation 
import math
import telnetlib
import threading
import time

#
## Parameter Setting:
#
__frame = 25
fig = plt.figure(figsize=(6,6))
plt.title('[Chicony] The Plot of the Combined Radars')
ax = plt.subplot(111, polar=True)       # 繪製極座標
ax.set_title('[Chicony] The Plot of the Combined Radars', fontdict=None, loc='center', pad=15, fontsize=20)
ax.set_theta_zero_location('N')         # 設定 0 度的位置
ax.set_thetamin(-90)                    # 設定顯示最小角度
ax.set_thetamax(90)                     # 設定顯示最大角度
ax.set_thetagrids(range(-90,91,15))     # 設定放射狀隔線
ax.set_rlim(0,1000)                     # 設定數值顯示範圍
ax.set_rgrids(range(0,1001,100))        # 設定圓周隔線
plot, = ax.plot([],[])

# threading locker
mutex = threading.Lock()

# initilize the scatter radius and angle
g_r = []
g_theta = []

def collect_data_telnet():

    # Telnet Parameter
    #Host = input("IP: ")
    Host = "10.42.0.2"
    Port = "23"
    username = "root"

    # Connect to Telnet Server
    tn = telnetlib.Telnet(Host, Port, timeout=5)
    tn.set_debuglevel(3)
    
    # login the user name 
    tn.read_until(b"Ambarella login: ")
    tn.write(username.encode('ascii') + b'\n')

    time.sleep(1)

    # excute the radar program
    tn.write(b"cec_radar_tester -Q\n")

    global thread_flag
    global g_r
    global g_theta

    while True :
        if thread_flag == 1:
            # Blocking reading the stream until the expected byte string
            show = tn.read_until(b"radarOutput").decode()
            # Get the return value after blocking reading the stream until the expected byte string
            show = tn.read_very_eager().decode()
            show_split = show.split('\r\n')
            #show_split = [' obj-0: angle=40, motion_range=659, velocity=65511, amp_vrms_vm=15']
            
            for i in show_split:
                show_split_v2 = i.split(',')
                l = 0
                for j in show_split_v2:
                    show_split_v3 = j.split('=')
                    p = 0
                    for k in show_split_v3:
                        if p == 1 and l == 0:
                            # define the scatter angle, and math.radians use in the tranformation between degree and radian
                            g_theta.append(math.radians(int(k)))
                            l = l + 1
                            continue
                        if p == 1 and l == 1:
                            # define the scatter radius
                            g_r.append(int(k))
                            l = l + 1
                            continue
                        p = p + 1

            print("g_r = ", g_r)
            print("g_theta = ", g_theta)
        else:
            break

    # Disconnect and close the telnet
    tn.write(b"exit\n")
    tn.close()

def callback_plot_polar(self):

    global g_r
    global g_theta

    mutex.acquire()

    plot = ax.scatter(g_theta, g_r, c='r',cmap='hsv',alpha=0.75, s=30)       #s設定點的大小

    #print("plot g_r = ", g_r)
    #print("plot g_theta = ", g_theta)

    g_r = []
    g_theta = []

    mutex.release()
    
    return plot,

if __name__ == "__main__":	

    thread_flag = 1

    # 建立一個子執行緒
    t1 = threading.Thread(target = collect_data_telnet)
    t1.setDaemon(True)
    # 執行該子執行緒
    t1.start()

    # 主程序執行Animation
    ani = FuncAnimation(fig, callback_plot_polar, frames=__frame, blit=True)
    plt.show()

    # 等待 t1 這個子執行緒結束
    #t1.join()
    thread_flag = 0

    print("Done.")