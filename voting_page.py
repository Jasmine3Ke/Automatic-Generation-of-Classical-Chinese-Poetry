# 引入套件
import os
import csv
import sys
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# 建立主視窗和規劃視窗
window = tk.Tk()
window.title('Voting page')
window.geometry('800x600')
window.configure(background='white')

# 設定畫布(show圖的地方)的長寬及位置
canvas = tk.Canvas(window, height=400, width=400)
canvas.place(relx=0.3, rely=0.5, anchor='center')

path = tk.StringVar() # 存路徑

global count
count = -1
cnt_i = 0

if os.path.isfile('D:\\專題資料\\vp_投票\\vote.csv')== False:
    with open('D:\\專題資料\\vp_投票\\vote.csv', 'a+', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['圖片名稱', '田園鄉村', '浪漫柔和', '懷舊復古', '灰暗憂鬱', '繽紛色彩'])

if os.path.isfile('D:\\專題資料\\vp_投票\\vote.csv'):
    if os.path.getsize('D:\\專題資料\\vp_投票\\vote.csv')== False:
        with open('D:\\專題資料\\vp_投票\\vote.csv', 'a+', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['圖片名稱','田園鄉村','浪漫柔和','懷舊復古','灰暗憂鬱','繽紛色彩'])


def resize(image):
    w, h = image.size
    mlength = max(w, h)  # 找出最大的邊
    mul = 400 / mlength  # 縮放倍數
    w1 = int(w * mul)  # 重新獲得長寬
    h1 = int(h * mul)
    return image.resize((w1, h1))

def show_image(path, name):
    global img, count, score
    image = Image.open(path)  # 開圖
    re_image = resize(image)  # 重新定義圖片尺寸 (使用resize function)
    img = ImageTk.PhotoImage(re_image)
    canvas.create_image(200, 200, anchor='center', image=img) # 在畫布上展示圖片，參數: 長, 寬, 位置, 引入圖片
    count += 1
    # score[0][count] = name

def openpicture(): # open and show image
    global fileindex, fatherpath, files, file_num, filename, cnt_i

    filepath = filedialog.askopenfilename()
    fatherpath = os.path.dirname(filepath)      # 獲取該路徑的上一級路徑
    filename = os.path.basename(filepath)   # 獲取該路徑下的文件名
    files = os.listdir(fatherpath)     # 該路徑下的所有文件並生成列表
    file_num = len(files)
    fileindex = files.index(filename)    # 獲取當前文件的索引值
    show_image(filepath, filename)
    var.set(filename)
    cnt_i = 1
    var_cnt.set(str(cnt_i) + ' / 1200')

