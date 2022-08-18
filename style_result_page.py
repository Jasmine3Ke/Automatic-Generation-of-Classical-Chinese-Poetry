import os
import sys
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

import cv2
import colorgram
import numpy as np

import pandas as pd
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from numpy import random

# 1. 規劃整體視窗
window = tk.Tk()
window.title('Voting page')
window.geometry('900x700')
window.configure(background='white')

canvas = tk.Canvas(window, height=400, width=400)
canvas.place(relx=0.3, rely=0.5, anchor='center')

path = tk.StringVar() # 存路徑

def resize(image):
    w, h = image.size
    mlength = max(w, h)  # 找出最大的邊
    mul = 400 / mlength  # 縮放倍數
    w1 = int(w * mul)  # 重新獲得長寬
    h1 = int(h * mul)
    return image.resize((w1, h1))

def show_image(path, name):
    global img, score
    image = Image.open(path)  # 開圖
    re_image = resize(image)  # 重新定義圖片尺寸 (使用resize function)
    img = ImageTk.PhotoImage(re_image)
    canvas.create_image(200, 200, anchor='center', image=img) # 在畫布上展示圖片，參數: 長, 寬, 位置, 引入圖片

def openpicture(): # open and show image
    global fileindex, fatherpath, files, file_num, filename, filepath

    filepath = filedialog.askopenfilename()
    fatherpath = os.path.dirname(filepath)      # 獲取該路徑的上一級路徑
    filename = os.path.basename(filepath)   # 獲取該路徑下的文件名
    files = os.listdir(fatherpath)     # 該路徑下的所有文件並生成列表
    file_num = len(files)
    fileindex = files.index(filename)    # 獲取當前文件的索引值
    show_image(filepath, filename)

    # 關鍵詞：page上面顯示繁體，但輸入到WMPoetry的需要簡體輸入
    country_key = ['樹', '山', '雲', '月', '鳥', '落日', '孤煙', '墟里', '東籬', '南山',
                   '竹林', '幽篁', '柴門', '荆扉', '林叟', '桑麻', '桑榆', '雞豚', '幾聲', '蘆花',
                   '溪岸', '白鷺', '沙鷗', '青草', '綠樹', '青山']

    romantic_key = ['愛', '自由', '美', '青春', '真', '溫柔', '天梯', '青冥', '雲霓', '歌吟',
                    '相思', '堅貞', '眷戀', '月光', '雙飛', '花', '堅定', '華美', '理想', '黎明',
                    '拂曉', '玫瑰']

    dark_key = ['傷心', '獨', '孤', '愁', '漁火', '瘦馬', '鐘聲', '鄉', '客', '歸',
                '杜鵑', '天涯', '空寂', '凄寒', '霧', '憤', '憶', '寄', '離別', '沾巾',
                '浮雲', '孤蓬', '水', '泣涕', '傷', '焚', '落絮', '柳絲', '流浪', '憾恨']

    colorful_key = ['太陽', '青春', '翠', '繽紛', '閒逸', '清新', '深秀', '日出', '朝氣', '晨光',
                    '晨曦', '笑語', '盛夏', '嬉戲', '朝陽']

    old_key = ['少壮', '年少', '青絲', '朱顏', '白髮', '華鬢', '壽考', '流水', '逝川', '燕子',
               '朝露', '盛壯', '夕陽', '長亭', '落花', '懷古', '昔時', '今昔', '歲月']

    if svm(filepath) == 'romantic':
        x = random.choice(romantic_key, size=(2))
        style_kw_result.set(x)
        print(svm(filepath), x)
    elif svm(filepath) == 'country':
        x = random.choice(country_key, size=(2))
        style_kw_result.set(x)
        print(svm(filepath), x)
    elif svm(filepath) == 'dark':
        x = random.choice(dark_key, size=(2))
        style_kw_result.set(x)
        print(svm(filepath), x)
    elif svm(filepath) == 'old':
        x = random.choice(old_key, size=(2))
        style_kw_result.set(x)
        print(svm(filepath), x)
    elif svm(filepath) == 'colorful':
        x = random.choice(colorful_key, size=(2))
        style_kw_result.set(x)
        print(svm(filepath), x)
    else:
        print('error')

