__author__ = 'mustafa'

class Motor(object):
    """
    Motor object for the robot. Contains the position and characteristics of a motor
    """
    def __init__(self, name):
        self.motor_name = name
        self.motor_number = 0
        self.max_limit = 2000
        self.min_limit = 1000
        self.current_position = 0
        self.goal_position = 0
        self.speed = 50
        self.position_dictionary = {}

    def set_limits(self, max_limit, min_limit):
        """
        Sets the maximum and minimum limits of the motor
        :param max_limit:
        :param min_limit:
        :return:
        """
        self.max_limit = max_limit
        self.min_limit = min_limit

    def check_limits(self, value):
        """
        Checks the goal position if it is between the limits
        :param value:
        :return:
        """
        if value> self.max_limit or value < self.min_limit:
            return False
        else:
            return True

    def set_goal_position(self, value):
        """
        sets goal position for the motor
        :param value:
        :return:
        """
        if self.check_limits(value):
            self.goal_position = value
        else:
            print('''
            Given Position does not satisfy limits:
            Motor Number: {0}
            Motor Name: {1}
            Given Position: {2}
            Maximum Limit: {3}
            Minimum Limit: {4}
            '''.format(self.motor_number, self.motor_name, value, self.max_limit, self.min_limit))

    def set_speed(self, value):
        """
        sets the speed value of the motor
        :param value:
        :return:
        """
        if 0 < value < 100 :
            self.speed = value
        else:
            print('''
            Speed value does not satisfy limits:
            Motor Number: {0}
            Motor Name: {1}
            Given Position: {2}
            Maximum Limit: 100
            Minimum Limit: 0
            '''.format(self.motor_number, self.motor_name, value)
            )