def runRedBrickMotor(motor: number, isLeft: bool, clicks: number):
    global lspeed
    lspeed = 60
    if not (isLeft):
        lspeed = 0 - lspeed
    for index in range(clicks):
        wuKong.set_motor_speed(motor, lspeed)
        basic.pause(200)
        wuKong.stop_motor(motor)

def on_button_pressed_a():
    runRedBrickMotor(wuKong.MotorList.M1, False, 3)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    runRedBrickMotor(wuKong.MotorList.M2, True, 2)
input.on_button_pressed(Button.B, on_button_pressed_b)

lspeed = 0
INIT = 0
M1_POS = 0
M2_POS = 0
LEFT = 0
wuKong.mecanum_wheel(wuKong.ServoList.S1,
    wuKong.ServoList.S2,
    wuKong.ServoList.S3,
    wuKong.ServoList.S4)
wuKong.stop_motor(wuKong.MotorList.M1)
wuKong.stop_motor(wuKong.MotorList.M2)
servos.P2.set_range(0, 60)
servos.P2.set_angle(45)
wuKong.stop_all_motor()
radio.set_group(3)
radio.set_frequency_band(33)
basic.show_icon(IconNames.YES)
radio.send_string("CLAW")
MAX_CLICKS = 5
MIN_CLICKS = -5
motor_states = [-3, -2, -1, 0, 1, 2, 3]
curMS = motor_states[INIT]