def genColorgram(path):
    colors = colorgram.extract(path, 10)  # extract 5 colors
    save = [0] * 15  # colors' mark (1-45)
    color_histogram = [0] * 45  # color_histogram[1] to color_histogram[45]

    for i in range(len(colors)):
        col = np.uint8([[colors[i].rgb]])
        hsv_col = cv2.cvtColor(col, cv2.COLOR_BGR2HSV)

        save[i] = ((hsv_col[0][0][0] / 20) * 4) - (((hsv_col[0][0][0] / 20) * 4) % 4)
        if hsv_col[0][0][1] >= 128:
            save[i] += 2
            if (hsv_col[0][0][2] >= 128): save[i] += 1
        if (hsv_col[0][0][1] < 128 and hsv_col[0][0][2] >= 128): save[i] += 1

        if hsv_col[0][0][0] == 0 and hsv_col[0][0][1] == 0:
            save[i] = 35 + round(hsv_col[0][0][2] / 28)
        color_histogram[np.uint8(save[i])] += round(colors[i].proportion, 4)

    return color_histogram

def svm(path):
    dataset = pd.read_csv('svm_train_final.csv')
    X = dataset.iloc[0:6876, 0:45]
    Y = dataset.loc[:, ['ans']]

    X_train, X_test, y_train, y_test = train_test_split(X, Y, stratify=Y, test_size=0.3)

    # Important to scale
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    clf = SVC(probability=True)
    clf.fit(X_train, y_train.values.ravel())
    pred = clf.predict(X_test)

    C = genColorgram(path)
    C = sc.transform([C])
    pre1 = clf.predict(C)
    if pre1 == 'dark': style_result.set('灰暗憂鬱')
    elif pre1 == 'old': style_result.set('懷舊復古')
    elif pre1 == 'colorful': style_result.set('色彩繽紛')
    elif pre1 == 'romantic': style_result.set('浪漫柔和')
    elif pre1 == 'country': style_result.set('田園鄉村')
    return pre1

def submit_val():
    global radioValue_country, filename
    global fileindex, fatherpath, files, file_num
    fileindex += 1
    if fileindex == file_num:
        print('Done!')
        sys.exit()
    filepath2 = os.path.join(fatherpath, files[fileindex])
    show_image(filepath2, files[fileindex])
    filename = files[fileindex]


b = tk.Button(window,text = 'select a picture', command = openpicture)
b.place(relx=0.3, rely=0.1, anchor='center')

global style_result, style, style_kw
style=tk.StringVar()
style.set("風格預測結果：")
style_label = tk.Label(window, textvariable=style)
style_label.place(relx = 0.62, rely = 0.2, anchor = 'center')

style_result=tk.StringVar()
style_result.set("")
style_result_label = tk.Label(window, textvariable=style_result)
style_result_label.place(relx = 0.7, rely = 0.2, anchor = 'center')

style_kw=tk.StringVar()
style_kw.set("風格關鍵詞：")
style_kw_label = tk.Label(window, textvariable=style_kw)
style_kw_label.place(relx = 0.615, rely = 0.25, anchor = 'center')

style_kw_result=tk.StringVar()
style_kw_result.set("")
style_kw_result_label = tk.Label(window, textvariable=style_kw_result)
style_kw_result_label.place(relx = 0.7, rely = 0.25, anchor = 'center')

# 提交鍵
submit = tk.Button(window, text = '提交', command = submit_val)
submit.place(relx=0.6, rely=0.8, anchor='center')

window.mainloop()

# keyword簡體版
# country_key = ['树', '山', '云', '月', '鸟', '落日', '孤烟', '墟里', '东篱', '南山',
#                '竹林', '幽篁', '柴门', '荆扉', '林叟', '桑麻', '桑榆', '鸡豚', '几声', '芦花',
#                '溪岸', '白鹭', '沙鸥', '青草', '绿树', '青山']
#
# romantic_key = ['爱', '自由', '美', '青春', '真', '温柔', '天梯', '青冥', '云霓', '歌吟',
#                 '相思', '坚贞', '眷恋', '月光', '双飞', '花', '坚定', '华美', '理想', '黎明',
#                 '拂晓', '玫瑰']
#
# dark_key = ['伤心', '独', '孤', '愁', '渔火', '瘦马', '钟声', '乡', '客', '归',
#             '杜鹃', '天涯', '空寂', '凄寒', '雾', '愤', '忆', '寄', '离别', '沾巾',
#             '浮云', '孤蓬', '水', '泣涕', '伤', '焚', '落絮', '柳丝', '流浪', '憾恨']
#
# colorful_key = ['太阳', '青春', '翠', '缤纷', '闲逸', '清新', '深秀', '日出', '朝气', '晨光',
#                 '晨曦', '笑语', '盛夏', '嬉戏', '朝阳']
#
# old_key = ['少壮', '年少', '青丝', '朱颜', '白发', '华鬓', '寿考', '流水', '逝川', '燕子',
#            '朝露', '盛壮', '夕阳', '长亭', '落花', '怀古', '昔时', '今昔', '岁月']