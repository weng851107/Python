"""
    Date: 2022/12/08
    Writer: Antony_Weng
    Application: Radar UI in PC(windows).
    Note: 
        1. Revise the parameters in APP1 mode.
        2. Plot the Dynamic Radar Pt.
"""

from cProfile import label
import tkinter as tk
from tkinter import * 
from tkinter import messagebox
import os
import threading
import telnetlib
import time
from functools import partial
import struct

from PIL import Image,ImageTk       ## 在Python中使用Label組件加入Jpg圖片

def float_to_hex(f):
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])

def hex_to_float(h):
    return struct.unpack('!f', bytes.fromhex(h))[0]

root = tk.Tk()

#print(root.winfo_screenwidth())     # 輸出螢幕寬度
#print(root.winfo_screenheight())    # 輸出螢幕高度
w=1080   # width
r=720   # height
x=100   # 與視窗左上x的距離
y=100   # 與視窗左上y的距離
root.geometry('%dx%d+%d+%d' % (w,r,x,y))
root.resizable(False, False)   # 設定 x 方向和 y 方向都不能縮放
#root.minsize(1080, 720)    # 設定視窗最小為 1080x720
#root.maxsize(1080, 720)    # 設定視窗最大為 1080x720

root.title('[Chicony] The GUI of the Radars')   # 設定視窗標題
_root_bg = "#EBEBFF"  #"#CFCFCF"
root.configure(bg=_root_bg)                    # 可以直接打顏色名稱或是找色碼表的代號(https://www.wibibi.com/info.php?tid=372)

'''
#
## Variable
#
'''
FwVer=""
cecFwVer=""

_timeout = 20

_ret_fail = "RET:FAILEND"

_label_ModeParameters_Mode_Text = '2' #2DMode
_label_ModeParameters_SentryTimes_Text = '1'
_label_ModeParameters_2DTimes_Text = '20'

_label_SensingParameters_SentryThr_Text = '10'
_label_SensingParameters_2DThr_Text = '10'

_label_DutyParameters_Enable_Text = '1' #ON
_label_DutyParameters_SentryDetectRate_Text = '8'
_label_DutyParameters_2DDetectRate_Text = '12'

_label_TargetParameters_RangeMax_Text = '1200'
_label_TargetParameters_RangeMin_Text = '0'
_label_TargetParameters_AngleMax_Text = '140'

_label_TrackingParameters_Init_Text = '4'
_label_TrackingParameters_Delete_Text = '8'

_label_ROISetting_ROIRangeMin_Text = '10'
_label_ROISetting_ROIRangeMax_Text = '1000'
_label_ROISetting_ROIAngleMax_Text = '140'

_label_ROISelect_Buffer1_Text = '0000000000000000'
_label_ROISelect_Buffer2_Text = '0000000000000000'

_label_GainConfigs_Sentry_TxGain_Text = '8'
_label_GainConfigs_Sentry_RxGain_Text = '8'
_label_GainConfigs_Sentry_Rx01HPF_Text = '23'
_label_GainConfigs_Sentry_Rx02HPF_Text = '23'
_label_GainConfigs_2D_TxGain_Text = '8'
_label_GainConfigs_2D_Rx01Gain_Text = '8'
_label_GainConfigs_2D_Rx02Gain_Text = '8'
_label_GainConfigs_2D_Rx01HPF_Text = '22'
_label_GainConfigs_2D_Rx02HPF_Text = '22'

_label_AngleParameters_Reverse_Text = '0' #OFF
_label_AngleParameters_Compensation_Text = '0'
_label_AngleParameters_Rate_Text = '1'


'''
#
## Function
#
'''

def thread_Dynplot():
    os.system('python DynPlotRadar.py')

def click_plot_start():
    # 建立一個子執行緒
    t1 = threading.Thread(target = thread_Dynplot)
    # 執行該子執行緒
    t1.start()

