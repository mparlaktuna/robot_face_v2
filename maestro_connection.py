__author__ = 'Mustafa Parlaktuna'
__company__ = 'Robotes'
__email__ = 'mparlaktuna@gmail.com'

import serial

class MaestroConnection(object):
    """
    creates and checkes maestro connection
    """
    def __init__(self, port_name='/dev/ttyACM0'):
        self.serial_port_name = port_name

    def connect(self):
        """
        connects to a defined port for maestro, default port is /dev/ttyACM0
        :return:
        """
        self.serial_port = serial.Serial(self.serial_port_name)
        print("Port opened")

    def disconnect(self):
        """
        closes the connection to maestro
        :return:
        """
        self.serial_port.close()
        del self.serial_port

    def write(self,*data):
        """
        writes the data to the port
        :param data:
        :return:
        """
        for d in data:
            self.serial_port.write(chr(d))
        self.serial_port.flush()

    def update_positions(self, motor_list):
        for motor_number, motor in enumerate(motor_list):
            highbits,lowbits = divmod(motor.goal_position,32)
            self.write(0x84,int(motor.motor_number),lowbits << 2,highbits)

    def update_speeds(self, motor_list):
        for motor_number, motor in enumerate(motor_list):
            highbits,lowbits = divmod(motor.speed,32)
            self.write(0x87,int(motor.motor_number),lowbits << 2,highbits)



