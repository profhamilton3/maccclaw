radio.onReceivedNumber(function (receivedNumber) {
    basic.showIcon(IconNames.Snake)
    if (1 == receivedNumber) {
        music.playSoundEffect(music.createSoundEffect(WaveShape.Sine, 5000, 0, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), SoundExpressionPlayMode.InBackground)
        runRedBrickMotor(wuKong.MotorList.M2, true, 1)
    } else if (2 == receivedNumber) {
        music.playSoundEffect(music.createSoundEffect(WaveShape.Square, 5000, 0, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), SoundExpressionPlayMode.InBackground)
        runRedBrickMotor(wuKong.MotorList.M2, false, 1)
    } else if (3 == receivedNumber) {
        music.playSoundEffect(music.createSoundEffect(WaveShape.Sawtooth, 5000, 0, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), SoundExpressionPlayMode.InBackground)
        runRedBrickMotor(wuKong.MotorList.M1, true, 1)
    } else if (4 == receivedNumber) {
        music.playSoundEffect(music.createSoundEffect(WaveShape.Triangle, 5000, 0, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), SoundExpressionPlayMode.InBackground)
        runRedBrickMotor(wuKong.MotorList.M1, false, 1)
    } else if (5 == receivedNumber) {
        music.playSoundEffect(music.createSoundEffect(WaveShape.Noise, 5000, 0, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), SoundExpressionPlayMode.InBackground)
        servos.P2.setAngle(15)
    } else if (6 == receivedNumber) {
        music.playSoundEffect(music.createSoundEffect(WaveShape.Square, 5000, 0, 255, 0, 500, SoundExpressionEffect.Vibrato, InterpolationCurve.Curve), SoundExpressionPlayMode.InBackground)
        servos.P2.setAngle(75)
    } else if (7 == receivedNumber) {
        music.playSoundEffect(music.createSoundEffect(WaveShape.Sine, 5000, 0, 255, 0, 500, SoundExpressionEffect.Tremolo, InterpolationCurve.Linear), SoundExpressionPlayMode.InBackground)
        wuKong.setLightMode(wuKong.LightMode.BREATH)
        wuKong.mecanumRun(wuKong.RunList.Front, 60)
        wuKong.setLightMode(wuKong.LightMode.OFF)
    } else if (8 == receivedNumber) {
        music.playSoundEffect(music.createSoundEffect(WaveShape.Triangle, 5000, 0, 255, 0, 500, SoundExpressionEffect.Tremolo, InterpolationCurve.Logarithmic), SoundExpressionPlayMode.InBackground)
        wuKong.setLightMode(wuKong.LightMode.BREATH)
        wuKong.mecanumRun(wuKong.RunList.rear, 60)
        wuKong.setLightMode(wuKong.LightMode.OFF)
    } else if (9 == receivedNumber) {
        music.playSoundEffect(music.createSoundEffect(WaveShape.Sawtooth, 5000, 0, 255, 0, 500, SoundExpressionEffect.Warble, InterpolationCurve.Logarithmic), SoundExpressionPlayMode.InBackground)
        wuKong.setLightMode(wuKong.LightMode.BREATH)
        wuKong.mecanumSpin(wuKong.TurnList.Left, 35)
        wuKong.setLightMode(wuKong.LightMode.OFF)
    } else if (10 == receivedNumber) {
        music.playSoundEffect(music.createSoundEffect(WaveShape.Sine, 5000, 0, 255, 0, 500, SoundExpressionEffect.Warble, InterpolationCurve.Logarithmic), SoundExpressionPlayMode.InBackground)
        wuKong.setLightMode(wuKong.LightMode.BREATH)
        wuKong.mecanumSpin(wuKong.TurnList.Right, 35)
        wuKong.setLightMode(wuKong.LightMode.OFF)
    } else if (11 == receivedNumber) {
        music.startMelody(music.builtInMelody(Melodies.PowerDown), MelodyOptions.Once)
        wuKong.setLightMode(wuKong.LightMode.OFF)
        wuKong.mecanumRun(wuKong.RunList.stop, 0)
    }
})
function runRedBrickMotor (motor: number, isLeft: boolean, clicks: number) {
    lspeed = 50
    if (!(isLeft)) {
        lspeed = 0 - lspeed
    }
    for (let index = 0; index < clicks; index++) {
        wuKong.setMotorSpeed(motor, lspeed)
basic.pause(100)
    }
    wuKong.stopMotor(motor)
}
input.onButtonPressed(Button.A, function () {
    servos.P2.setAngle(15)
})
input.onButtonPressed(Button.B, function () {
    servos.P2.setAngle(75)
})
let lspeed = 0
wuKong.mecanumWheel(
wuKong.ServoList.S1,
wuKong.ServoList.S2,
wuKong.ServoList.S3,
wuKong.ServoList.S4
)
wuKong.stopMotor(wuKong.MotorList.M1)
wuKong.stopMotor(wuKong.MotorList.M2)
servos.P2.setRange(15, 80)
servos.P2.setAngle(15)
wuKong.stopAllMotor()
wuKong.setLightMode(wuKong.LightMode.BREATH)
radio.setGroup(3)
radio.setFrequencyBand(33)
basic.showIcon(IconNames.Heart)
radio.sendString("CLAW")
