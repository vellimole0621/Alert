# SMTP
# Simple Mail Transfer Protocol

# 메일을 주고받는 방법
# 각각의 메일 서버를 통과해 상대방의 컴퓨터에 이동함

import json
import smtplib # smtp 사용 위한 파이썬 모듈 smtplib

my_email = # 키 생략
my_password = # 키 생략

Alert = f"MJ in Danger!! Help her!!"

danger_act = False # 기본 화재 없음 설정

with open("danger.json", "r") as dan:
    jsonDan = json.load(dan)
    fire_alert = int(jsonDan["fire"])
    if fire_alert > 20:
        danger_act = True

    if danger_act == True: # 화재 발생시 작동
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection: # 이메일 제공자 설정, 서버 마다 다름(Gmail, Naver ... etc)
            connection.starttls() # 이메일 송수신시 보호. 암호화
            connection.login(user=my_email, password=my_password) # 송신자 로그인
            connection.sendmail(from_addr=my_email, to_addrs="hkpythontest2@gmail.com", msg=f"{Alert}")
