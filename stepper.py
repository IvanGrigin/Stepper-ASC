from pymata4 import pymata4


class Step_Motor:
    def __init__(self):
        self.num_steps = 800  # 800 - 800 steps in 360 degrees
        self.pins = [4, 5]
        self.board = pymata4.Pymata4()
        self.board.set_pin_mode_stepper(self.num_steps, self.pins)


    def rotate_on_degrees(self, angle_in_degrees, rate_of_turnover):

        speed = rate_of_turnover # 400 - max speed


        rotate = int(angle_in_degrees * self.num_steps / 360)
        self.board.stepper_write(speed, rotate)
        print('Success')


stepper = Step_Motor()
print('Write num of degrees\n')
stepper.rotate_on_degrees(int(input()), 40)