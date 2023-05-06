import serial

# 라즈베리파이에 시리얼통신으로 값 수신 코드

ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)
ser.open()

ser.write("testing")
try:
    while 1:
        response = ser.readline()
except KeyboardInterrupt:
    ser.close()

