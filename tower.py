#!/usr/bin/env python3

from RPi import GPIO
from mcpi.minecraft import Minecraft
import time

PinNum = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(PinNum,GPIO.IN)

mc = Minecraft.create()
pos = mc.player.getTilePos()
x = pos.x + 1
y = pos.y
z = pos.z

# Add 10 glass blocks (block id 20) to this list
blocks = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
barBlock = 22  # Lapis lazuli
glassBlock = 20

count = 0
back = 0
size = len(blocks)

while True:
    if GPIO.input(PinNum) == True:
        continue

    i = 0
    while i < len(blocks):
        mc.setBlock(x, y + i, z, blocks[i])
        i += 1
    
    if count >= len(blocks):
        count = 0
        if back == 0:
            back = 1
        else:
            back = 0
            
    # print("count" + str(count))
    # print("back" + str(back))
    
    if back == 0:
        del blocks[size - 1]
        blocks.insert(0, barBlock)
    else:
        del blocks[0]
        blocks.insert(size - 1 , glassBlock)

    count += 1
    time.sleep(.5)


