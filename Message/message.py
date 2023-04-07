# twilio 사용 메세지

# twilio module 사용
from twilio.rest import Client

# 계정 token 입력
account_sid = # 키 생략
auth_token = # 키 생략
client = Client(account_sid, auth_token)

# 메세지 및 송신 번호 수신 번호 입력
message = client.messages \
                .create(
                     body="MJ in Danger!!",
                     from_='+15855801083',
                     to=# 키 생략
                 )

# 송수신 결과 출력
print(message.sid)
