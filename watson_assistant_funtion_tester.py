from watson_assistant import WatsonAssistant

# 你的 IBM Watson Assistant 和 API 配置信息
assistant_apikey = 'N4ROgFLSFheVexFDKTB8aQdyvclGz6QdfJEeXxHqPcAQ'  # 替換為你的 API 金鑰
assistant_url = 'https://api.au-syd.assistant.watson.cloud.ibm.com/instances/8616d148-c668-4225-b8d7-dbde21052795'  # 替換為你的服務 URL
assistant_id = 'ae4f08ab-8988-4c06-9617-134169c58ee3'  # 替換為你的 Assistant ID

# 測試與 Watson Assistant 交互的程式
def test_watson_assistant():
    # 初始化 WatsonAssistant 物件
    assistant = WatsonAssistant(assistant_apikey, assistant_url, assistant_id, version='2023-04-15')
    
    # 開始與 Watson Assistant 的對話
    while True:
        user_input = input("You: ").strip()
        if not user_input:
            print("No input detected. Please try again.")
            continue
        
        if "quit" in user_input.lower():
            print("Exiting...")
            break
        
        # 發送訊息到 Watson Assistant
        response = assistant.send_message(user_input)
        
        if response:
            # 提取 Assistant 的回應文本
            response_texts = response.get('output', {}).get('generic', [])
            
            for text in response_texts:
                if text['response_type'] == 'text':
                    print(f"TJBot: {text['text']}")  # 打印 Assistant 的回應
        else:
            print("No response from Assistant.")

# 執行測試
if __name__ == "__main__":
    test_watson_assistant()
