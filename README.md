# Automatic Generation of Classical Chinese Poetry

**Research topic: Automatic Generation of Classical Chinese Poetry Based on Image and Color of Paintings**

## To-Do
* [ ] 導入WMPoetry
* [ ] 整合成一個step就可以跑

## Quick Setup (Basic Usage)
### 1. Build a virtual environment (Anaconda 4.7.12):
``` 
conda create --name myenv python=3.8.13 
conda activate myenv
conda install pandas
conda install scikit-learn
conda install pillow
conda install opencv
```

### 2. Execute: 
```
python style_result_page.py
```
視窗出現後，按"select a picture"選圖片

## Contact
Feel free to reach me at any time.
<pre><code>Email: meirenke4@gmail.com
LinkedIn: https://www.linkedin.com/in/mei-ren-ke-7136641a5/ </code></pre>

## conda note
* `conda -V` : 檢查版本
* `conda update conda` : 更新conda
* `conda env list` : conda環境列表
* `conda create --name myenv python=3.7` : 建conda虛擬環境

* `activate myenv` : 啟動某環境
* `conda list` : 看這個環境底下有什麼東西
* `conda install numpy` : 安裝某套件
* `conda deactivate` : 離開環境

* `conda remove --name myenv numpy` : 刪除某個package
* `conda env remove --name myenv` : 刪除整個環境
