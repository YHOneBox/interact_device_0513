## 第一步：安裝 Miniconda

### ✅ Windows 使用者

1. 前往 Miniconda 官方網站下載 Windows 版安裝程式：  
    [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)

2. 選擇：
   - **Python 3.10**
   - **64-bit installer**
   - 下載 `.exe` 檔後點擊安裝。

3. 安裝時請勾選：
   - ✔️「Add Miniconda to my PATH environment variable」  
   - ✔️「Register Anaconda as my default Python」

---

## 第二步：開啟終端機 (Anaconda Prompt)

安裝完成後，點擊「開始選單」找到 **Anaconda Prompt** 並打開。

---

## 第三步：建立專案環境

請在終端機依序輸入以下指令：

```bash
conda create -n webapp_env python=3.10 -y
conda activate webapp_env
```

---

## 第四步：安裝必要套件

### 1. 安裝 Flask 與 Python Dotenv：

```bash
pip install flask python-dotenv
```

### 2. 安裝 Playwright 與 Chromium 瀏覽器驅動：

```bash
pip install playwright
playwright install
```

---

## 第五步：執行程式

### 執行 Web 伺服器
(確認目錄在Interact Device)

```bash
cd face_capture
python face_capture.py
```

> 開啟後請用瀏覽器前往：`http://127.0.0.1:5000`

---

### 執行自動爬蟲程式（網頁文字擷取）
再打開anaconda prompt(目錄要切換到Interact Device)執行以下指令
```bash
python catch.py
```


---

## ❓常見問題

- 若 `playwright install` 出錯，請確認已成功安裝 Chromium 或重新執行。
- 若找不到 `python` 指令，請確認 Miniconda 有加入環境變數。
- 執行 Python 檔案前，請務必先使用 `conda activate webapp_env` 進入正確環境。

---

