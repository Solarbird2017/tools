import cv2
import numpy as np
import glob

names = []
for i in range(1,403):
    text = "%08d" % i
    text = './code/kcf-tracker_opencv/img/' + text+'.jpg'
    names.append(text)
    # print(text)

size = (0,0)
img_array = []
for filename in names:
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)

out = cv2.VideoWriter('project.mov', cv2.VideoWriter_fourcc(*'DIVX'), 30, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()

