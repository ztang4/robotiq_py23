#!/usr/bin/env python
#AUTHUR: ZHIQIANG TANG
#DATE: 2019/04/20
import minimalmodbus
import binascii
import time
import sys

class Robotiq_py2:
	def __init__(self):
		### command definition
		self.initGripper_str = '000000000000'
		#                 aabbcc. aa:position, bb:speed, cc:torque
		self.close_str = '090000ffffff'
		self.open_str = '09000000ffff'

	def init_gripper(self):
		### open serial port and setup baudrate
		instrument = minimalmodbus.Instrument('/dev/ttyS1', 9) # port name, slave address (in decimal)
		instrument.serial.baudrate = 115200

		### init robotiq
		print("init...")
		time.sleep(0.5)
		return_str = instrument.write_string(1000, binascii.unhexlify(self.initGripper_str), numberOfRegisters=3)
		print(return_str)
		time.sleep(0.5)
		print("init done!")

	def close_gripper(self):

		# open serial port and setup baudrate
		instrument = minimalmodbus.Instrument('/dev/ttyS1', 9)  # port name, slave address (in decimal)
		instrument.serial.baudrate = 115200

		# read robotiq
		# register address 0x07d0==2000     numberOfRegisters    functioncode
		return_str = instrument.read_string(2000, numberOfRegisters=3, functioncode=3)
		print("robotiq status:"+" ".join(hex(ord(n)) for n in return_str))

		# close robotiq
		# address of 1st register:0x03e8 = 1000
		instrument.write_string(1000, binascii.unhexlify(self.close_str), numberOfRegisters=3)

	def open_gripper(self):
		# open serial port and setup baudrate
		instrument = minimalmodbus.Instrument('/dev/ttyS1', 9)  # port name, slave address (in decimal)
		instrument.serial.baudrate = 115200

		# read robotiq
		# register address 0x07d0==2000     numberOfRegisters    function code
		return_str = instrument.read_string(2000, numberOfRegisters=3, functioncode=3)
		print("robotiq status:"+" ".join(hex(ord(n)) for n in return_str))

		# open:
		print("open")
		instrument.write_string(1000, binascii.unhexlify(self.open_str), numberOfRegisters=3)

	def gripper_test(self):
		# open serial port and setup baudrate
		instrument = minimalmodbus.Instrument('/dev/ttyS1', 9)  # port name, slave address (in decimal)
		instrument.serial.baudrate = 115200

		# read robotiq
		#         registeraddress 0x07d0==2000     numberOfRegisters    functioncode
		return_str = instrument.read_string(2000, numberOfRegisters=3, functioncode=3)
		# print it in help
		print("robotiq status:"+" ".join(hex(ord(n)) for n in return_str))

		# wirte robotiq
		for i in range(3):
			#close:
			print("clse:")
								#address of 1st register:0x03e8 = 1000
			return_str = instrument.write_string(1000, binascii.unhexlify(self.close_str), numberOfRegisters=3)
			time.sleep(3)
			#open:
			print("open")
			instrument.write_string(1000, binascii.unhexlify(self.open_str), numberOfRegisters=3)
			time.sleep(3)
			### read robotiq 
			#         registeraddress 0x07d0==2000     numberOfRegisters    functioncode
			return_str = instrument.read_string(2000, numberOfRegisters=3, functioncode=3)
			# print it in hex
			print ("robotiq status:"+" ".join(hex(ord(n)) for n in return_str))

def testpy():
	print ("test start py3")
	r = Robotiq_py2()
	r.gripperTest()

	
if __name__ == '__main__':
	r = Robotiq_py2()

	# cmd for init gripper
	if sys.argv[1] is 'i':
		print("initiating gripper")
		r.init_gripper()

	# cmd for close gripper
	if sys.argv[1] is 'c':
		print("closing gripper")
		r.close_gripper()

	# cmd for open gripper
	if sys.argv[1] is 'o':
		print("opening gripper")
		r.open_gripper()







