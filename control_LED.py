#!/usr/bin/env python3
from gpiozero import LED

# GPIO Zeroライブラリを使用して、GPIOピン17に接続されたLEDを初期化
led = LED(17)

def change_color(state):
    """
    LEDの状態を制御する関数
    :param state: 'on' または 'off'
    """
    if state == "on":
        led.on()
    elif state == "off":
        led.off()
