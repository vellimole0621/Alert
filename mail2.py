from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib

EMAIL_USER =  # 테스트 서버
EMAIL_PASSWORD =  # 테스트 서버 비밀번호


def make(sender, receiver, title, content, files=[]):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "%s" % (title)
    msg['From'] = sender
    msg['To'] = receiver
    html = MIMEText(content, 'html')

    msg.attach(html)

    for file in files:
        with open(file, 'rb') as fp:
            print(fp.read())
            img = MIMEImage(fp.read(), 'txt')

            msg.attach(img)

    return msg.as_string()


def templete(payload):
    return '''
    <h1>긴급 안내 문자 입니다.</h1>
    <p>{text1}</p>
    <p>{text2}</p>
  '''.format(text1=payload['text1'], text2=payload['text2'])


def send(receiver, title, payload, files=[]):
    print(receiver, payload)
    server = smtplib.SMTP_SSL('smtp.gmail.com', 587)
    server.login(EMAIL_USER, EMAIL_PASSWORD)

    html_message = templete(payload)
    body = make(EMAIL_USER, receiver, title, html_message, files)

    server.sendmail(EMAIL_USER, ['hkpythontest3@gmail.com'], body)
    server.quit()

    return True


if __name__ == '__main__':
    reveiver_email = "hkpythontest2@gmail.com"
    title = "긴급 안내 메일 입니다."
    payload = {
        "text1": "t1",
        "text2": "t2"
    }
    files = ['test.txt', 'test1.txt']
    email_res = send(reveiver_email, title, payload, files)
    print(email_res)
