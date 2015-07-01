__author__ = 'mustafa'
from motor import Motor
from maestro_connection import MaestroConnection
import os

class Robot(object):
    """
    Robot object contains all things for the robot like motors, sound files, sequences
    """
    def __init__(self, name):
        self.maestro = MaestroConnection()
        self.maestro.connect()
        self.motor_list = {}
        self.project_directory = '/home/mustafa/PycharmProjects/robot_face_v2/'
        self.config_directory =name + '_config/'
        os.chdir(self.project_directory)

    def setup_robot(self):
        """
        load config files: motor
        :return:
        """
        f = open(self.config_directory + 'motor.txt', 'r')

        for line in f:
            self.add_motor(line)

        self.update_motors()

    def add_motor(self, line):
        """
        Add a new motor to the motor list
        :param line: motor parameters line as string from config file
        motor_number, motor_name, start_position, min_limit, max_limit
        :return:
        """
        line_list = line.split()
        new_motor = Motor(line_list[1])
        new_motor.motor_number = int(line_list[0])
        new_motor.goal_position = int(line_list[2])
        new_motor.min_limit = int(line_list[3])
        new_motor.max_limit = int(line_list[4])
        self.motor_list[line_list[1]] = new_motor



    def setup_connections(self):
        self.maestro.connect()

    def update_motors(self):
        for motor in self.motor_list:
            self.maestro.update_positions(self.motor_list.values())
