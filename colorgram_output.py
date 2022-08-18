import os
import csv
import cv2
import colorgram
import numpy as np

yourpath = "D:\\專題test" #enter file path
allFileList = os.listdir(yourpath)
number = 0 # set photo num

for file in allFileList:
    print(file)
    number += 1
    colors = colorgram.extract(os.path.join(yourpath, file), 10) # extract 5 colors
    save = [0]*15 # colors' mark (1-45)
    color_histogram = [0]*45 # color_histogram[1] to color_histogram[45]

    for i in range(len(colors)):
        print(i+1, ' color:')
        col = np.uint8([[colors[i].rgb]]) # rgb of colors
        hsv_col = cv2.cvtColor(col, cv2.COLOR_BGR2HSV) # hsv of colors
        # note: hsv_col[0][0][0] == h , hsv_col[0][0][1] == s , hsv_col[0][0][2] == v

        # first step: use h to classify
        save[i] = ((hsv_col[0][0][0] / 20) * 4) - (((hsv_col[0][0][0] / 20) * 4) % 4)
        if hsv_col[0][0][1] >= 128:
            save[i] += 2
            if (hsv_col[0][0][2] >= 128): save[i] += 1
        if (hsv_col[0][0][1] < 128 and hsv_col[0][0][2] >= 128) : save[i] += 1

        # for black, white, gray
        if hsv_col[0][0][0] == 0 and hsv_col[0][0][1] == 0:
            save[i] = 35 + round(hsv_col[0][0][2]/28)

        color_histogram[np.uint8(save[i])] += round(colors[i].proportion, 4)
        print('color number: ', save[i])
        print('proportion: ', round(colors[i].proportion, 4))

    print(color_histogram)
    with open('test.csv', 'a+', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([file, color_histogram[0], color_histogram[1], color_histogram[2], color_histogram[3], color_histogram[4], color_histogram[5],
                         color_histogram[6], color_histogram[7], color_histogram[8], color_histogram[9], color_histogram[10], color_histogram[11],
                         color_histogram[12], color_histogram[13], color_histogram[14], color_histogram[15], color_histogram[16], color_histogram[17],
                         color_histogram[18], color_histogram[19], color_histogram[20], color_histogram[21], color_histogram[22], color_histogram[23],
                         color_histogram[24], color_histogram[25], color_histogram[26], color_histogram[27], color_histogram[28], color_histogram[29],
                         color_histogram[30], color_histogram[31], color_histogram[32], color_histogram[33], color_histogram[34], color_histogram[35],
                         color_histogram[36], color_histogram[37], color_histogram[38], color_histogram[39], color_histogram[40], color_histogram[41],
                         color_histogram[42], color_histogram[43], color_histogram[44]])