def submit_val():
    global radioValue_country, radioValue_romantic, radioValue_old, radioValue_dark, radioValue_happy, count, filename
    with open('../../vp_投票/vote.csv', 'a+', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([filename, radioValue_country.get(), radioValue_romantic.get(), radioValue_old.get(), radioValue_dark.get(), radioValue_happy.get()])
    global fileindex, fatherpath, files, file_num, cnt_i
    fileindex += 1
    if fileindex == file_num:
        print('Done!')
        sys.exit()
        # fileindex = 0
    filepath2 = os.path.join(fatherpath, files[fileindex])
    show_image(filepath2, files[fileindex])
    filename = files[fileindex]
    var.set(filename)
    cnt_i += 1
    var_cnt.set(str(cnt_i) + ' / 1200')


b = tk.Button(window,text = 'select a picture', command = openpicture)
b.place(relx=0.3, rely=0.1, anchor='center')

global radioValue_country, radioValue_romantic, radioValue_old, radioValue_dark, radioValue_happy
# 田園鄉村
radioValue_country = tk.IntVar()
label_country = tk.Label(window, text = '田園鄉村')
label_country.place(relx = 0.62, rely = 0.2, anchor = 'center')

c_rdioOne = tk.Radiobutton(window, text='1', variable=radioValue_country, value=1)
c_rdioTwo = tk.Radiobutton(window, text='2', variable=radioValue_country, value=2)
c_rdioThree = tk.Radiobutton(window, text='3', variable=radioValue_country, value=3)
c_rdioFour = tk.Radiobutton(window, text='4', variable=radioValue_country, value=4)
c_rdioFive = tk.Radiobutton(window, text='5', variable=radioValue_country, value=5)
c_rdioOne.place(relx=0.6, rely=0.25, anchor='center')
c_rdioTwo.place(relx=0.65, rely=0.25, anchor='center')
c_rdioThree.place(relx=0.7, rely=0.25, anchor='center')
c_rdioFour.place(relx=0.75, rely=0.25, anchor='center')
c_rdioFive.place(relx=0.8, rely=0.25, anchor='center')

# 浪漫柔和
radioValue_romantic = tk.IntVar()
label_romantic = tk.Label(window, text = '浪漫柔和')
label_romantic.place(relx = 0.62, rely = 0.3, anchor = 'center')

r_rdioOne = tk.Radiobutton(window, text='1', variable=radioValue_romantic, value=1)
r_rdioTwo = tk.Radiobutton(window, text='2', variable=radioValue_romantic, value=2)
r_rdioThree = tk.Radiobutton(window, text='3', variable=radioValue_romantic, value=3)
r_rdioFour = tk.Radiobutton(window, text='4', variable=radioValue_romantic, value=4)
r_rdioFive = tk.Radiobutton(window, text='5', variable=radioValue_romantic, value=5)
r_rdioOne.place(relx=0.6, rely=0.35, anchor='center')
r_rdioTwo.place(relx=0.65, rely=0.35, anchor='center')
r_rdioThree.place(relx=0.7, rely=0.35, anchor='center')
r_rdioFour.place(relx=0.75, rely=0.35, anchor='center')
r_rdioFive.place(relx=0.8, rely=0.35, anchor='center')

# 懷舊復古
radioValue_old = tk.IntVar()
label_old = tk.Label(window, text = '懷舊復古')
label_old.place(relx = 0.62, rely = 0.4, anchor = 'center')

o_rdioOne = tk.Radiobutton(window, text='1', variable=radioValue_old, value=1)
o_rdioTwo = tk.Radiobutton(window, text='2', variable=radioValue_old, value=2)
o_rdioThree = tk.Radiobutton(window, text='3', variable=radioValue_old, value=3)
o_rdioFour = tk.Radiobutton(window, text='4', variable=radioValue_old, value=4)
o_rdioFive = tk.Radiobutton(window, text='5', variable=radioValue_old, value=5)
o_rdioOne.place(relx=0.6, rely=0.45, anchor='center')
o_rdioTwo.place(relx=0.65, rely=0.45, anchor='center')
o_rdioThree.place(relx=0.7, rely=0.45, anchor='center')
o_rdioFour.place(relx=0.75, rely=0.45, anchor='center')
o_rdioFive.place(relx=0.8, rely=0.45, anchor='center')

# 灰暗憂鬱
radioValue_dark = tk.IntVar()
label_dark = tk.Label(window, text = '灰暗憂鬱')
label_dark.place(relx = 0.62, rely = 0.5, anchor = 'center')

d_rdioOne = tk.Radiobutton(window, text='1', variable=radioValue_dark, value=1)
d_rdioTwo = tk.Radiobutton(window, text='2', variable=radioValue_dark, value=2)
d_rdioThree = tk.Radiobutton(window, text='3', variable=radioValue_dark, value=3)
d_rdioFour = tk.Radiobutton(window, text='4', variable=radioValue_dark, value=4)
d_rdioFive = tk.Radiobutton(window, text='5', variable=radioValue_dark, value=5)
d_rdioOne.place(relx=0.6, rely=0.55, anchor='center')
d_rdioTwo.place(relx=0.65, rely=0.55, anchor='center')
d_rdioThree.place(relx=0.7, rely=0.55, anchor='center')
d_rdioFour.place(relx=0.75, rely=0.55, anchor='center')
d_rdioFive.place(relx=0.8, rely=0.55, anchor='center')

# 繽紛色彩
radioValue_happy = tk.IntVar()
label_happy = tk.Label(window, text = '繽紛色彩')
label_happy.place(relx = 0.62, rely = 0.6, anchor = 'center')

h_rdioOne = tk.Radiobutton(window, text='1', variable=radioValue_happy, value=1)
h_rdioTwo = tk.Radiobutton(window, text='2', variable=radioValue_happy, value=2)
h_rdioThree = tk.Radiobutton(window, text='3', variable=radioValue_happy, value=3)
h_rdioFour = tk.Radiobutton(window, text='4', variable=radioValue_happy, value=4)
h_rdioFive = tk.Radiobutton(window, text='5', variable=radioValue_happy, value=5)
h_rdioOne.place(relx=0.6, rely=0.65, anchor='center')
h_rdioTwo.place(relx=0.65, rely=0.65, anchor='center')
h_rdioThree.place(relx=0.7, rely=0.65, anchor='center')
h_rdioFour.place(relx=0.75, rely=0.65, anchor='center')
h_rdioFive.place(relx=0.8, rely=0.65, anchor='center')

# 提交鍵
submit = tk.Button(window, text = '提交', command = submit_val)
submit.place(relx=0.6, rely=0.8, anchor='center')

var = tk.StringVar()
var.set("pic name")
picname = tk.Label(window, textvariable = var)
picname.place(relx=0.3, rely=0.9, anchor='center')

var_cnt = tk.StringVar()
var_cnt.set('0 / 1200')
cnt = tk.Label(window, textvariable = var_cnt)
cnt.place(relx=0.15, rely=0.9, anchor='center')

window.mainloop()

