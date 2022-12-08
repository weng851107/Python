"""
    Date: 2022/05/31
    Writer: Antony_Weng
    Application: PC(windows) read the radar data from ARM machine and display it.
    Note: 
        1. collect_data_telnet(): Use python telnetlib to get the data. --> sub-thread
           thread_plot_polar(): display in the figure. --> main-thread
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import telnetlib
import threading

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

    # excute the radar program
    tn.write(b"cec_radar_tester -Q\n")

    global g_r
    global g_theta

    while True :
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

    # Disconnect and close the telnet
    tn.write(b"exit\n")
    tn.close()

def thread_plot_polar():

    # define the scatter color
    colors = 'r'

    global g_r
    global g_theta

    while True :

        # plot polar coordinates
        ax = plt.subplot(111, projection='polar')
        ax.set_xlim(-np.pi/2, np.pi/2)
        ax.set_xticks(np.arange(-np.pi/2, np.pi/2*1.1, np.pi/18))
        ax.set_ylim(0, 1000)
        ax.set_yticks(np.arange(0, 1010, 100))

        mutex.acquire()
        # draw a scatter plot, parameter(angle, radius, color)
        c = ax.scatter(g_theta, g_r, s=10, c=colors, cmap='hsv', alpha=0.75)

        #print("plot g_r = ", g_r)
        #print("plot g_theta = ", g_theta)
        
        g_r = []
        g_theta = []

        mutex.release()

        # display
        plt.pause(0.5)


if __name__ == "__main__":	

    # 建立一個子執行緒
    t1 = threading.Thread(target = collect_data_telnet)
    # 執行該子執行緒
    t1.start()

    thread_plot_polar()

    # 等待 t 這個子執行緒結束
    t1.join()

    print("Done.")