def click_radar_command(option):

    global entry_RadarID
    global label_FwVer
    global label_cecFwVer
    global label_Return

    label_Return.config(text="NULL")

    # Telnet Parameter
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

    if option == 'fwver':
        cmd = "cec_radar_tester -i " + entry_RadarID.get() + " -v\n"
        # excute the radar program
        tn.write(cmd.encode())
        key="Radar-" + entry_RadarID.get() + ": "
        show = tn.read_until(key.encode(), timeout=_timeout).decode()
        # Get the return value after blocking reading the stream until the expected byte string
        show = tn.read_very_eager().decode()
        FwVer = show.split('\r\n\r\n#')
        #print(FwVer)
        label_FwVer.config(text=FwVer[0])
    elif option == 'cecfwver':
        cmd = "cec_radar_tester -i " + entry_RadarID.get() + " -V\n"
        # excute the radar program
        tn.write(cmd.encode())
        key="radar_index=" + entry_RadarID.get() + "\r\n"
        show = tn.read_until(key.encode(), timeout=_timeout).decode()
        # Get the return value after blocking reading the stream until the expected byte string
        show = tn.read_very_eager().decode()
        cecFwVer = show.split('\r\n')
        #print("cecFwVer=", cecFwVer)
        label_cecFwVer.config(text=cecFwVer[0])

    elif option == 'reset':
        cmd = "cec_radar_tester -i " + entry_RadarID.get() + " -s\n"
        # excute the radar program
        tn.write(cmd.encode())
        show = tn.read_until(b"cec_hal_radar_ts24g_reset:", timeout=_timeout).decode()
    elif option == 'reboot':
        cmd = "cec_radar_tester -i " + entry_RadarID.get() + " -b\n"
        # excute the radar program
        tn.write(cmd.encode())
        show = tn.read_until(b"cec_hal_radar_ts24g_reboot:", timeout=_timeout).decode()
    elif option == 'default':
        cmd = "cec_radar_tester -i " + entry_RadarID.get() + " -d\n"
        # excute the radar program
        tn.write(cmd.encode())
        show = tn.read_until(b"cec_hal_radar_ts24g_load_default:", timeout=_timeout).decode()

    elif option == 'ModeParameters_Get':
        cmd = "cec_radar_tester -i " + entry_RadarID.get() + " -E r\n"
        # excute the radar program
        tn.write(cmd.encode())
        key = "Radar-" + entry_RadarID.get() + ": parameter = "
        show = tn.read_until(key.encode(), timeout=_timeout).decode()
        show = tn.read_very_eager().decode()
        result = show.split('\r\n\r\n')
        if len(result[0]) != 0:
            result_payload = result[0].split(' ')
            result_ret = result[1].split('\r\n')
            label_Return.config(text=result_ret[0])
            mode = int(result_payload[5], 16)
            sentrytimes = int(result_payload[6], 16)
            twodtimes = int(result_payload[7], 16)
            label_ModeParameters_Mode_Text.config(text=mode)
            label_ModeParameters_SentryTimes_Text.config(text=sentrytimes)
            label_ModeParameters_2DTimes_Text.config(text=twodtimes)
        else:
            label_Return.config(text=_ret_fail)
    elif option == 'ModeParameters_Set':
        mode = '{:#04x}'.format(int(entry_ModeParameters_Mode.get()))
        sentrytimes = '{:#04x}'.format(int(entry_ModeParameters_SentryTimes.get()))
        twodtimes = '{:#04x}'.format(int(entry_ModeParameters_2DTimes.get()))
        cmd = "cec_radar_tester -i " + entry_RadarID.get() + " -E w " + mode + " " + sentrytimes + " " + twodtimes + "\n"
        # excute the radar program
        tn.write(cmd.encode())
        key = "Radar-" + entry_RadarID.get() + ": parameter = "
        show = tn.read_until(key.encode(), timeout=_timeout).decode()
        show = tn.read_very_eager().decode()
        result = show.split('\r\n\r\n')
        if len(result[0]) != 0:
            result_payload = result[0].split(' ')
            result_ret = result[1].split('\r\n')
            label_Return.config(text=result_ret[0])
            mode = int(result_payload[5], 16)
            sentrytimes = int(result_payload[6], 16)
            twodtimes = int(result_payload[7], 16)
            label_ModeParameters_Mode_Text.config(text=mode)
            label_ModeParameters_SentryTimes_Text.config(text=sentrytimes)
            label_ModeParameters_2DTimes_Text.config(text=twodtimes)
        else:
            label_Return.config(text=_ret_fail)

    elif option == 'SensingParameters_Get':
        cmd = "cec_radar_tester -i " + entry_RadarID.get() + " -H r\n"
        # excute the radar program
        tn.write(cmd.encode())
        key = "Radar-" + entry_RadarID.get() + ": parameter = "
        show = tn.read_until(key.encode(), timeout=_timeout).decode()
        show = tn.read_very_eager().decode()
        result = show.split('\r\n\r\n')
        if len(result[0]) != 0:
            result_payload = result[0].split(' ')
            result_ret = result[1].split('\r\n')
            label_Return.config(text=result_ret[0])
            sentrythreshold = int(result_payload[6] + result_payload[5], 16)
            twodthreshold = int(result_payload[8] + result_payload[7], 16)
            label_SensingParameters_SentryThr_Text.config(text=sentrythreshold)
            label_SensingParameters_2DThr_Text.config(text=twodthreshold)
        else:
            label_Return.config(text=_ret_fail)

    elif option == 'SensingParameters_Set':
        sentrythreshold = '{:#06x}'.format(int(entry_SensingParameters_SentryThr.get()))
        twodthreshold = '{:#06x}'.format(int(entry_SensingParameters_2DThr.get()))
        cmd = "cec_radar_tester -i " + entry_RadarID.get() + " -H w 0x" + sentrythreshold[4:6] + " 0x" + sentrythreshold[2:4] + " 0x" + twodthreshold[4:6] + " 0x" + twodthreshold[2:4] + "\n"
        # excute the radar program
        tn.write(cmd.encode())
        key = "Radar-" + entry_RadarID.get() + ": parameter = "
        show = tn.read_until(key.encode(), timeout=_timeout).decode()
        show = tn.read_very_eager().decode()
        result = show.split('\r\n\r\n')
        if len(result[0]) != 0:
            result_payload = result[0].split(' ')
            result_ret = result[1].split('\r\n')
            label_Return.config(text=result_ret[0])
            sentrythreshold = int(result_payload[6] + result_payload[5], 16)
            twodthreshold = int(result_payload[8] + result_payload[7], 16)
            label_SensingParameters_SentryThr_Text.config(text=sentrythreshold)
            label_SensingParameters_2DThr_Text.config(text=twodthreshold)
        else:
            label_Return.config(text=_ret_fail)

    elif option == 'DutyParameters_Get':
        cmd = "cec_radar_tester -i " + entry_RadarID.get() + " -c r\n"
        # excute the radar program
        tn.write(cmd.encode())
        key = "Radar-" + entry_RadarID.get() + ": parameter = "
        show = tn.read_until(key.encode(), timeout=_timeout).decode()
        show = tn.read_very_eager().decode()
        result = show.split('\r\n\r\n')
        if len(result[0]) != 0:
            result_payload = result[0].split(' ')
            result_ret = result[1].split('\r\n')
            label_Return.config(text=result_ret[0])
            duty_enable = int(result_payload[5], 16)
            sentrydetectrate = int(result_payload[6], 16)
            twoddetectrate = int(result_payload[7], 16)
            label_DutyParameters_Enable_Text.config(text=duty_enable)
            label_DutyParameters_SentryDetectRate_Text.config(text=sentrydetectrate)
            label_DutyParameters_2DDetectRate_Text.config(text=twoddetectrate)
        else:
            label_Return.config(text=_ret_fail)
    elif option == 'DutyParameters_Set':
        duty_enable = '{:#04x}'.format(int(entry_DutyParameters_Enable.get()))
        sentrydetectrate = '{:#04x}'.format(int(entry_DutyParameters_SentryDetectRate.get()))
        twoddetectrate = '{:#04x}'.format(int(entry_DutyParameters_2DDetectRate.get()))
        cmd = "cec_radar_tester -i " + entry_RadarID.get() + " -c w " + duty_enable + " " + sentrydetectrate + " " + twoddetectrate + "\n"
        # excute the radar program
        tn.write(cmd.encode())
        key = "Radar-" + entry_RadarID.get() + ": parameter = "
        show = tn.read_until(key.encode(), timeout=_timeout).decode()
        show = tn.read_very_eager().decode()
        result = show.split('\r\n\r\n')
        if len(result[0]) != 0:
            result_payload = result[0].split(' ')
            result_ret = result[1].split('\r\n')
            label_Return.config(text=result_ret[0])
            duty_enable = int(result_payload[5], 16)
            sentrydetectrate = int(result_payload[6], 16)
            twoddetectrate = int(result_payload[7], 16)
            label_DutyParameters_Enable_Text.config(text=duty_enable)
            label_DutyParameters_SentryDetectRate_Text.config(text=sentrydetectrate)
            label_DutyParameters_2DDetectRate_Text.config(text=twoddetectrate)
        else:
            label_Return.config(text=_ret_fail)

    elif option == 'TargetParameters_Get':
        cmd = "cec_radar_tester -i " + entry_RadarID.get() + " -n r\n"
        # excute the radar program
        tn.write(cmd.encode())
        key = "Radar-" + entry_RadarID.get() + ": parameter = "
        show = tn.read_until(key.encode(), timeout=_timeout).decode()
        show = tn.read_very_eager().decode()
        result = show.split('\r\n\r\n')
        if len(result[0]) != 0:
            result_payload = result[0].split(' ')
            result_ret = result[1].split('\r\n')
            label_Return.config(text=result_ret[0])
            rangemin = int(result_payload[6] + result_payload[5], 16)
            rangemax = int(result_payload[8] + result_payload[7], 16)
            anglemax = int(result_payload[9], 16)
            label_TargetParameters_RangeMin_Text.config(text=rangemin)
            label_TargetParameters_RangeMax_Text.config(text=rangemax)
            label_TargetParameters_AngleMax_Text.config(text=anglemax)
        else:
            label_Return.config(text=_ret_fail)
    elif option == 'TargetParameters_Set':
        rangemax = '{:#06x}'.format(int(entry_TargetParameters_RangeMax.get()))
        rangemin = '{:#06x}'.format(int(entry_TargetParameters_RangeMin.get()))
        anglemax = '{:#04x}'.format(int(entry_TargetParameters_AngleMax.get()))
        cmd = "cec_radar_tester -i " + entry_RadarID.get() + " -n w 0x" + rangemin[4:6] + " " + rangemin[0:4] + " " + " 0x" + rangemax[4:6] + " " + rangemax[0:4] + " " + anglemax + "\n"
        # excute the radar program
        tn.write(cmd.encode())
        key = "Radar-" + entry_RadarID.get() + ": parameter = "
        show = tn.read_until(key.encode(), timeout=_timeout).decode()
        show = tn.read_very_eager().decode()
        result = show.split('\r\n\r\n')
        if len(result[0]) != 0:
            result_payload = result[0].split(' ')
            result_ret = result[1].split('\r\n')
            label_Return.config(text=result_ret[0])
            rangemin = int(result_payload[6] + result_payload[5], 16)
            rangemax = int(result_payload[8] + result_payload[7], 16)
            anglemax = int(result_payload[9], 16)
            label_TargetParameters_RangeMin_Text.config(text=rangemin)
            label_TargetParameters_RangeMax_Text.config(text=rangemax)
            label_TargetParameters_AngleMax_Text.config(text=anglemax)
        else:
            label_Return.config(text=_ret_fail)

    elif option == 'TrackingParameters_Get':
        cmd = "cec_radar_tester -i " + entry_RadarID.get() + " -e r\n"
        # excute the radar program
        tn.write(cmd.encode())
        key = "Radar-" + entry_RadarID.get() + ": parameter = "
        show = tn.read_until(key.encode(), timeout=_timeout).decode()
        show = tn.read_very_eager().decode()
        result = show.split('\r\n\r\n')
        if len(result[0]) != 0:
            result_payload = result[0].split(' ')
            result_ret = result[1].split('\r\n')
            label_Return.config(text=result_ret[0])
            init = int(result_payload[5], 16)
            delete = int(result_payload[6], 16)
            label_TrackingParameters_Init_Text.config(text=init)
            label_TrackingParameters_Delete_Text.config(text=delete)
        else:
            label_Return.config(text=_ret_fail)
    elif option == 'TrackingParameters_Set':
        init = '{:#04x}'.format(int(entry_TrackingParameters_Init.get()))
        delete = '{:#04x}'.format(int(entry_TrackingParameters_Delete.get()))
        cmd = "cec_radar_tester -i " + entry_RadarID.get() + " -e w " + init + " " + delete + "\n"
        # excute the radar program
        tn.write(cmd.encode())
        key = "Radar-" + entry_RadarID.get() + ": parameter = "
        show = tn.read_until(key.encode(), timeout=_timeout).decode()
        show = tn.read_very_eager().decode()
        result = show.split('\r\n\r\n')
        if len(result[0]) != 0:
            result_payload = result[0].split(' ')
            result_ret = result[1].split('\r\n')
            label_Return.config(text=result_ret[0])
            init = int(result_payload[5], 16)
            delete = int(result_payload[6], 16)
            label_TrackingParameters_Init_Text.config(text=init)
            label_TrackingParameters_Delete_Text.config(text=delete)
        else:
            label_Return.config(text=_ret_fail)

    elif option == 'ROISetting_Get':
        cmd = "cec_radar_tester -i " + entry_RadarID.get() + " -O r\n"
        # excute the radar program
        tn.write(cmd.encode())
        key = "Radar-" + entry_RadarID.get() + ": parameter = "
        show = tn.read_until(key.encode(), timeout=_timeout).decode()
        show = tn.read_very_eager().decode()
        result = show.split('\r\n\r\n')
        if len(result[0]) != 0:
            result_payload = result[0].split(' ')
            result_ret = result[1].split('\r\n')
            label_Return.config(text=result_ret[0])
            roirangemin = int(result_payload[6] + result_payload[5], 16)
            roirangemax = int(result_payload[8] + result_payload[7], 16)
            roianglemax = int(result_payload[9], 16)
            label_ROISetting_ROIRangeMin_Text.config(text=roirangemin)
            label_ROISetting_ROIRangeMax_Text.config(text=roirangemax)
            label_ROISetting_ROIAngleMax_Text.config(text=roianglemax)
        else:
            label_Return.config(text=_ret_fail)
    elif option == 'ROISetting_Set':
        roirangemax = '{:#06x}'.format(int(entry_ROISetting_ROIRangeMax.get()))
        roirangemin = '{:#06x}'.format(int(entry_ROISetting_ROIRangeMin.get()))
        roianglemax = '{:#04x}'.format(int(entry_ROISetting_ROIAngleMax.get()))
        cmd = "cec_radar_tester -i " + entry_RadarID.get() + " -O w 0x" + roirangemin[4:6] + " " + roirangemin[0:4] + " 0x" + roirangemax[4:6] + " " + roirangemax[0:4] + " " + roianglemax + "\n"
        # excute the radar program
        tn.write(cmd.encode())
        key = "Radar-" + entry_RadarID.get() + ": parameter = "
        show = tn.read_until(key.encode(), timeout=_timeout).decode()
        show = tn.read_very_eager().decode()
        result = show.split('\r\n\r\n')
        if len(result[0]) != 0:
            result_payload = result[0].split(' ')
            result_ret = result[1].split('\r\n')
            label_Return.config(text=result_ret[0])
            roirangemin = int(result_payload[6] + result_payload[5], 16)
            roirangemax = int(result_payload[8] + result_payload[7], 16)
            roianglemax = int(result_payload[9], 16)
            label_ROISetting_ROIRangeMin_Text.config(text=roirangemin)
            label_ROISetting_ROIRangeMax_Text.config(text=roirangemax)
            label_ROISetting_ROIAngleMax_Text.config(text=roianglemax)
        else:
            label_Return.config(text=_ret_fail)

    elif option == 'ROISelect_Buffer1_Get':
        cmd = "cec_radar_tester -i " + entry_RadarID.get() + " -L r\n"
        # excute the radar program
        tn.write(cmd.encode())
        key = "Radar-" + entry_RadarID.get() + ": parameter = "
        show = tn.read_until(key.encode(), timeout=_timeout).decode()
        show = tn.read_very_eager().decode()
        result = show.split('\r\n\r\n')
        if len(result[0]) != 0:
            result_payload = result[0].split(' ')
            result_ret = result[1].split('\r\n')
            label_Return.config(text=result_ret[0])
            buffer1 = result_payload[5] + result_payload[6] + result_payload[7] + result_payload[8] + result_payload[9] + result_payload[10] + result_payload[11] + result_payload[12]
            label_ROISelect_Buffer1_Text.config(text=buffer1)
        else:
            label_Return.config(text=_ret_fail)
    elif option == 'ROISelect_Buffer1_Set':
        buffer1 = str(entry_ROISelect_Buffer1.get())
        cmd = "cec_radar_tester -i " + entry_RadarID.get() + " -L w 0x" + buffer1[0:2] + " 0x" + buffer1[2:4] + " 0x" + buffer1[4:6] + " 0x" + buffer1[6:8] + " 0x" + buffer1[8:10] \
             + " 0x" + buffer1[10:12] + " 0x" + buffer1[12:14] + " 0x" + buffer1[14:16] + "\n"
        # excute the radar program
        tn.write(cmd.encode())
        key = "Radar-" + entry_RadarID.get() + ": parameter = "
        show = tn.read_until(key.encode(), timeout=_timeout).decode()
        show = tn.read_very_eager().decode()
        result = show.split('\r\n\r\n')
        if len(result[0]) != 0:
            result_payload = result[0].split(' ')
            result_ret = result[1].split('\r\n')
            label_Return.config(text=result_ret[0])
            buffer1 = result_payload[5] + result_payload[6] + result_payload[7] + result_payload[8] + result_payload[9] + result_payload[10] + result_payload[11] + result_payload[12]
            label_ROISelect_Buffer1_Text.config(text=buffer1)
        else:
            label_Return.config(text=_ret_fail)

    elif option == 'ROISelect_Buffer2_Get':
        cmd = "cec_radar_tester -i " + entry_RadarID.get() + " -l r\n"
        # excute the radar program
        tn.write(cmd.encode())
        key = "Radar-" + entry_RadarID.get() + ": parameter = "
        show = tn.read_until(key.encode(), timeout=_timeout).decode()
        show = tn.read_very_eager().decode()
        result = show.split('\r\n\r\n')
        if len(result[0]) != 0:
            result_payload = result[0].split(' ')
            result_ret = result[1].split('\r\n')
            label_Return.config(text=result_ret[0])
            buffer2 = result_payload[5] + result_payload[6] + "000000000000"
            label_ROISelect_Buffer2_Text.config(text=buffer2)
        else:
            label_Return.config(text=_ret_fail)
    elif option == 'ROISelect_Buffer2_Set':
        buffer2 = str(entry_ROISelect_Buffer2.get())
        cmd = "cec_radar_tester -i " + entry_RadarID.get() + " -l w 0x" + buffer2[0:2] + " 0x" + buffer2[2:4] + " 0x00 0x00 0x00 0x00 0x00 0x00\n"
        # excute the radar program
        tn.write(cmd.encode())
        key = "Radar-" + entry_RadarID.get() + ": parameter = "
        show = tn.read_until(key.encode(), timeout=_timeout).decode()
        show = tn.read_very_eager().decode()
        result = show.split('\r\n\r\n')
        if len(result[0]) != 0:
            result_payload = result[0].split(' ')
            result_ret = result[1].split('\r\n')
            label_Return.config(text=result_ret[0])
            buffer2 = result_payload[5] + result_payload[6] + "000000000000"
            label_ROISelect_Buffer2_Text.config(text=buffer2)
        else:
            label_Return.config(text=_ret_fail)

    elif option == 'GainConfigs_Get':
        cmd = "cec_radar_tester -i " + entry_RadarID.get() + " -G r\n"
        # excute the radar program
        tn.write(cmd.encode())
        key = "Radar-" + entry_RadarID.get() + ": parameter = "
        show = tn.read_until(key.encode(), timeout=_timeout).decode()
        show = tn.read_very_eager().decode()
        result = show.split('\r\n\r\n')
        if len(result[0]) != 0:
            result_payload = result[0].split(' ')
            result_ret = result[1].split('\r\n')
            label_Return.config(text=result_ret[0])
            sentrytxgain = int(result_payload[5], 16)
            sentryrxgain = int(result_payload[6], 16) & 0b00001111
            sentryrx01hpf = int(result_payload[7], 16)
            sentryrx02hpf = int(result_payload[8], 16)
            twodtxgain = int(result_payload[9], 16)
            twodrx01gain = (int(result_payload[10], 16) & 0b11110000) >> 4
            twodrx02gain = int(result_payload[10], 16) & 0b00001111
            twodrx01hpf = int(result_payload[11], 16)
            twodrx02hpf = int(result_payload[12], 16)
            label_GainConfigs_Sentry_TxGain_Text.config(text=sentrytxgain)
            label_GainConfigs_Sentry_RxGain_Text.config(text=sentryrxgain)
            label_GainConfigs_Sentry_Rx01HPF_Text.config(text=sentryrx01hpf)
            label_GainConfigs_Sentry_Rx02HPF_Text.config(text=sentryrx02hpf)
            label_GainConfigs_2D_TxGain_Text.config(text=twodtxgain)
            label_GainConfigs_2D_Rx01Gain_Text.config(text=twodrx01gain)
            label_GainConfigs_2D_Rx02Gain_Text.config(text=twodrx02gain)
            label_GainConfigs_2D_Rx01HPF_Text.config(text=twodrx01hpf)
            label_GainConfigs_2D_Rx02HPF_Text.config(text=twodrx02hpf)
        else:
            label_Return.config(text=_ret_fail)
    elif option == 'GainConfigs_Set':
        sentrytxgain = '{:#04x}'.format(int(entry_GainConfigs_Sentry_TxGain.get()))
        sentryrxgain = '{:#03x}'.format(int(entry_GainConfigs_Sentry_RxGain.get()))
        sentryrxgain = sentryrxgain + sentryrxgain[2]
        sentryrx01hpf = '{:#04x}'.format(int(entry_GainConfigs_Sentry_Rx01HPF.get()))
        sentryrx02hpf = '{:#04x}'.format(int(entry_GainConfigs_Sentry_Rx02HPF.get()))
        twodtxgain = '{:#04x}'.format(int(entry_GainConfigs_2D_TxGain.get()))
        twodrx01gain = '{:#03x}'.format(int(entry_GainConfigs_2D_Rx01Gain.get()))
        twodrx02gain = '{:#03x}'.format(int(entry_GainConfigs_2D_Rx02Gain.get()))
        twodrx01hpf = '{:#04x}'.format(int(entry_GainConfigs_2D_Rx01HPF.get()))
        twodrx02hpf = '{:#04x}'.format(int(entry_GainConfigs_2D_Rx02HPF.get()))
        cmd = "cec_radar_tester -i " + entry_RadarID.get() + " -G w " + sentrytxgain + " " + sentryrxgain + " " + sentryrx01hpf + " " \
            + sentryrx02hpf + " " + twodtxgain + " " + twodrx01gain + twodrx02gain[2] + " " + twodrx01hpf + " " + twodrx02hpf + "\n"
        # excute the radar program
        tn.write(cmd.encode())
        key = "Radar-" + entry_RadarID.get() + ": parameter = "
        show = tn.read_until(key.encode(), timeout=_timeout).decode()
        show = tn.read_very_eager().decode()
        result = show.split('\r\n\r\n')
        if len(result[0]) != 0:
            result_payload = result[0].split(' ')
            result_ret = result[1].split('\r\n')
            label_Return.config(text=result_ret[0])
            sentrytxgain = int(result_payload[5], 16)
            sentryrxgain = int(result_payload[6], 16) & 0b00001111
            sentryrx01hpf = int(result_payload[7], 16)
            sentryrx02hpf = int(result_payload[8], 16)
            twodtxgain = int(result_payload[9], 16)
            twodrx01gain = (int(result_payload[10], 16) & 0b11110000) >> 4
            twodrx02gain = int(result_payload[10], 16) & 0b00001111
            twodrx01hpf = int(result_payload[11], 16)
            twodrx02hpf = int(result_payload[12], 16)
            label_GainConfigs_Sentry_TxGain_Text.config(text=sentrytxgain)
            label_GainConfigs_Sentry_RxGain_Text.config(text=sentryrxgain)
            label_GainConfigs_Sentry_Rx01HPF_Text.config(text=sentryrx01hpf)
            label_GainConfigs_Sentry_Rx02HPF_Text.config(text=sentryrx02hpf)
            label_GainConfigs_2D_TxGain_Text.config(text=twodtxgain)
            label_GainConfigs_2D_Rx01Gain_Text.config(text=twodrx01gain)
            label_GainConfigs_2D_Rx02Gain_Text.config(text=twodrx02gain)
            label_GainConfigs_2D_Rx01HPF_Text.config(text=twodrx01hpf)
            label_GainConfigs_2D_Rx02HPF_Text.config(text=twodrx02hpf)
        else:
            label_Return.config(text=_ret_fail)

    elif option == 'AngleParameters_Get':
        cmd = "cec_radar_tester -i " + entry_RadarID.get() + " -g r\n"
        # excute the radar program
        tn.write(cmd.encode())
        key = "Radar-" + entry_RadarID.get() + ": parameter = "
        show = tn.read_until(key.encode(), timeout=_timeout).decode()
        show = tn.read_very_eager().decode()
        result = show.split('\r\n\r\n')
        if len(result[0]) != 0:
            result_payload = result[0].split(' ')
            result_ret = result[1].split('\r\n')
            label_Return.config(text=result_ret[0])
            anglereverse = int(result_payload[5], 16)
            angleoffset = int(result_payload[8] + result_payload[7], 16)
            anglerate = round(hex_to_float(result_payload[12] + result_payload[11] + result_payload[10] + result_payload[9]), 1)
            label_AngleParameters_Reverse_Text.config(text=anglereverse)
            label_AngleParameters_Compensation_Text.config(text=angleoffset)
            label_AngleParameters_Rate_Text.config(text=anglerate)
        else:
            label_Return.config(text=_ret_fail)
    elif option == 'AngleParameters_Set':
        anglereverse = '{:#04x}'.format(int(entry_AngleParameters_Reverse.get()))
        angleoffset = '{:#06x}'.format(int(entry_AngleParameters_Compensation.get()))
        anglerate = float_to_hex(float(entry_AngleParameters_Rate.get()))
        cmd = "cec_radar_tester -i " + entry_RadarID.get() + " -g w " + anglereverse + " 0x" + angleoffset[4:6] + " " + angleoffset[0:4] \
            + " 0x" + anglerate[8:10] + " 0x" + anglerate[6:8] + " 0x" + anglerate[4:6] + " " + anglerate[0:4] + "\n"
        # excute the radar program
        tn.write(cmd.encode())
        key = "Radar-" + entry_RadarID.get() + ": parameter = "
        show = tn.read_until(key.encode(), timeout=_timeout).decode()
        show = tn.read_very_eager().decode()
        result = show.split('\r\n\r\n')
        if len(result[0]) != 0:
            result_payload = result[0].split(' ')
            result_ret = result[1].split('\r\n')
            label_Return.config(text=result_ret[0])
            anglereverse = int(result_payload[5], 16)
            angleoffset = int(result_payload[8] + result_payload[7], 16)
            anglerate = round(hex_to_float(result_payload[12] + result_payload[11] + result_payload[10] + result_payload[9]), 1)
            label_AngleParameters_Reverse_Text.config(text=anglereverse)
            label_AngleParameters_Compensation_Text.config(text=angleoffset)
            label_AngleParameters_Rate_Text.config(text=anglerate)
        else:
            label_Return.config(text=_ret_fail)

    else:
        print("option is invailid!")

    # Get the return value after blocking reading the stream until the expected byte string
    #show = tn.read_very_eager().decode()

    '''
    #print("show=", show)
    if "SUCCESS" in show:
        print("RET:SUCCESSEND")
    else:
        print("RET:FAILEND")
    '''

