# 메세지로 날씨 알림
from twilio.rest import Client # twilio module 사용
import requests # http 송수신 모듈

api_key = # api 키 생략
data = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q=Seoul&days=1&aqi=yes&alerts=yes").json() # 날씨 api 송수신

# 날씨 값 확인
weather_data = data["current"]["condition"]["text"]

# 날씨 값 영어를 한국어로 변경
if weather_data == "mist":
    weather_data_kr = "흐림"
elif weather_data == "Light drizzle":
    weather_data_kr = "이슬비"

# 계정 token 입력
account_sid =  # 키 생략
auth_token =  # 키 생략
client = Client(account_sid, auth_token)

# 메세지 및 송신 번호 수신 번호 입력
message = client.messages \
                .create(
                     body=f"서울 날씨는 지금 {weather_data_kr} 입니다!",
                     from_='+15855801083',
                     to= # 키 생략
                 )
# 송수신 결과 출력
print(message.sid)


