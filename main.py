import serial, time, pynmea2
from twilio.rest import Client
import googlemaps
import spidev

# 화재 감지
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 500000


def read_spi_adc(adcChannel):
    adcValue = 0
    buff = spi.xfer2([1, (8 + adcChannel) << 4, 0])
    adcValue = ((buff[1] & 3) << 8) + buff[2]
    return adcValue


try:
    while True:
        adcChannel = 0
        adcValue = read_spi_adc(adcChannel)
        time.sleep(0.2)

except KeyboardInterrupt:
    spi.close()

# GPS
"""
필요한 gpsd 라이브러리 설치
sudo apt install gpsd,gpsd-clients
pip3 install gpsd-py3
"""

"""
gps 사용 시작
sudo systemctl stop gpsd
sudo systemctl stop gpsd.socket
sudo systemctl disable gpsd.socket
sudo gpsd /dev/ttyACM0 -F /var/run/gpsd.sock
"""

# 라즈베리파이 시리얼 통신
port = '/dev/ttyACM0'
baud = 9600
serialPort = serial.Serial(port, baudrate=baud, timeout=0.5)

while True:
    str = serialPort.readline().decode().strip()
    # print(str)
    if str.find('GGA') > 0:
        msg = pynmea2.parse(str)
        mj_latitude = round(msg.latitude, 6)
        mj_longitude = round(msg.longitude, 6)
    time.sleep(0.01)

googlemaps_API = -# API 값

gmaps = googlemaps.Client(key=googlemaps_API)  # api key
reverse_geocode_result = gmaps.reverse_geocode((mj_latitude, mj_longitutde), language='ko')
mj_gps = reverse_geocode_result[1]['formatted_address']

# 메세지

# 계정 token 입력
account_sid = -
auth_token = -
client = Client(account_sid, auth_token)

# 위험 감지
danger_act = False  # 기본 위험 없음 설정

# 화재 감지값 900 이상일 때, 화재라 판단
if adcValue > 900:
    danger_act = True

if not danger_act:
    pass

# 메세지 송신
else:
    message = client.messages \
        .create(
        body=f"위험 위험!!, 할머니가 위험해요. 종류 : 화재 발생 // 위치 : {mj_gps} ",
        from_= -
        to=-
    )
    # 다시 위험 없음으로 변경
    danger_act = False
