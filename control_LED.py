#!/usr/bin/env python3
from gpiozero import RGBLED

WHITE  = (1,1,1)
RED    = (1,0,0)
GREEN  = (0,1,0)
BLUE   = (0,0,1)
YELLOW = (1,1,0)
PURPLE = (1,0,1)
CYAN   = (0,1,1)
BLACK  = (0,0,0)
# GPIO Zeroライブラリを使用して、GPIOピンに接続されたLEDを初期化
led = RGBLED(red=17, green=18, blue=27)

def change_color(state):
    """
    LEDの状態を制御する関数
    :param state: 'on' または 'off'
    """
    if state == "white":
        led.color = WHITE
    elif state == "red":
        led.color = RED
    elif state == "green":
        led.color = GREEN
    elif state == "blue":
        led.color = BLUE
    elif state == "yellow":
        led.color = YELLOW
    elif state == "purple":
        led.color = PURPLE
    elif state == "cyan":
        led.color = CYAN
    elif state == "black":
        led.color = BLACK
