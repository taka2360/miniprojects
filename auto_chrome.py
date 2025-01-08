from selenium import webdriver
from selenium.webdriver.common.by import By
import numpy as np
import cv2

import time

driver = webdriver.Chrome()

driver.get('https://google.com')

driver.save_screenshot(r"./screenshots/test.png")
binaryimg = driver.get_screenshot_as_png()

arr = np.frombuffer(binaryimg, dtype=np.uint8)
img = cv2.imdecode(arr, flags=cv2.IMREAD_COLOR)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
time.sleep(10000)