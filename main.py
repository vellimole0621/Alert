from twilio.rest import Client
import serial
import json
import googlemaps

# Twilio
# 계정 token 입력
account_sid =
auth_token =
client = Client(account_sid, auth_token)

# GPS 위치 가져오기
file_path = "/home/pi/Desktop/GPS/gps_info.json"
with open(file_path, "r") as json_file:
    json_data = json.load(json_file)
    latitude = json_data["gps"][0]["latitude"]
    longitude = json_data["gps"][0]["longitude"]

# 위도 경도 -> 지번 주소로 변경 // 역지오코드

API =  # API 값

gmaps = googlemaps.Client(key=API) # api key
reverse_geocode_result = gmaps.reverse_geocode((latitude, longitude), language='ko')
gps = reverse_geocode_result[1]["formatted_address"]

message_send = 1 # 메세지 송신 트리거

# 화재 감지 코드
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM1', 9600, timeout=1)
    ser.flush()
    while True:
        if ser.in_waiting > 0 :
            line = ser.readline().decode('utf-8').rstrip()
            s_line = int(line)
            if s_line > 200:
                message_send *= -1

            if message_send < 0: # 실험을 위해서 200을 기준으로 설정
                message = client.messages \
                    .create(
                    body=f"위험 위험!!, 할머니가 위험해요. 종류 : 화재 발생. 위치는 {gps}",
                    from_=
                    to=
                )
                message_send = 0



