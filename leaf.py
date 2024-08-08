import pydirectinput
from pathlib import Path
import tomllib
import dataclasses
from pydirectinput import (
    keyDown,
    keyUp,
    move,
    moveRel,
    moveTo,
    mouseDown,
    mouseUp,
    press,
    leftClick,
    rightClick,
)
import time

pydirectinput.FAILSAFE = False

round = 0

def run(t: int):
    keyDown("w")
    time.sleep(0.01)
    keyDown("shiftleft")
    time.sleep(t / 1000)
    keyUp("w")
    keyUp("shiftleft")


def enter():
    keyDown("o")
    time.sleep(4)
    keyUp("o")
    time.sleep(10)
    moveTo(1500, 940)
    leftClick()

def start():
    global round

    moveTo(1500, 940)
    time.sleep(0.2)
    leftClick()
    print("进图")
    time.sleep(10)
    print("wait")
    time.sleep(10)
    print("wait")
    time.sleep(10)
    print("wait")
    time.sleep(10)
    print("wait")
    time.sleep(10)
    print("wait")
    time.sleep(10)
    print("go")


    run(10000)
    time.sleep(0.5)
    keyDown('w')
    keyDown('d')
    time.sleep(2)
    keyUp('w')
    time.sleep(1)
    keyUp('d')


    time.sleep(10)
    print("wait")
    time.sleep(10)
    print("wait")
    time.sleep(10)
    print("wait")
    time.sleep(10)
    print("wait")
    time.sleep(10)
    print("wait")
    time.sleep(10)
    print("wait")
    round = round + 1    
    print("已执行", round, "轮")
    time.sleep(0.5)
    enter()
    time.sleep(0.1)
   

time.sleep(0.5)
time.sleep(0.5)
print("5秒后开启程序,请手动切到游戏窗口")
time.sleep(1)
print("4秒后开启程序,请手动切到游戏窗口")
time.sleep(1)
print("3秒后开启程序,请手动切到游戏窗口")
time.sleep(1)
print("2秒后开启程序,请手动切到游戏窗口")
time.sleep(1)
print("1秒后开启程序,请手动切到游戏窗口")

if __name__ == "__main__":
    try:
        while True:
            start()
    except KeyboardInterrupt:
        ...
