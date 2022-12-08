import numpy as np
import telnetlib

def telnet_test():

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
    
    # key in the password
    #tn.read_until("Password: ")
    #tn.write(str(password)+'\n')
    
    # judging password error prompt
    #if tn.read_until(finish):
        #print "****** login incorrect!\n"

    tn.write(b"./cec_radar_tester_test -Q\n")
    tn.read_until(b"radarOutput obj-0:")
    show = tn.read_very_eager().decode()
    show_split = show.split('\r\n')
    tn.write(b"exit\n")
    tn.close()

if __name__ == "__main__":	
    telnet_test()
