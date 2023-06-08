def on_received_number(receivedNumber):
    basic.show_icon(IconNames.SNAKE)
    if 1 == receivedNumber:
        music.play_sound_effect(music.create_sound_effect(WaveShape.SINE,
                5000,
                0,
                255,
                0,
                500,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LINEAR),
            SoundExpressionPlayMode.IN_BACKGROUND)
        runRedBrickMotor(wuKong.MotorList.M2, True, 1)
    elif 2 == receivedNumber:
        music.play_sound_effect(music.create_sound_effect(WaveShape.SQUARE,
                5000,
                0,
                255,
                0,
                500,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LINEAR),
            SoundExpressionPlayMode.IN_BACKGROUND)
        runRedBrickMotor(wuKong.MotorList.M2, False, 1)
    elif 3 == receivedNumber:
        music.play_sound_effect(music.create_sound_effect(WaveShape.SAWTOOTH,
                5000,
                0,
                255,
                0,
                500,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LINEAR),
            SoundExpressionPlayMode.IN_BACKGROUND)
        runRedBrickMotor(wuKong.MotorList.M1, True, 1)
    elif 4 == receivedNumber:
        music.play_sound_effect(music.create_sound_effect(WaveShape.TRIANGLE,
                5000,
                0,
                255,
                0,
                500,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LINEAR),
            SoundExpressionPlayMode.IN_BACKGROUND)
        runRedBrickMotor(wuKong.MotorList.M1, False, 1)
    elif 5 == receivedNumber:
        music.play_sound_effect(music.create_sound_effect(WaveShape.NOISE,
                5000,
                0,
                255,
                0,
                500,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LINEAR),
            SoundExpressionPlayMode.IN_BACKGROUND)
        servos.P2.set_angle(15)
    elif 6 == receivedNumber:
        music.play_sound_effect(music.create_sound_effect(WaveShape.SQUARE,
                5000,
                0,
                255,
                0,
                500,
                SoundExpressionEffect.VIBRATO,
                InterpolationCurve.CURVE),
            SoundExpressionPlayMode.IN_BACKGROUND)
        servos.P2.set_angle(75)
    elif 7 == receivedNumber:
        music.play_sound_effect(music.create_sound_effect(WaveShape.SINE,
                5000,
                0,
                255,
                0,
                500,
                SoundExpressionEffect.TREMOLO,
                InterpolationCurve.LINEAR),
            SoundExpressionPlayMode.IN_BACKGROUND)
        wuKong.set_light_mode(wuKong.LightMode.BREATH)
        wuKong.mecanum_run(wuKong.RunList.FRONT, 60)
        wuKong.set_light_mode(wuKong.LightMode.OFF)
    elif 8 == receivedNumber:
        music.play_sound_effect(music.create_sound_effect(WaveShape.TRIANGLE,
                5000,
                0,
                255,
                0,
                500,
                SoundExpressionEffect.TREMOLO,
                InterpolationCurve.LOGARITHMIC),
            SoundExpressionPlayMode.IN_BACKGROUND)
        wuKong.set_light_mode(wuKong.LightMode.BREATH)
        wuKong.mecanum_run(wuKong.RunList.REAR, 60)
        wuKong.set_light_mode(wuKong.LightMode.OFF)
    elif 9 == receivedNumber:
        music.play_sound_effect(music.create_sound_effect(WaveShape.SAWTOOTH,
                5000,
                0,
                255,
                0,
                500,
                SoundExpressionEffect.WARBLE,
                InterpolationCurve.LOGARITHMIC),
            SoundExpressionPlayMode.IN_BACKGROUND)
        wuKong.set_light_mode(wuKong.LightMode.BREATH)
        wuKong.mecanum_spin(wuKong.TurnList.LEFT, 35)
        wuKong.set_light_mode(wuKong.LightMode.OFF)
    elif 10 == receivedNumber:
        music.play_sound_effect(music.create_sound_effect(WaveShape.SINE,
                5000,
                0,
                255,
                0,
                500,
                SoundExpressionEffect.WARBLE,
                InterpolationCurve.LOGARITHMIC),
            SoundExpressionPlayMode.IN_BACKGROUND)
        wuKong.set_light_mode(wuKong.LightMode.BREATH)
        wuKong.mecanum_spin(wuKong.TurnList.RIGHT, 35)
        wuKong.set_light_mode(wuKong.LightMode.OFF)
    elif 11 == receivedNumber:
        music.start_melody(music.built_in_melody(Melodies.POWER_DOWN),
            MelodyOptions.ONCE)
        wuKong.set_light_mode(wuKong.LightMode.OFF)
        wuKong.mecanum_run(wuKong.RunList.STOP, 0)
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
    servos.P2.set_angle(15)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    servos.P2.set_angle(75)
input.on_button_pressed(Button.B, on_button_pressed_b)

lspeed = 0
wuKong.mecanum_wheel(wuKong.ServoList.S1,
    wuKong.ServoList.S2,
    wuKong.ServoList.S3,
    wuKong.ServoList.S4)
wuKong.stop_motor(wuKong.MotorList.M1)
wuKong.stop_motor(wuKong.MotorList.M2)
servos.P2.set_range(15, 80)
servos.P2.set_angle(15)
wuKong.stop_all_motor()
wuKong.set_light_mode(wuKong.LightMode.BREATH)
radio.set_group(3)
radio.set_frequency_band(33)
basic.show_icon(IconNames.HEART)
radio.send_string("CLAW")