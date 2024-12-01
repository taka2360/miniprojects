import time
import math
import os
import numpy as np

A = -10
B = 0
C = 0

cubeWidth = 3
width = 160
height = 44
backgroundASCIICode = ' '
zBuffer = [0 for _ in range(width * height * 4)]
buffer = [backgroundASCIICode for _ in range(width * height)]
distanceFromCam = 60
horizontalOffset = 0
K1 = 40
incrementSpeed = 0.6


def calculateX(i:int, j:int, k:int):
  return j * math.sin(A) * math.sin(B) * math.cos(C) - k * math.cos(A) * math.sin(B) * math.cos(C) + j * math.cos(A) * math.sin(C) + k * math.sin(A) * math.sin(C) + i * math.cos(B) * math.cos(C)


def calculateY(i:int, j:int, k:int) :
  return j * math.cos(A) * math.cos(C) + k * math.sin(A) * math.cos(C) - j * math.sin(A) * math.sin(B) * math.sin(C) + k * math.cos(A) * math.sin(B) * math.sin(C) - i * math.cos(B) * math.sin(C)


def calculateZ(i:int, j:int, k:int):
  return k * math.cos(A) * math.cos(B) - j * math.sin(A) * math.cos(B) + i * math.sin(B)


def calculateForSurface(cubeX:float, cubeY:float, cubeZ:float, ch:int):
  x = calculateX(cubeX, cubeY, cubeZ)
  y = calculateY(cubeX, cubeY, cubeZ)
  z = calculateZ(cubeX, cubeY, cubeZ) + distanceFromCam

  ooz = 1 / z

  xp = int(width / 2 + horizontalOffset + K1 * ooz * x * 2)
  yp = int(height / 2 + K1 * ooz * y)

  idx = xp + yp * width
  if (idx >= 0 and idx < width * height):
    if (ooz > zBuffer[idx]) :
      zBuffer[idx] = ooz
      buffer[idx] = ch

def main() :
  global horizontalOffset, A, B, C, buffer, zBuffer
  

  os.system("cls")
  
  while (1) :
    cubeWidth = 10
    #horizontalOffset = -2 * cubeWidth
    buffer = [backgroundASCIICode for _ in range(width * height)]
    zBuffer = [0 for _ in range(width * height * 4)]
    # first cube
    for cubeX in np.arange(-cubeWidth, cubeWidth, incrementSpeed):
      for cubeY in np.arange(-cubeWidth, cubeWidth, incrementSpeed):
        calculateForSurface(cubeX, cubeY, -cubeWidth, '.')
        calculateForSurface(cubeWidth, cubeY, cubeX, '$')
        calculateForSurface(-cubeWidth, cubeY, -cubeX, '~')
        calculateForSurface(-cubeX, cubeY, cubeWidth, '#')
        calculateForSurface(cubeX, -cubeWidth, -cubeY, ';')
        calculateForSurface(cubeX, cubeWidth, cubeY, '+')
    """
      
    
    cubeWidth = 10
    horizontalOffset = 1 * cubeWidth
    # second cube
    for cubeX in np.arange(-cubeWidth, cubeWidth, incrementSpeed):
      for cubeY in np.arange(-cubeWidth, cubeWidth, incrementSpeed):
        calculateForSurface(cubeX, cubeY, -cubeWidth, '@')
        calculateForSurface(cubeWidth, cubeY, cubeX, '$')
        calculateForSurface(-cubeWidth, cubeY, -cubeX, '~')
        calculateForSurface(-cubeX, cubeY, cubeWidth, '#')
        calculateForSurface(cubeX, -cubeWidth, -cubeY, ';')
        calculateForSurface(cubeX, cubeWidth, cubeY, '+')
      
    
    cubeWidth = 5
    horizontalOffset = 8 * cubeWidth
    # third cube
    for cubeX in np.arange(-cubeWidth, cubeWidth, incrementSpeed):
      for cubeY in np.arange(-cubeWidth, cubeWidth, incrementSpeed):
        calculateForSurface(cubeX, cubeY, -cubeWidth, '@')
        calculateForSurface(cubeWidth, cubeY, cubeX, '$')
        calculateForSurface(-cubeWidth, cubeY, -cubeX, '~')
        calculateForSurface(-cubeX, cubeY, cubeWidth, '#')
        calculateForSurface(cubeX, -cubeWidth, -cubeY, ';')
        calculateForSurface(cubeX, cubeWidth, cubeY, '+')
    """
    
    
    os.system("cls")
    display_text = ""
    for i in range(height):
      display_text += "".join(buffer[i*width:(i+1)*width]) + "\n"
    print(display_text)
  
    
    """
    A += 0.05
    B += 0.05
    C += 0.01"""
    time.sleep(1/60)
  
if __name__ == "__main__":
  main()
