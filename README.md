
#  TJBot-Python (IBM Watson + Raspberry Pi)

這個專案是 IBM TJBot 專案的 Python 重製版，整合了 IBM Watson 的對話與語音服務，並結合 Raspberry Pi 硬體控制，實現語音或文字互動的聊天機器人功能。

## 🚀 功能簡介

- 💬 **Watson Assistant 聊天機器人**：理解使用者輸入、回應自然語言問題。
- 🔊 **語音互動**：使用語音辨識（Speech to Text）與語音合成（Text to Speech）與使用者溝通。
- 🤖 **硬體控制**：控制伺服馬達揮手、舉手、放下手臂，與控制 Neopixel LED 顯示顏色。

## 📁 專案檔案說明

| 檔案 | 功能說明 |
|------|-----------|
| `main.py` | 語音版主程式。透過麥克風聆聽，與 Watson Assistant 對話，並控制硬體。 |
| `typing_main.py` | 文字輸入版主程式。命令列輸入對話，適合開發或無麥克風情境。 |
| `watson_assistant.py` | 封裝 IBM Watson Assistant 聊天 API，用於發送訊息與接收回應。 |
| `text_to_speech.py` | 將 Watson Assistant 的回應轉為語音，並播放。 |
| `hardware_control.py` | 控制 Raspberry Pi 的伺服馬達與 Neopixel LED。 |
| `requirements-sudo.txt` | 安裝所需套件清單。使用 `pip install -r requirements-sudo.txt` 安裝。 |

### 🔧 測試與開發輔助檔案

| 測試程式 | 功能說明 |
|----------|-----------|
| `hardware_test.py` | 一次測試所有伺服馬達與 LED 功能（舉手、放下、揮手、變色、關燈）。 |
| `led_test.py` | 單獨測試 Neopixel LED（預設為紅燈並等待關閉）。 |
| `record_test.py` | 錄製 3 秒音訊並儲存為 `output.wav`，用來測試麥克風與音訊參數。 |
| `watson_assistant_funtion_tester.py` | 測試與 Watson Assistant API 的互動是否成功，命令列輸入對話並回應。 |
| `watson_official_simple.py` | IBM 官方簡易範例程式，確認最基本的聊天功能能正常運作。 |

## 📌 安裝與執行

### 1. 安裝必要套件

```bash
sudo pip install -r requirements-sudo.txt
```

### 2. 設定 IBM Watson API 金鑰與 URL

請至 IBM Cloud 建立下列服務並取得金鑰與 URL：

- Watson Assistant
- Text to Speech
- Speech to Text

在 `main.py`、`typing_main.py`、`watson_assistant_funtion_tester.py` 中設定：

```python
assistant_apikey = 'your-assistant-apikey'
assistant_url = 'your-assistant-url'
assistant_id = 'your-assistant-id'

tts_apikey = 'your-tts-apikey'
tts_url = 'your-tts-url'

stt_apikey = 'your-stt-apikey'
stt_url = 'your-stt-url'
```

### 3. 硬體需求與接線

- Raspberry Pi（建議使用 Pi 3 或以上）
- Servo Motor（預設接 GPIO 7）
- WS2812 Neopixel LED（預設接 GPIO 18）
- USB 麥克風或 3.5mm 麥克風（可透過 `record_test.py` 測試）

### 4. 執行互動主程式

#### 文字模式（不需麥克風）

```bash
python3 typing_main.py
```

#### 語音模式（需麥克風）

```bash
python3 main.py
```

### 5. 硬體/軟體測試（開發初期建議執行）

```bash
python3 hardware_test.py           # 測試伺服與LED
python3 record_test.py            # 測試麥克風錄音
python3 watson_assistant_funtion_tester.py  # 測試聊天機器人回應
python3 led_test.py               # 單燈測試
```

## 🧠 支援語意範例

| 意圖 (Intent) | 動作 (Action) |
|---------------|----------------|
| `wave`        | 機器人揮手 🤚 |
| `raise-arm`   | 抬起手臂 🙋‍♂️ |
| `lower-arm`   | 放下手臂 🙇 |
| `shine` + `color` | 改變 LED 顏色 🌈（支援 red, green, blue, white）|

## 📝 參考來源

- [TJBot - IBM Watson](https://github.com/ibmtjbot/tjbot)
- [IBM Cloud Watson Services](https://cloud.ibm.com/catalog)

---
