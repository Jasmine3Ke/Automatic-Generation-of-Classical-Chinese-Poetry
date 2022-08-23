# :art:  Automatic Generation of Classical Chinese Poetry

* **Research topic:** Automatic Generation of Classical Chinese Poetry Based on Image and Color of Paintings
* **Authors:** Mei-Ren Ke, An-Ting Hsieh, I-Cheng Yeh

### :ballot_box_with_check:  To-Do
* [ ] import WMPoetry

### :kissing_cat:  Keypoints
* Compressed a 45-dimensions feature vector via one-hot encoding and inputted to support vector machine
* Trained support vector machine and conducted style prediction

### :robot:  Quick Setup (Basic Usage)
#### 1. Build a virtual environment (Anaconda 4.7.12):
``` 
conda create --name myenv python=3.8.13 
conda activate myenv
conda install pandas
conda install scikit-learn
conda install pillow
conda install opencv
```

#### 2. Execute: 
```
python style_result_page.py
```

<img src="example.png" width="50%" height="50%" >

* 視窗出現後，按"select a picture"選圖片
* 按"提交"之後，會開始預測同個資料夾內下一張圖片的風格

### :speech_balloon:  Contact
Feel free to reach me at any time.
<pre><code>Email: meirenke4@gmail.com
LinkedIn: https://www.linkedin.com/in/mei-ren-ke-7136641a5/ </code></pre>