def click_queue_parameters():
    click_radar_command('ModeParameters_Get')
    click_radar_command('SensingParameters_Get')
    click_radar_command('DutyParameters_Get')
    click_radar_command('TargetParameters_Get')
    click_radar_command('TrackingParameters_Get')
    click_radar_command('ROISetting_Get')
    click_radar_command('ROISelect_Buffer1_Get')
    click_radar_command('ROISelect_Buffer2_Get')
    click_radar_command('GainConfigs_Get')
    click_radar_command('AngleParameters_Get')

def click_radar_messagebox(option):
    subw=720   # width
    subr=480   # height
    subx=200   # 與視窗左上x的距離
    suby=200   # 與視窗左上y的距離
    sub_bg = '#CFCFCF'      # 可以直接打顏色名稱或是找色碼表的代號(https://www.wibibi.com/info.php?tid=372)
    sub_width = 720
    sub_font = ('Times', 12)
    sub_row=0


    if option == 'SystemConfiguration':
        subWindow = tk.Toplevel(root)
        subWindow.geometry('%dx%d+%d+%d' % (subw, subr, subx, suby))
        subWindow.title('[Chicony] System Configuration')
        #subWindow.configure(bg=sub_bg)

        Message(subWindow, text='0x04 - Reset', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='O:reboot', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='O:load default setting(gain, plot and showlog)', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='O:calibration(if app has calibration procedure)\n', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='0x05 - Reboot', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='O:reboot', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='X:load default setting(gain, plot and showlog)', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='X:calibration(if app has calibration procedure)\n', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='0x06 - Load Default', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='X:reboot', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='O:load default setting(gain, plot and showlog)', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='X:calibration(if app has calibration procedure)', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1

        subWindow.mainloop()
    elif option == 'ModeParameters':
        subWindow = tk.Toplevel(root)
        subWindow.geometry('%dx%d+%d+%d' % (subw, subr, subx, suby))
        subWindow.title('[Chicony] Mode Parameters')
        #subWindow.configure(bg=sub_bg)

        jpg = Image.open("./RadarUI/ModeParameters00.PNG")
        jpg_resized = jpg.resize((720, 120))  
        jpg_show = ImageTk.PhotoImage(jpg_resized)
        text_jpg = tk.Label(subWindow, image=jpg_show, height=120, width=720)
        text_jpg.grid(row=sub_row, column=0, sticky='w')
        sub_row+=1

        Message(subWindow, text='\nMode Select(uint8_t) : 1: Sentry Mode. 2: 2D Mode. 3: Dual Mode.\n', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='Sentry Mode to 2D Mode(Times)(uint8_t) : Times of sentry mode swith to 2D mode debounce. Default value is 1, the system detect 1 time if \
                object location out of detection zone ,then switch to 2D mode.\n', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='2D Mode to Sentry Mode(Times)(uint8_t) : Times of 2D mode swith to sentry mode debounce. Default value is 20, the system detect 20 times if \
                object location out of detection zone ,then switch to sentry mode.\n', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1

        subWindow.mainloop()
    elif option == 'SensingParameters':
        subWindow = tk.Toplevel(root)
        subWindow.geometry('%dx%d+%d+%d' % (subw, subr, subx, suby))
        subWindow.title('[Chicony] Sensing Parameters')
        #subWindow.configure(bg=sub_bg)

        jpg = Image.open("./RadarUI/SensingParameters00.PNG")
        jpg_resized = jpg.resize((720, 80))  
        jpg_show = ImageTk.PhotoImage(jpg_resized)
        text_jpg = tk.Label(subWindow, image=jpg_show, height=80, width=720)
        text_jpg.grid(row=sub_row, column=0, sticky='w')
        sub_row+=1

        Message(subWindow, text='\nSentry Mode MTI CFAR Threshold(uint16_t ): 調整Sentry模式CFAR閥值\n', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='2D Mode MTI CFAR Threshold(uint16_t ): 調整2D模式CFAR閥\n', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1

        subWindow.mainloop()
    elif option == 'DutyParameters':
        subWindow = tk.Toplevel(root)
        subWindow.geometry('%dx%d+%d+%d' % (subw, subr, subx, suby))
        subWindow.title('[Chicony] Duty Parameters')
        #subWindow.configure(bg=sub_bg)

        jpg = Image.open("./RadarUI/DutyParameters00.PNG")
        jpg_resized = jpg.resize((720, 80))  
        jpg_show = ImageTk.PhotoImage(jpg_resized)
        text_jpg = tk.Label(subWindow, image=jpg_show, height=80, width=720)
        text_jpg.grid(row=sub_row, column=0, sticky='w')
        sub_row+=1

        Message(subWindow, text='\nDutyCycleEnable (uint8_t): [ON]=1, 開啟省電模式; [OFF]=0,關閉省電模式', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='註 : 開啟Duty Enable選項 SentryMode Detection Rate 及 TwoDMode Detection Rate 才有功能\n', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='SentryModeDetectionRate (uint8_t): 1Hz、2Hz、4Hz、6Hz、8Hz、10Hz、12Hz、14Hz、16Hz、18Hz、20Hz、22Hz、24Hz、26Hz、28Hz、30Hz、32Hz、34Hz\n', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='TwoDModeDetectionRate (uint8_t): 1Hz、2Hz、4Hz、6Hz、8Hz、10Hz、12Hz、14Hz、16Hz、18Hz、20Hz、22Hz、24Hz、26Hz、28Hz、30Hz、32Hz、34Hz\n', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='調整偵測次數越高反應越靈敏，系統耗電增加。可以依照耗電需求微調參數以達到最佳效\n', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1

        subWindow.mainloop()
    elif option == 'TargetParameters':
        subWindow = tk.Toplevel(root)
        subWindow.geometry('%dx%d+%d+%d' % (subw, subr, subx, suby))
        subWindow.title('[Chicony] Target Parameters')
        #subWindow.configure(bg=sub_bg)

        jpg = Image.open("./RadarUI/TargetParameters00.PNG")
        jpg_resized = jpg.resize((720, 80))  
        jpg_show = ImageTk.PhotoImage(jpg_resized)
        text_jpg = tk.Label(subWindow, image=jpg_show, height=80, width=720)
        text_jpg.grid(row=sub_row, column=0, sticky='w')
        sub_row+=1

        jpg1 = Image.open("./RadarUI/TargetParameters01.PNG")
        jpg_resized1 = jpg1.resize((720, 80))  
        jpg_show1 = ImageTk.PhotoImage(jpg_resized1)
        text_jpg1 = tk.Label(subWindow, image=jpg_show1, height=80, width=720)
        text_jpg1.grid(row=sub_row, column=0, sticky='w', pady=5)

        sub_row+=1
        Message(subWindow, text='\nMotionRangeMin(uint16_t): Min range in cm\n', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='MotionRangeMax(uint16_t): Max range in cm\n', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='MotionAngleMax(uint8_t) : Azimuth, if this value is 60, then the system accepts targets between -30~+30 degree.\n', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1

        subWindow.mainloop()
    elif option == 'TrackingParameters':
        subWindow = tk.Toplevel(root)
        subWindow.geometry('%dx%d+%d+%d' % (subw, subr, subx, suby))
        subWindow.title('[Chicony] Tracking Parameters')
        #subWindow.configure(bg=sub_bg)

        jpg = Image.open("./RadarUI/TrackingParameters00.PNG")
        jpg_resized = jpg.resize((720, 80))  
        jpg_show = ImageTk.PhotoImage(jpg_resized)
        text_jpg = tk.Label(subWindow, image=jpg_show, height=100, width=720)
        text_jpg.grid(row=sub_row, column=0, sticky='w')
        sub_row+=1

        Message(subWindow, text='\nTracking init_times (uint8_t): 判斷為可用數據的初始偵測次數。(單位 : 筆數)', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='註1 : 當環境雜訊過多，建議調整該參數降低雜訊被判斷成可用數據。', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='註2 : 減少init數值相當於增加靈敏度，增加init數值相當於減少靈敏度。', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='\nTracking delete_times (uint8_t): 數據延遲刪除次數。(單位 : 筆數)', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='註1 : 當init與delete皆設定為1時，系統顯示資料為原始數據。', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='註2 : init參數需小於delete參數。否則系統無法將數值判斷為可用數據。', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='        在init次數等於delete時該筆數值已被系統判定成刪除資料。', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1

        subWindow.mainloop()
    elif option == 'ROISetting':
        subWindow = tk.Toplevel(root)
        subWindow.geometry('%dx%d+%d+%d' % (subw, subr, subx, suby))
        subWindow.title('[Chicony] ROI Setting')
        #subWindow.configure(bg=sub_bg)

        jpg = Image.open("./RadarUI/ROISetting00.PNG")
        jpg_resized = jpg.resize((720, 100))  
        jpg_show = ImageTk.PhotoImage(jpg_resized)
        text_jpg = tk.Label(subWindow, image=jpg_show, height=100, width=720)
        text_jpg.grid(row=sub_row, column=0, sticky='w')
        sub_row+=1

        jpg1 = Image.open("./RadarUI/ROISetting01.PNG")
        jpg_resized1 = jpg1.resize((720, 100))  
        jpg_show1 = ImageTk.PhotoImage(jpg_resized1)
        text_jpg1 = tk.Label(subWindow, image=jpg_show1, height=100, width=720)
        text_jpg1.grid(row=sub_row, column=0, sticky='w', pady=5)
        sub_row+=1

        Message(subWindow, text='\nROI_RangeMin (uint16_t): ROI minimum detection range (cm).', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='註1 : 設定值以10的倍數進行參數設定, 註2 : ROI Range Maximum需小於Range Max參數設定。\n', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='ROI_RangeMax (uint16_t) : ROI maximim detection range (cm).', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='註1 : 設定值以10的倍數進行參數設定, 註2 : ROI Range Minimum需大於Range Min參數設定。\n', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='ROI_AngleMax (uint8_t) : ROI maximum detection range.', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='註1. ROI Angle Maximum需小於Angle Max參數設定。\n', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1

        subWindow.mainloop()
    elif option == 'ROISelect':
        sub_width = 440
        subw = 900
        subr = 520
        subWindow = tk.Toplevel(root)
        subWindow.geometry('%dx%d+%d+%d' % (subw, subr, subx, suby))
        subWindow.title('[Chicony] ROI Select - Buffer1')
        #subWindow.configure(bg=sub_bg)

        jpg = Image.open("./RadarUI/ROISelect00.PNG")
        jpg_resized = jpg.resize((360, 120))  
        jpg_show = ImageTk.PhotoImage(jpg_resized)
        text_jpg = tk.Label(subWindow, image=jpg_show, height=120, width=360)
        text_jpg.grid(row=sub_row, column=0, sticky='w')
        sub_row+=1

        Message(subWindow, text='ROI_Select_Buf[0]-ROI_Select_Buf[7] : ROI Zone from 1 - 64 . Each bit represent ROI zone .', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='Bit set 0 : ROI zone select, Bit set 1 : ROI zone ignore.\n', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='Set example           : 55 AA 31 38 08 F8 F8 F8 E7 E7 E7 E7 1F 5D', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='Response example : 55 AA 31 39 08 F8 F8 F8 E7 E7 E7 E7 1F 5D', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='F8 : ROI_Select_Buf[0] = 0b11111000', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='F8 : ROI_Select_Buf[1] = 0b11111000', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='F8 : ROI_Select_Buf[2] = 0b11111000', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='E7 : ROI_Select_Buf[3] = 0b11100111', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='E7 : ROI_Select_Buf[4] = 0b11100111', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='E7 : ROI_Select_Buf[5] = 0b11100111', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='E7 : ROI_Select_Buf[6] = 0b11100111', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='1F : ROI_Select_Buf[7] = 0b00011111', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1

        sub_row = 0
        sub_col = 1
        jpg1 = Image.open("./RadarUI/ROISelect01.PNG")
        jpg_resized1 = jpg1.resize((360, 120))  
        jpg_show1 = ImageTk.PhotoImage(jpg_resized1)
        text_jpg1 = tk.Label(subWindow, image=jpg_show1, height=120, width=360)
        text_jpg1.grid(row=sub_row, column=sub_col, sticky='w')
        sub_row+=1

        Message(subWindow, text='ROI_Select_Buf[0]-ROI_Select_Buf[1] : ROI Zone from 65 - 80 . Each bit represent ROI zone (Current firmware support 80 ROI Zone to select) .', font=sub_font, width=sub_width).grid(row=sub_row, column=sub_col, sticky='w')
        sub_row+=1
        Message(subWindow, text='Bit set 0 : ROI zone select, Bit set 1 : ROI zone ignore.\n', font=sub_font, width=sub_width).grid(row=sub_row, column=sub_col, sticky='w')
        sub_row+=1
        Message(subWindow, text='Set example           : 55 AA 31 41 08 1F 1F 00 00 00 00 00 00 C2 ', font=sub_font, width=sub_width).grid(row=sub_row, column=sub_col, sticky='w')
        sub_row+=1
        Message(subWindow, text='Response example : 55 AA 31 42 08 1F 1F 00 00 00 00 00 00 C2', font=sub_font, width=sub_width).grid(row=sub_row, column=sub_col, sticky='w')
        sub_row+=1
        Message(subWindow, text='1F : ROI_Select_Buf[0] = 0b00011111', font=sub_font, width=sub_width).grid(row=sub_row, column=sub_col, sticky='w')
        sub_row+=1
        Message(subWindow, text='1F : ROI_Select_Buf[1] = 0b00011111', font=sub_font, width=sub_width).grid(row=sub_row, column=sub_col, sticky='w')
        sub_row+=1

        subWindow.mainloop()
    elif option == 'GainConfigs':
        subWindow = tk.Toplevel(root)
        subWindow.geometry('%dx%d+%d+%d' % (subw, subr, subx, suby))
        subWindow.title('[Chicony] Gain Configs')
        #subWindow.configure(bg=sub_bg)

        jpg = Image.open("./RadarUI/GainConfigs00.PNG")
        jpg_resized = jpg.resize((720, 80))  
        jpg_show = ImageTk.PhotoImage(jpg_resized)
        text_jpg = tk.Label(subWindow, image=jpg_show, height=120, width=720)
        text_jpg.grid(row=sub_row, column=0, sticky='w')
        sub_row+=1

        jpg1 = Image.open("./RadarUI/GainConfigs01.PNG")
        jpg_resized1 = jpg1.resize((720, 80))  
        jpg_show1 = ImageTk.PhotoImage(jpg_resized1)
        text_jpg1 = tk.Label(subWindow, image=jpg_show1, height=80, width=720)
        text_jpg1.grid(row=sub_row, column=0, sticky='w')
        sub_row+=1

        jpg2 = Image.open("./RadarUI/GainConfigs02.PNG")
        jpg_resized2 = jpg2.resize((720, 80))  
        jpg_show2 = ImageTk.PhotoImage(jpg_resized2)
        text_jpg2 = tk.Label(subWindow, image=jpg_show2, height=80, width=720)
        text_jpg2.grid(row=sub_row, column=0, sticky='w')
        sub_row+=1

        jpg3 = Image.open("./RadarUI/GainConfigs03.PNG")
        jpg_resized3 = jpg3.resize((720, 80))  
        jpg_show3 = ImageTk.PhotoImage(jpg_resized3)
        text_jpg3 = tk.Label(subWindow, image=jpg_show3, height=120, width=720)
        text_jpg3.grid(row=sub_row, column=0, sticky='w')
        sub_row+=1

        subWindow.mainloop()
    elif option == 'AngleParameters':
        subWindow = tk.Toplevel(root)
        subWindow.geometry('%dx%d+%d+%d' % (subw, subr, subx, suby))
        subWindow.title('[Chicony] Angle Parameters')
        #subWindow.configure(bg=sub_bg)

        jpg = Image.open("./RadarUI/AngleParameters00.PNG")
        jpg_resized = jpg.resize((720, 80))  
        jpg_show = ImageTk.PhotoImage(jpg_resized)
        text_jpg = tk.Label(subWindow, image=jpg_show, height=80, width=720)
        text_jpg.grid(row=sub_row, column=0, sticky='w')
        sub_row+=1

        jpg1 = Image.open("./RadarUI/AngleParameters01.PNG")
        jpg_resized1 = jpg1.resize((720, 80))  
        jpg_show1 = ImageTk.PhotoImage(jpg_resized1)
        text_jpg1 = tk.Label(subWindow, image=jpg_show1, height=80, width=720)
        text_jpg1.grid(row=sub_row, column=0, sticky='w')
        sub_row+=1

        Message(subWindow, text='angle_reverse (uint8_t): Output data angle sign reverse. [ON] = 1, 反轉，[OFF] = 0, 不反轉。', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='angle_offset (int16_t) : 角度補償參數, 參數範圍 : +90到-90', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='註 : 根據中心測試調整該參數需補償角度數值。', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='angle_rate (float) : 角度補償參數', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='調整偵測次數越高反應越靈敏，系統耗電增加。可以依照耗電需求微調參數以達到最佳效\n', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='Set example            : 55 AA 31 44 08 00 00 00 00 CD CC 8C 3F 9C', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='Response example : 55 AA 31 45 08 00 00 00 00 CD CC 8C 3F 9C', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='00 : angle_reverse OFF', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='0000 : angle_offset 0', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1
        Message(subWindow, text='CDCC8C3F : angle_rate 1.1', font=sub_font, width=sub_width).grid(row=sub_row, column=0, sticky='w')
        sub_row+=1

        subWindow.mainloop()
    else:
        print("option is invailid!")


'''
#
## Label
#
'''
_Text_fg = '#000000'
_title_fg = '#A86E00'
_subtitle_fg = '#8D00F5'

label_RadarID = tk.Label(root, text="RadarID", bg=_root_bg, fg=_title_fg)

label_Return = tk.Label(root, text="NULL", bg=_root_bg, fg=_Text_fg)

label_FwVer = tk.Label(root, text="FwVer", bg=_root_bg, fg=_Text_fg)
label_cecFwVer = tk.Label(root, text="cecFwVer", bg=_root_bg, fg=_Text_fg)

label_SystemConfiguration = tk.Label(root, text="System Configuration", bg=_root_bg, fg=_title_fg)

jpg_chicony = Image.open("./RadarUI/chicony.png")
jpg_resized_chicony = jpg_chicony.resize((200, 100))  
jpg_show_chicony = ImageTk.PhotoImage(jpg_resized_chicony)
label_chicony = tk.Label(root, image=jpg_show_chicony, height=100, width=200)
#label_chicony = tk.Label(root, text="Chicony VIP", font=("Lucida Console", 20, "bold", "italic"), bg=_root_bg, fg="#6E6EFF")

label_ModeParameters = tk.Label(root, text="Mode Parameters", bg=_root_bg, fg=_title_fg)
label_ModeParameters_Mode = tk.Label(root, text="MODE:", bg=_root_bg, fg=_subtitle_fg)
label_ModeParameters_Mode_Text = tk.Label(root, text=_label_ModeParameters_Mode_Text, bg=_root_bg, fg=_Text_fg)
label_ModeParameters_SentryTimes = tk.Label(root, text="Sentry to 2D(times):", bg=_root_bg, fg=_subtitle_fg)
label_ModeParameters_SentryTimes_Text = tk.Label(root, text=_label_ModeParameters_SentryTimes_Text, bg=_root_bg, fg=_Text_fg)
label_ModeParameters_2DTimes = tk.Label(root, text="2D to Sentry(times):", bg=_root_bg, fg=_subtitle_fg)
label_ModeParameters_2DTimes_Text = tk.Label(root, text=_label_ModeParameters_2DTimes_Text, bg=_root_bg, fg=_Text_fg)

label_SensingParameters = tk.Label(root, text="Sensing Parameters", bg=_root_bg, fg=_title_fg)
label_SensingParameters_SentryThr = tk.Label(root, text="Sentry Mode Threshold:", bg=_root_bg, fg=_subtitle_fg)
label_SensingParameters_SentryThr_Text = tk.Label(root, text=_label_SensingParameters_SentryThr_Text, bg=_root_bg, fg=_Text_fg)
label_SensingParameters_2DThr = tk.Label(root, text="2D Mode Threshold:", bg=_root_bg, fg=_subtitle_fg)
label_SensingParameters_2DThr_Text = tk.Label(root, text=_label_SensingParameters_2DThr_Text, bg=_root_bg, fg=_Text_fg)

label_DutyParameters = tk.Label(root, text="Duty Parameters", bg=_root_bg, fg=_title_fg)
label_DutyParameters_Enable = tk.Label(root, text="Duty Enable:", bg=_root_bg, fg=_subtitle_fg)
label_DutyParameters_Enable_Text = tk.Label(root, text=_label_DutyParameters_Enable_Text, bg=_root_bg, fg=_Text_fg)
label_DutyParameters_SentryDetectRate = tk.Label(root, text="SentryMode Detection Rate(Hz):", bg=_root_bg, fg=_subtitle_fg)
label_DutyParameters_SentryDetectRate_Text = tk.Label(root, text=_label_DutyParameters_SentryDetectRate_Text, bg=_root_bg, fg=_Text_fg)
label_DutyParameters_2DDetectRate = tk.Label(root, text="TwoDMode Detection Rate(Hz):", bg=_root_bg, fg=_subtitle_fg)
label_DutyParameters_2DDetectRate_Text = tk.Label(root, text=_label_DutyParameters_2DDetectRate_Text, bg=_root_bg, fg=_Text_fg)

label_TargetParameters = tk.Label(root, text="Target Parameters", bg=_root_bg, fg=_title_fg)
label_TargetParameters_RangeMax = tk.Label(root, text="Range Max(cm):", bg=_root_bg, fg=_subtitle_fg)
label_TargetParameters_RangeMax_Text = tk.Label(root, text=_label_TargetParameters_RangeMax_Text, bg=_root_bg, fg=_Text_fg)
label_TargetParameters_RangeMin = tk.Label(root, text="Range Min(cm):", bg=_root_bg, fg=_subtitle_fg)
label_TargetParameters_RangeMin_Text = tk.Label(root, text=_label_TargetParameters_RangeMin_Text, bg=_root_bg, fg=_Text_fg)
label_TargetParameters_AngleMax = tk.Label(root, text="Angle Max(degree):", bg=_root_bg, fg=_subtitle_fg)
label_TargetParameters_AngleMax_Text = tk.Label(root, text=_label_TargetParameters_AngleMax_Text, bg=_root_bg, fg=_Text_fg)

label_TrackingParameters = tk.Label(root, text="Tracking Parameters", bg=_root_bg, fg=_title_fg)
label_TrackingParameters_Init = tk.Label(root, text="init:", bg=_root_bg, fg=_subtitle_fg)
label_TrackingParameters_Init_Text = tk.Label(root, text=_label_TrackingParameters_Init_Text, bg=_root_bg, fg=_Text_fg)
label_TrackingParameters_Delete = tk.Label(root, text="delete", bg=_root_bg, fg=_subtitle_fg)
label_TrackingParameters_Delete_Text = tk.Label(root, text=_label_TrackingParameters_Delete_Text, bg=_root_bg, fg=_Text_fg)

label_ROISetting = tk.Label(root, text="ROI Setting", bg=_root_bg, fg=_title_fg)
label_ROISetting_ROIRangeMax = tk.Label(root, text="ROI Range Max(cm):", bg=_root_bg, fg=_subtitle_fg)
label_ROISetting_ROIRangeMax_Text = tk.Label(root, text=_label_ROISetting_ROIRangeMax_Text, bg=_root_bg, fg=_Text_fg)
label_ROISetting_ROIRangeMin = tk.Label(root, text="ROI Range Min(cm):", bg=_root_bg, fg=_subtitle_fg)
label_ROISetting_ROIRangeMin_Text = tk.Label(root, text=_label_ROISetting_ROIRangeMin_Text, bg=_root_bg, fg=_Text_fg)
label_ROISetting_ROIAngleMax = tk.Label(root, text="ROI Angle Max(degree):", bg=_root_bg, fg=_subtitle_fg)
label_ROISetting_ROIAngleMax_Text = tk.Label(root, text=_label_ROISetting_ROIAngleMax_Text, bg=_root_bg, fg=_Text_fg)

label_ROISelect = tk.Label(root, text="ROI Select", bg=_root_bg, fg=_title_fg)
label_ROISelect_Buffer1 = tk.Label(root, text="Buffer1:", bg=_root_bg, fg=_subtitle_fg)
label_ROISelect_Buffer1_Text = tk.Label(root, text=_label_ROISelect_Buffer1_Text, bg=_root_bg, fg=_Text_fg)
label_ROISelect_Buffer2 = tk.Label(root, text="Buffer2:", bg=_root_bg, fg=_subtitle_fg)
label_ROISelect_Buffer2_Text = tk.Label(root, text=_label_ROISelect_Buffer2_Text, bg=_root_bg, fg=_Text_fg)

label_GainConfigs = tk.Label(root, text="Gain Configs", bg=_root_bg, fg=_title_fg)
label_GainConfigs_Sentry_TxGain = tk.Label(root, text="Sentry TxGain", bg=_root_bg, fg=_subtitle_fg)
label_GainConfigs_Sentry_TxGain_Text = tk.Label(root, text=_label_GainConfigs_Sentry_TxGain_Text, bg=_root_bg, fg=_Text_fg)
label_GainConfigs_Sentry_RxGain = tk.Label(root, text="Sentry RxGain", bg=_root_bg, fg=_subtitle_fg)
label_GainConfigs_Sentry_RxGain_Text = tk.Label(root, text=_label_GainConfigs_Sentry_RxGain_Text, bg=_root_bg, fg=_Text_fg)
label_GainConfigs_Sentry_Rx01HPF = tk.Label(root, text="Sentry Rx01HPF", bg=_root_bg, fg=_subtitle_fg)
label_GainConfigs_Sentry_Rx01HPF_Text = tk.Label(root, text=_label_GainConfigs_Sentry_Rx01HPF_Text, bg=_root_bg, fg=_Text_fg)
label_GainConfigs_Sentry_Rx02HPF = tk.Label(root, text="Sentry Rx02HPF", bg=_root_bg, fg=_subtitle_fg)
label_GainConfigs_Sentry_Rx02HPF_Text = tk.Label(root, text=_label_GainConfigs_Sentry_Rx02HPF_Text, bg=_root_bg, fg=_Text_fg)
label_GainConfigs_2D_TxGain = tk.Label(root, text="2D TxGain", bg=_root_bg, fg=_subtitle_fg)
label_GainConfigs_2D_TxGain_Text = tk.Label(root, text=_label_GainConfigs_2D_TxGain_Text, bg=_root_bg, fg=_Text_fg)
label_GainConfigs_2D_Rx01Gain = tk.Label(root, text="2D Rx01Gain", bg=_root_bg, fg=_subtitle_fg)
label_GainConfigs_2D_Rx01Gain_Text = tk.Label(root, text=_label_GainConfigs_2D_Rx01Gain_Text, bg=_root_bg, fg=_Text_fg)
label_GainConfigs_2D_Rx02Gain = tk.Label(root, text="2D Rx02Gain", bg=_root_bg, fg=_subtitle_fg)
label_GainConfigs_2D_Rx02Gain_Text = tk.Label(root, text=_label_GainConfigs_2D_Rx02Gain_Text, bg=_root_bg, fg=_Text_fg)
label_GainConfigs_2D_Rx01HPF = tk.Label(root, text="2D Rx01HPF", bg=_root_bg, fg=_subtitle_fg)
label_GainConfigs_2D_Rx01HPF_Text = tk.Label(root, text=_label_GainConfigs_2D_Rx01HPF_Text, bg=_root_bg, fg=_Text_fg)
label_GainConfigs_2D_Rx02HPF = tk.Label(root, text="2D Rx02HPF", bg=_root_bg, fg=_subtitle_fg)
label_GainConfigs_2D_Rx02HPF_Text = tk.Label(root, text=_label_GainConfigs_2D_Rx02HPF_Text, bg=_root_bg, fg=_Text_fg)

label_AngleParameters = tk.Label(root, text="Angle Parameters", bg=_root_bg, fg=_title_fg)
label_AngleParameters_Reverse = tk.Label(root, text="Angle Reverse", bg=_root_bg, fg=_subtitle_fg)
label_AngleParameters_Reverse_Text = tk.Label(root, text=_label_AngleParameters_Reverse_Text, bg=_root_bg, fg=_Text_fg)
label_AngleParameters_Compensation = tk.Label(root, text="Angle Compensation", bg=_root_bg, fg=_subtitle_fg)
label_AngleParameters_Compensation_Text = tk.Label(root, text=_label_AngleParameters_Compensation_Text, bg=_root_bg, fg=_Text_fg)
label_AngleParameters_Rate = tk.Label(root, text="Angle Rate", bg=_root_bg, fg=_subtitle_fg)
label_AngleParameters_Rate_Text = tk.Label(root, text=_label_AngleParameters_Rate_Text, bg=_root_bg, fg=_Text_fg)

'''
#
## Entry
#
'''
entry_RadarID = tk.Entry(root)
entry_RadarID.insert(0, 0)

entry_ModeParameters_Mode = tk.Entry(root)
entry_ModeParameters_Mode.insert(0, _label_ModeParameters_Mode_Text)
entry_ModeParameters_SentryTimes = tk.Entry(root)
entry_ModeParameters_SentryTimes.insert(0, _label_ModeParameters_SentryTimes_Text)
entry_ModeParameters_2DTimes = tk.Entry(root)
entry_ModeParameters_2DTimes.insert(0, _label_ModeParameters_2DTimes_Text)

entry_SensingParameters_SentryThr = tk.Entry(root)
entry_SensingParameters_SentryThr.insert(0, _label_SensingParameters_SentryThr_Text)
entry_SensingParameters_2DThr = tk.Entry(root)
entry_SensingParameters_2DThr.insert(0, _label_SensingParameters_2DThr_Text)

entry_DutyParameters_Enable = tk.Entry(root)
entry_DutyParameters_Enable.insert(0, _label_DutyParameters_Enable_Text)
entry_DutyParameters_SentryDetectRate = tk.Entry(root)
entry_DutyParameters_SentryDetectRate.insert(0, _label_DutyParameters_SentryDetectRate_Text)
entry_DutyParameters_2DDetectRate = tk.Entry(root)
entry_DutyParameters_2DDetectRate.insert(0, 20)     #_label_DutyParameters_2DDetectRate_Text

entry_TargetParameters_RangeMax = tk.Entry(root)
entry_TargetParameters_RangeMax.insert(0, 700)      #_label_TargetParameters_RangeMax_Text
entry_TargetParameters_RangeMin = tk.Entry(root)
entry_TargetParameters_RangeMin.insert(0, _label_TargetParameters_RangeMin_Text)
entry_TargetParameters_AngleMax = tk.Entry(root)
entry_TargetParameters_AngleMax.insert(0, _label_TargetParameters_AngleMax_Text)

entry_TrackingParameters_Init = tk.Entry(root)
entry_TrackingParameters_Init.insert(0, _label_TrackingParameters_Init_Text)
entry_TrackingParameters_Delete = tk.Entry(root)
entry_TrackingParameters_Delete.insert(0, _label_TrackingParameters_Delete_Text)

entry_ROISetting_ROIRangeMin = tk.Entry(root)
entry_ROISetting_ROIRangeMin.insert(0, _label_ROISetting_ROIRangeMin_Text)
entry_ROISetting_ROIRangeMax = tk.Entry(root)
entry_ROISetting_ROIRangeMax.insert(0, 700)     #_label_ROISetting_ROIRangeMax_Text
entry_ROISetting_ROIAngleMax = tk.Entry(root)
entry_ROISetting_ROIAngleMax.insert(0, _label_ROISetting_ROIAngleMax_Text)

entry_ROISelect_Buffer1 = tk.Entry(root)
entry_ROISelect_Buffer1.insert(0, _label_ROISelect_Buffer1_Text)
entry_ROISelect_Buffer2 = tk.Entry(root)
entry_ROISelect_Buffer2.insert(0, _label_ROISelect_Buffer2_Text[0:4])

entry_GainConfigs_Sentry_TxGain = tk.Entry(root)
entry_GainConfigs_Sentry_TxGain.insert(0, _label_GainConfigs_Sentry_TxGain_Text)
entry_GainConfigs_Sentry_RxGain = tk.Entry(root)
entry_GainConfigs_Sentry_RxGain.insert(0, _label_GainConfigs_Sentry_RxGain_Text)
entry_GainConfigs_Sentry_Rx01HPF = tk.Entry(root)
entry_GainConfigs_Sentry_Rx01HPF.insert(0, _label_GainConfigs_Sentry_Rx01HPF_Text)
entry_GainConfigs_Sentry_Rx02HPF = tk.Entry(root)
entry_GainConfigs_Sentry_Rx02HPF.insert(0, _label_GainConfigs_Sentry_Rx02HPF_Text)
entry_GainConfigs_2D_TxGain = tk.Entry(root)
entry_GainConfigs_2D_TxGain.insert(0, 5)    #_label_GainConfigs_2D_TxGain_Text
entry_GainConfigs_2D_Rx01Gain = tk.Entry(root)
entry_GainConfigs_2D_Rx01Gain.insert(0, 5)  #_label_GainConfigs_2D_Rx01Gain_Text
entry_GainConfigs_2D_Rx02Gain = tk.Entry(root)
entry_GainConfigs_2D_Rx02Gain.insert(0, 5)  #_label_GainConfigs_2D_Rx02Gain_Text
entry_GainConfigs_2D_Rx01HPF = tk.Entry(root)
entry_GainConfigs_2D_Rx01HPF.insert(0, 4)  #_label_GainConfigs_2D_Rx01HPF_Text
entry_GainConfigs_2D_Rx02HPF = tk.Entry(root)
entry_GainConfigs_2D_Rx02HPF.insert(0, 4)  #_label_GainConfigs_2D_Rx02HPF_Text

entry_AngleParameters_Reverse = tk.Entry(root)
entry_AngleParameters_Reverse.insert(0, _label_AngleParameters_Reverse_Text)
entry_AngleParameters_Compensation = tk.Entry(root)
entry_AngleParameters_Compensation.insert(0, _label_AngleParameters_Compensation_Text)
entry_AngleParameters_Rate = tk.Entry(root)
entry_AngleParameters_Rate.insert(0, _label_AngleParameters_Rate_Text)


'''
#
## Button
#
'''
bt_FwVer = tk.Button(root, text='FwVer', command=partial(click_radar_command, 'fwver'), relief="groove",
             state=tk.ACTIVE,                   #設定按鈕的狀態
            )
bt_cecFwVer = tk.Button(root, text='cecFwVer', command=partial(click_radar_command, 'cecfwver'), relief="groove",
             state=tk.ACTIVE,                   #設定按鈕的狀態
            )

bt_SystemConfiguration = tk.Button(root, text='System Configuration', bd=-1, bg=_root_bg, fg=_title_fg, command=partial(click_radar_messagebox, 'SystemConfiguration'), relief="flat",
             #state=tk.ACTIVE,                   #設定按鈕的狀態
            )
bt_Reset = tk.Button(root, text='RESET', command=partial(click_radar_command, 'reset'), relief="groove",
             state=tk.ACTIVE,                   #設定按鈕的狀態
            )
bt_Reboot = tk.Button(root, text='REBOOT', command=partial(click_radar_command, 'reboot'), relief="groove",
             state=tk.ACTIVE,                   #設定按鈕的狀態
            )
bt_Default = tk.Button(root, text='DEFAULT', command=partial(click_radar_command, 'default'), relief="groove",
             state=tk.ACTIVE,                   #設定按鈕的狀態
            )

bt_ModeParameters = tk.Button(root, text='Mode Parameters', bd=-1, bg=_root_bg, fg=_title_fg, command=partial(click_radar_messagebox, 'ModeParameters'), relief="flat",
             #state=tk.ACTIVE,                   #設定按鈕的狀態
            )
bt_ModeParameters_Get = tk.Button(root, text='GET', command=partial(click_radar_command, 'ModeParameters_Get'), relief="groove",
             state=tk.ACTIVE,                   #設定按鈕的狀態
            )
bt_ModeParameters_Set = tk.Button(root, text='SET', command=partial(click_radar_command, 'ModeParameters_Set'), relief="groove",
             state=tk.DISABLED,                   #設定按鈕的狀態
            )

bt_SensingParameters = tk.Button(root, text='Sensing Parameters', bd=-1, bg=_root_bg, fg=_title_fg, command=partial(click_radar_messagebox, 'SensingParameters'), relief="flat",
             #state=tk.ACTIVE,                   #設定按鈕的狀態
            )
bt_SensingParameters_Get = tk.Button(root, text='GET', command=partial(click_radar_command, 'SensingParameters_Get'), relief="groove",
             state=tk.ACTIVE,                   #設定按鈕的狀態
            )
bt_SensingParameters_Set = tk.Button(root, text='SET', command=partial(click_radar_command, 'SensingParameters_Set'), relief="groove",
             state=tk.ACTIVE,                   #設定按鈕的狀態
            )

bt_DutyParameters = tk.Button(root, text='Duty Parameters', bd=-1, bg=_root_bg, fg=_title_fg, command=partial(click_radar_messagebox, 'DutyParameters'), relief="flat",
             #state=tk.ACTIVE,                   #設定按鈕的狀態
            )
bt_DutyParameters_Get = tk.Button(root, text='GET', command=partial(click_radar_command, 'DutyParameters_Get'), relief="groove",
             state=tk.ACTIVE,                   #設定按鈕的狀態
            )
bt_DutyParameters_Set = tk.Button(root, text='SET', command=partial(click_radar_command, 'DutyParameters_Set'), relief="groove",
             state=tk.ACTIVE,                   #設定按鈕的狀態
            )

bt_TargetParameters = tk.Button(root, text='Target Parameters', bd=-1, bg=_root_bg, fg=_title_fg, command=partial(click_radar_messagebox, 'TargetParameters'), relief="flat",
             #state=tk.DISABLED,                   #設定按鈕的狀態
            )
bt_TargetParameters_Get = tk.Button(root, text='GET', command=partial(click_radar_command, 'TargetParameters_Get'), relief="groove",
             state=tk.ACTIVE,                   #設定按鈕的狀態
            )
bt_TargetParameters_Set = tk.Button(root, text='SET', command=partial(click_radar_command, 'TargetParameters_Set'), relief="groove",
             state=tk.ACTIVE,                   #設定按鈕的狀態
            )

bt_TrackingParameters = tk.Button(root, text='Tracking Parameters', bd=-1, bg=_root_bg, fg=_title_fg, command=partial(click_radar_messagebox, 'TrackingParameters'), relief="flat",
             #state=tk.ACTIVE,                   #設定按鈕的狀態
            )
bt_TrackingParameters_Get = tk.Button(root, text='GET', command=partial(click_radar_command, 'TrackingParameters_Get'), relief="groove",
             state=tk.ACTIVE,                   #設定按鈕的狀態
            )
bt_TrackingParameters_Set = tk.Button(root, text='SET', command=partial(click_radar_command, 'TrackingParameters_Set'), relief="groove",
             state=tk.ACTIVE,                   #設定按鈕的狀態
            )

bt_ROISetting = tk.Button(root, text='ROI Setting', bd=-1, bg=_root_bg, fg=_title_fg, command=partial(click_radar_messagebox, 'ROISetting'), relief="flat",
             #state=tk.ACTIVE,                   #設定按鈕的狀態
            )
bt_ROISetting_Get = tk.Button(root, text='GET', command=partial(click_radar_command, 'ROISetting_Get'), relief="groove",
             state=tk.ACTIVE,                   #設定按鈕的狀態
            )
bt_ROISetting_Set = tk.Button(root, text='SET', command=partial(click_radar_command, 'ROISetting_Set'), relief="groove",
             state=tk.ACTIVE,                   #設定按鈕的狀態
            )

bt_ROISelect = tk.Button(root, text='ROI Select', bd=-1, bg=_root_bg, fg=_title_fg, command=partial(click_radar_messagebox, 'ROISelect'), relief="flat",
             #state=tk.ACTIVE,                   #設定按鈕的狀態
            )
bt_ROISelect_Buffer1_Get = tk.Button(root, text='GET', command=partial(click_radar_command, 'ROISelect_Buffer1_Get'), relief="groove",
             state=tk.ACTIVE,                   #設定按鈕的狀態
            )
bt_ROISelect_Buffer1_Set = tk.Button(root, text='SET', command=partial(click_radar_command, 'ROISelect_Buffer1_Set'), relief="groove",
             state=tk.ACTIVE,                   #設定按鈕的狀態
            )
bt_ROISelect_Buffer2_Get = tk.Button(root, text='GET', command=partial(click_radar_command, 'ROISelect_Buffer2_Get'), relief="groove",
             state=tk.ACTIVE,                   #設定按鈕的狀態
            )
bt_ROISelect_Buffer2_Set = tk.Button(root, text='SET', command=partial(click_radar_command, 'ROISelect_Buffer2_Set'), relief="groove",
             state=tk.ACTIVE,                   #設定按鈕的狀態
            )

bt_GainConfigs = tk.Button(root, text='Gain Configs', bd=-1, bg=_root_bg, fg=_title_fg, command=partial(click_radar_messagebox, 'GainConfigs'), relief="flat",
             #state=tk.ACTIVE,                   #設定按鈕的狀態
            )
bt_GainConfigs_Get = tk.Button(root, text='GET', command=partial(click_radar_command, 'GainConfigs_Get'), relief="groove",
             state=tk.ACTIVE,                   #設定按鈕的狀態
            )
bt_GainConfigs_Set = tk.Button(root, text='SET', command=partial(click_radar_command, 'GainConfigs_Set'), relief="groove",
             state=tk.ACTIVE,                   #設定按鈕的狀態
            )

bt_AngleParameters = tk.Button(root, text='Angle Parameters', bd=-1, bg=_root_bg, fg=_title_fg, command=partial(click_radar_messagebox, 'AngleParameters'), relief="flat",
             #state=tk.ACTIVE,                   #設定按鈕的狀態
            )
bt_AngleParameters_Get = tk.Button(root, text='GET', command=partial(click_radar_command, 'AngleParameters_Get'), relief="groove",
             state=tk.ACTIVE,                   #設定按鈕的狀態
            )
bt_AngleParameters_Set = tk.Button(root, text='SET', command=partial(click_radar_command, 'AngleParameters_Set'), relief="groove",
             state=tk.ACTIVE,                   #設定按鈕的狀態
            )

bt_plot_start = tk.Button(root, text='Plot Start', command=click_plot_start, relief="groove",
             state=tk.ACTIVE,                   #設定按鈕的狀態
             padx=10,
             pady=15,
            )

bt_queue_parameters = tk.Button(root, text='Queue Paremeters', command=click_queue_parameters, relief="groove",
             state=tk.ACTIVE,                   #設定按鈕的狀態
             pady=15,
            )


'''
#
## Grid Setting
#
'''
_r=0
__r=3
__cstart=6
_pady='3'
_padx='3'
_ipadx='5'

bt_plot_start.grid(row=_r, column=4, rowspan=3, columnspan=2)
bt_queue_parameters.grid(row=_r, column=6, rowspan=3)
label_chicony.grid(row=_r, column=7, rowspan=3, columnspan=3)

label_RadarID.grid(row=_r, column=0, pady=_pady)
entry_RadarID.grid(row=_r, column=1, pady=_pady)
label_Return.grid(row=_r, column=2, columnspan=2, pady=_pady)
_r+=1
bt_FwVer.grid(row=_r, column=0, pady=_pady)
label_FwVer.grid(row=_r, column=1, pady=_pady)
bt_cecFwVer.grid(row=_r, column=2, pady=_pady)
label_cecFwVer.grid(row=_r, column=3, pady=_pady)
_r+=1

#label_SystemConfiguration.grid(row=_r, column=0, pady=_pady)
bt_SystemConfiguration.grid(row=_r, column=0, pady=_pady)
bt_Reset.grid(row=_r, column=1, padx=_padx, pady=_pady)
bt_Reboot.grid(row=_r, column=2, padx='10', pady=_pady)
bt_Default.grid(row=_r, column=3, padx=_padx, pady=_pady)
_r+=1

#label_ModeParameters.grid(row=_r, column=0, pady=_pady)
bt_ModeParameters.grid(row=_r, column=0, pady=_pady)
label_ModeParameters_Mode.grid(row=_r, column=1, pady=_pady)
label_ModeParameters_Mode_Text.grid(row=_r, column=2, pady=_pady)
entry_ModeParameters_Mode.grid(row=_r, column=3, pady=_pady)
bt_ModeParameters_Get.grid(row=_r, column=4, padx=_padx, pady=_pady)
_r+=1
label_ModeParameters_SentryTimes.grid(row=_r, column=1, pady=_pady)
label_ModeParameters_SentryTimes_Text.grid(row=_r, column=2, pady=_pady)
entry_ModeParameters_SentryTimes.grid(row=_r, column=3, pady=_pady)
bt_ModeParameters_Set.grid(row=_r, column=4, padx=_padx, pady=_pady)
_r+=1
label_ModeParameters_2DTimes.grid(row=_r, column=1, pady=_pady)
label_ModeParameters_2DTimes_Text.grid(row=_r, column=2, pady=_pady)
entry_ModeParameters_2DTimes.grid(row=_r, column=3, pady=_pady)
_r+=1

#label_SensingParameters.grid(row=_r, column=0, pady=_pady)
bt_SensingParameters.grid(row=_r, column=0, pady=_pady)
label_SensingParameters_SentryThr.grid(row=_r, column=1, pady=_pady)
label_SensingParameters_SentryThr_Text.grid(row=_r, column=2, pady=_pady)
entry_SensingParameters_SentryThr.grid(row=_r, column=3, pady=_pady)
bt_SensingParameters_Get.grid(row=_r, column=4, padx=_padx, pady=_pady)
_r+=1
label_SensingParameters_2DThr.grid(row=_r, column=1, pady=_pady)
label_SensingParameters_2DThr_Text.grid(row=_r, column=2, pady=_pady)
entry_SensingParameters_2DThr.grid(row=_r, column=3, pady=_pady)
bt_SensingParameters_Set.grid(row=_r, column=4, padx=_padx, pady=_pady)
_r+=1

#label_DutyParameters.grid(row=_r, column=0, pady=_pady)
bt_DutyParameters.grid(row=_r, column=0, pady=_pady)
label_DutyParameters_Enable.grid(row=_r, column=1, pady=_pady)
label_DutyParameters_Enable_Text.grid(row=_r, column=2, pady=_pady)
entry_DutyParameters_Enable.grid(row=_r, column=3, pady=_pady)
bt_DutyParameters_Get.grid(row=_r, column=4, padx=_padx, pady=_pady)
_r+=1
label_DutyParameters_SentryDetectRate.grid(row=_r, column=1, pady=_pady)
label_DutyParameters_SentryDetectRate_Text.grid(row=_r, column=2, pady=_pady)
entry_DutyParameters_SentryDetectRate.grid(row=_r, column=3, pady=_pady)
bt_DutyParameters_Set.grid(row=_r, column=4, padx=_padx, pady=_pady)
_r+=1
label_DutyParameters_2DDetectRate.grid(row=_r, column=1, pady=_pady)
label_DutyParameters_2DDetectRate_Text.grid(row=_r, column=2, pady=_pady)
entry_DutyParameters_2DDetectRate.grid(row=_r, column=3, pady=_pady)
_r+=1

#label_TargetParameters.grid(row=_r, column=0, pady=_pady)
bt_TargetParameters.grid(row=_r, column=0, pady=_pady)
label_TargetParameters_RangeMax.grid(row=_r, column=1, pady=_pady)
label_TargetParameters_RangeMax_Text.grid(row=_r, column=2, pady=_pady)
entry_TargetParameters_RangeMax.grid(row=_r, column=3, pady=_pady)
bt_TargetParameters_Get.grid(row=_r, column=4, padx=_padx, pady=_pady)
_r+=1
label_TargetParameters_RangeMin.grid(row=_r, column=1, pady=_pady)
label_TargetParameters_RangeMin_Text.grid(row=_r, column=2, pady=_pady)
entry_TargetParameters_RangeMin.grid(row=_r, column=3, pady=_pady)
bt_TargetParameters_Set.grid(row=_r, column=4, padx=_padx, pady=_pady)
_r+=1
label_TargetParameters_AngleMax.grid(row=_r, column=1, pady=_pady)
label_TargetParameters_AngleMax_Text.grid(row=_r, column=2, pady=_pady)
entry_TargetParameters_AngleMax.grid(row=_r, column=3, pady=_pady)
_r+=1

#label_TrackingParameters.grid(row=_r, column=0, pady=_pady)
bt_TrackingParameters.grid(row=_r, column=0, pady=_pady)
label_TrackingParameters_Init.grid(row=_r, column=1, pady=_pady)
label_TrackingParameters_Init_Text.grid(row=_r, column=2, pady=_pady)
entry_TrackingParameters_Init.grid(row=_r, column=3, pady=_pady)
bt_TrackingParameters_Get.grid(row=_r, column=4, padx=_padx, pady=_pady)
_r+=1
label_TrackingParameters_Delete.grid(row=_r, column=1, pady=_pady)
label_TrackingParameters_Delete_Text.grid(row=_r, column=2, pady=_pady)
entry_TrackingParameters_Delete.grid(row=_r, column=3, pady=_pady)
bt_TrackingParameters_Set.grid(row=_r, column=4, padx=_padx, pady=_pady)
_r+=1

#label_ROISetting.grid(row=_r, column=0, pady=_pady)
bt_ROISetting.grid(row=_r, column=0, pady=_pady)
label_ROISetting_ROIRangeMax.grid(row=_r, column=1, pady=_pady)
label_ROISetting_ROIRangeMax_Text.grid(row=_r, column=2, pady=_pady)
entry_ROISetting_ROIRangeMax.grid(row=_r, column=3, pady=_pady)
bt_ROISetting_Get.grid(row=_r, column=4, padx=_padx, pady=_pady)
_r+=1
label_ROISetting_ROIRangeMin.grid(row=_r, column=1, pady=_pady)
label_ROISetting_ROIRangeMin_Text.grid(row=_r, column=2, pady=_pady)
entry_ROISetting_ROIRangeMin.grid(row=_r, column=3, pady=_pady)
bt_ROISetting_Set.grid(row=_r, column=4, padx=_padx, pady=_pady)
_r+=1
label_ROISetting_ROIAngleMax.grid(row=_r, column=1, pady=_pady)
label_ROISetting_ROIAngleMax_Text.grid(row=_r, column=2, pady=_pady)
entry_ROISetting_ROIAngleMax.grid(row=_r, column=3, pady=_pady)
_r+=1

#label_ROISelect.grid(row=_r, column=0, pady=_pady)
bt_ROISelect.grid(row=_r, column=0, pady=_pady)
label_ROISelect_Buffer1.grid(row=_r, column=1, pady=_pady)
label_ROISelect_Buffer1_Text.grid(row=_r, column=2, pady=_pady)
entry_ROISelect_Buffer1.grid(row=_r, column=3, pady=_pady)
bt_ROISelect_Buffer1_Get.grid(row=_r, column=4, padx=_padx, pady=_pady)
bt_ROISelect_Buffer1_Set.grid(row=_r, column=5, padx=_padx, pady=_pady)
_r+=1
label_ROISelect_Buffer2.grid(row=_r, column=1, pady=_pady)
label_ROISelect_Buffer2_Text.grid(row=_r, column=2, pady=_pady)
entry_ROISelect_Buffer2.grid(row=_r, column=3, pady=_pady)
bt_ROISelect_Buffer2_Get.grid(row=_r, column=4, padx=_padx, pady=_pady)
bt_ROISelect_Buffer2_Set.grid(row=_r, column=5, padx=_padx, pady=_pady)
_r+=1


__c=__cstart
#label_GainConfigs.grid(row=__r, column=__c, columnspan=4, padx=_padx, pady=_pady)
bt_GainConfigs.grid(row=__r, column=__c, columnspan=4, padx=_padx, pady=_pady)
__c+=1
__r+=1
__c=__cstart
label_GainConfigs_Sentry_TxGain.grid(row=__r, column=__c, padx=_padx, pady=_pady)
__c+=1
label_GainConfigs_Sentry_TxGain_Text.grid(row=__r, column=__c, padx='10', pady=_pady)
__c+=1
entry_GainConfigs_Sentry_TxGain.grid(row=__r, column=__c, padx=_padx, pady=_pady)
__c+=1
bt_GainConfigs_Get.grid(row=__r, column=__c, padx=_padx, pady=_pady)
__c+=1
__r+=1
__c=__cstart
label_GainConfigs_Sentry_RxGain.grid(row=__r, column=__c, padx=_padx, pady=_pady)
__c+=1
label_GainConfigs_Sentry_RxGain_Text.grid(row=__r, column=__c, padx=_padx, pady=_pady)
__c+=1
entry_GainConfigs_Sentry_RxGain.grid(row=__r, column=__c, padx=_padx, pady=_pady)
__c+=1
bt_GainConfigs_Set.grid(row=__r, column=__c, padx=_padx, pady=_pady)
__c+=1
__r+=1
__c=__cstart
label_GainConfigs_Sentry_Rx01HPF.grid(row=__r, column=__c, padx=_padx, pady=_pady)
__c+=1
label_GainConfigs_Sentry_Rx01HPF_Text.grid(row=__r, column=__c, padx=_padx, pady=_pady)
__c+=1
entry_GainConfigs_Sentry_Rx01HPF.grid(row=__r, column=__c, padx=_padx, pady=_pady)
__c+=1
__r+=1
__c=__cstart
label_GainConfigs_Sentry_Rx02HPF.grid(row=__r, column=__c, padx=_padx, pady=_pady)
__c+=1
label_GainConfigs_Sentry_Rx02HPF_Text.grid(row=__r, column=__c, padx=_padx, pady=_pady)
__c+=1
entry_GainConfigs_Sentry_Rx02HPF.grid(row=__r, column=__c, padx=_padx, pady=_pady)
__c+=1
__r+=1
__c=__cstart
label_GainConfigs_2D_TxGain.grid(row=__r, column=__c, padx=_padx, pady=_pady)
__c+=1
label_GainConfigs_2D_TxGain_Text.grid(row=__r, column=__c, padx=_padx, pady=_pady)
__c+=1
entry_GainConfigs_2D_TxGain.grid(row=__r, column=__c, padx=_padx, pady=_pady)
__c+=1
__r+=1
__c=__cstart
label_GainConfigs_2D_Rx01Gain.grid(row=__r, column=__c, padx=_padx, pady=_pady)
__c+=1
label_GainConfigs_2D_Rx01Gain_Text.grid(row=__r, column=__c, padx=_padx, pady=_pady)
__c+=1
entry_GainConfigs_2D_Rx01Gain.grid(row=__r, column=__c, padx=_padx, pady=_pady)
__c+=1
__r+=1
__c=__cstart
label_GainConfigs_2D_Rx02Gain.grid(row=__r, column=__c, padx=_padx, pady=_pady)
__c+=1
label_GainConfigs_2D_Rx02Gain_Text.grid(row=__r, column=__c, padx=_padx, pady=_pady)
__c+=1
entry_GainConfigs_2D_Rx02Gain.grid(row=__r, column=__c, padx=_padx, pady=_pady)
__c+=1
__r+=1
__c=__cstart
label_GainConfigs_2D_Rx01HPF.grid(row=__r, column=__c, padx=_padx, pady=_pady)
__c+=1
label_GainConfigs_2D_Rx01HPF_Text.grid(row=__r, column=__c, padx=_padx, pady=_pady)
__c+=1
entry_GainConfigs_2D_Rx01HPF.grid(row=__r, column=__c, padx=_padx, pady=_pady)
__c+=1
__r+=1
__c=__cstart
label_GainConfigs_2D_Rx02HPF.grid(row=__r, column=__c, padx=_padx, pady=_pady)
__c+=1
label_GainConfigs_2D_Rx02HPF_Text.grid(row=__r, column=__c, padx=_padx, pady=_pady)
__c+=1
entry_GainConfigs_2D_Rx02HPF.grid(row=__r, column=__c, padx=_padx, pady=_pady)
__c+=1
__r+=1
__c=__cstart


#label_AngleParameters.grid(row=__r, column=__c, columnspan=4, padx=_padx, pady=_pady)
bt_AngleParameters.grid(row=__r, column=__c, columnspan=4, padx=_padx, pady=_pady)
__c+=1
__r+=1
__c=__cstart
label_AngleParameters_Reverse.grid(row=__r, column=__c, padx=_padx, pady=_pady)
__c+=1
label_AngleParameters_Reverse_Text.grid(row=__r, column=__c, padx=_padx, pady=_pady)
__c+=1
entry_AngleParameters_Reverse.grid(row=__r, column=__c, padx=_padx, pady=_pady)
__c+=1
bt_AngleParameters_Get.grid(row=__r, column=__c, padx=_padx, pady=_pady)
__c+=1
__r+=1
__c=__cstart
label_AngleParameters_Compensation.grid(row=__r, column=__c, padx=_padx, pady=_pady)
__c+=1
label_AngleParameters_Compensation_Text.grid(row=__r, column=__c, padx=_padx, pady=_pady)
__c+=1
entry_AngleParameters_Compensation.grid(row=__r, column=__c, padx=_padx, pady=_pady)
__c+=1
bt_AngleParameters_Set.grid(row=__r, column=__c, padx=_padx, pady=_pady)
__c+=1
__r+=1
__c=__cstart
label_AngleParameters_Rate.grid(row=__r, column=__c, padx=_padx, pady=_pady)
__c+=1
label_AngleParameters_Rate_Text.grid(row=__r, column=__c, padx=_padx, pady=_pady)
__c+=1
entry_AngleParameters_Rate.grid(row=__r, column=__c, padx=_padx, pady=_pady)
__c+=1
__r+=1
__c=__cstart




root.mainloop()