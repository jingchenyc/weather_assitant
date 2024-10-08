# -*- coding: utf-8 -*-
"""linebot_get_weather.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kG5c4VF5pt0RjHgs0gQbJh2HZ2wSNcWo
"""

# cloud function 上執行的模組 get_weather.py
# weather() 函式輸入縣市名稱，輸出天氣預報內容
import requests

def weather(raw_location_input):
    url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001"
    headers = {"Authorization": 你的API Key}
    params = {"format": "JSON"}

    res = requests.get(url, headers=headers, params=params)

    # 檢查請求是否成功
    if res.status_code == 200:

        # 解析 JSON 回應
        data_json = res.json()

        # 提取包含位置資訊的資料集
        dataset = data_json["records"]["location"]

        # 建立位置名稱轉換字典
        location_mapping = {
            "台": "臺",
            # 其他地區的對應
        }


        # 將使用者輸入的 "台" 字轉換為 "臺"
        location_input = raw_location_input.replace("台", "臺")

        # 迭代資料集以查找輸入的位置
        for i in dataset:
            if i["locationName"] == location_input:

                # 提取指定位置的天氣資訊
                city = i['locationName']    # 縣市名稱
                wx8 = i['weatherElement'][0]['time'][0]['parameter']['parameterName']    # 天氣現象
                pop8 = i['weatherElement'][1]['time'][0]['parameter']['parameterName']  # 降雨機率
                mint8 = i['weatherElement'][2]['time'][0]['parameter']['parameterName']  # 最低溫
                ci8 = i['weatherElement'][3]['time'][0]['parameter']['parameterName']    # 舒適度
                maxt8 = i['weatherElement'][4]['time'][0]['parameter']['parameterName']   # 最高溫

                output_msg = f"地點：{city}\n" + f"天氣描述：{wx8}\n" + f"氣溫：{mint8} ~ {maxt8} 度\n" + f"降雨機率：{pop8}%\n" + f"感覺：{ci8}\n"

                # 根據最低溫度(mint8)和降雨機率(pop8)確定穿著建議
                advice = "是" if int(pop8) >= 30 else "否"
                output_msg += f"是否攜帶雨具：{advice}\n"

                if int(mint8) <= 15:
                    cloth = "天氣有點冷，建議多穿一點，可以考慮穿上羽絨衣來保暖。"
                elif int(mint8) <= 20:
                    cloth = "溫度稍微降低，穿上長袖搭配外套可能會更舒適。"
                elif int(mint8) <= 25:
                    cloth = "天氣宜人，可以穿上長袖享受一下清爽的氣候。"
                else:
                    cloth = "天氣溫暖，穿上清涼透氣的衣物，讓自己享受一下夏天。"

                output_msg += f"建議穿著：{cloth}"

                return output_msg
                break
        else:
            # 如果未找到位置，提示使用者輸入正確位置
            return "請輸入正確位置"
    else:
        # 如果請求不成功，列印錯誤訊息
        return f"Error: {res.status_code} - {res.text}"

