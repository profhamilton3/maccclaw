def on_received_number(receivedNumber):
    if 1 == receivedNumber:
        runRedBrickMotor(wuKong.MotorList.M2, True, 1)
    elif 2 == receivedNumber:
        runRedBrickMotor(wuKong.MotorList.M2, False, 1)
    elif 3 == receivedNumber:
        runRedBrickMotor(wuKong.MotorList.M1, True, 1)
    elif 4 == receivedNumber:
        runRedBrickMotor(wuKong.MotorList.M1, False, 1)
    elif 5 == receivedNumber:
        servos.P2.set_angle(0)
    elif 6 == receivedNumber:
        servos.P2.set_angle(60)
    else:
        pass
radio.on_received_number(on_received_number)

def runRedBrickMotor(motor: number, isLeft: bool, clicks: number):
    global lspeed
    lspeed = 50
    if not (isLeft):
        lspeed = 0 - lspeed
    for index in range(clicks):
        wuKong.set_motor_speed(motor, lspeed)
        basic.pause(100)
    wuKong.stop_motor(motor)

def on_button_pressed_a():
    servos.P2.set_angle(0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    servos.P2.set_angle(60)
input.on_button_pressed(Button.B, on_button_pressed_b)

lspeed = 0

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
basic.show_icon(IconNames.CONFUSED)
radio.send_string("CLAW")
MAX_CLICKS = 5
MIN_CLICKS = -5