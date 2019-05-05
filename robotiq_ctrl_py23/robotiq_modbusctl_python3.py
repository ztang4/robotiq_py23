#!/usr/bin/env python
#AUTHUR: ZHIQIANG TANG
#DATE: 2019/04/20
import subprocess
import time
# The last parameter has three choices:
# "c" : stands for closing gripper
# "i" : stands for initiating gripper
# "o" : stands for opening gripper

# init gripper first
subprocess.run(["python","robotiq_modbusctl.py", "i"])
# close gripper
time.sleep(1)
subprocess.run(["python","robotiq_modbusctl.py", "c"])
# open gripper
time.sleep(1)
subprocess.run(["python","robotiq_modbusctl.py", "o"])

