import os
import smtplib


def send_email(sender_email, sender_password, recipient_email, subject, message):
    # 连接到SMTP服务器
    with smtplib.SMTP("smtp.qq.com", 587) as server:
        server.starttls()
        # 登录到你的邮箱账户
        server.login(sender_email, sender_password)

        # 构建邮件内容
        email_message = f"From: {sender_email}\nSubject: {subject}\n\n{message}"

        # 发送邮件
        server.sendmail(sender_email, recipient_email, email_message.encode('utf-8'))


        # 断开与服务器的连接
        server.quit()



if __name__ == '__main__':
    sender_email = "3010528988@qq.com"  # 发件人邮箱
    sender_password = "jugyapxfxvlhdcii"  # 发件人邮箱密码
    recipient_email = '3010528988@qq.com'  # 收件人邮箱
    subject = "IPV6"  # 邮件主题
    message = os.popen("ipconfig").read()  # 邮件内容
    send_email(sender_email, sender_password, recipient_email, subject, message)