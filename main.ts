function runRedBrickMotor(motor: number, isLeft: boolean, clicks: number) {
    
    lspeed = 60
    if (!isLeft) {
        lspeed = 0 - lspeed
    }
    
    for (let index = 0; index < clicks; index++) {
        wuKong.setMotorSpeed(motor, lspeed)
        basic.pause(200)
        wuKong.stopMotor(motor)
    }
}

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    runRedBrickMotor(wuKong.MotorList.M1, false, 3)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    runRedBrickMotor(wuKong.MotorList.M2, true, 2)
})
let lspeed = 0
let INIT = 0
let M1_POS = 0
let M2_POS = 0
let LEFT = 0
wuKong.mecanumWheel(wuKong.ServoList.S1, wuKong.ServoList.S2, wuKong.ServoList.S3, wuKong.ServoList.S4)
wuKong.stopMotor(wuKong.MotorList.M1)
wuKong.stopMotor(wuKong.MotorList.M2)
servos.P2.setRange(0, 60)
servos.P2.setAngle(45)
wuKong.stopAllMotor()
radio.setGroup(3)
radio.setFrequencyBand(33)
basic.showIcon(IconNames.Yes)
radio.sendString("CLAW")
let MAX_CLICKS = 5
let MIN_CLICKS = -5
let motor_states = [-3, -2, -1, 0, 1, 2, 3]
let curMS = motor_states[INIT]
