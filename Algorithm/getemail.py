import poplib
import email
from email.header import decode_header
from email.utils import parsedate_to_datetime
from datetime import datetime, timedelta
import time

def decode(header: str):
    value, charset = email.header.decode_header(header)[0]
    if charset:
        return str(value, encoding=charset)
    else:
        return value

POP3_HOST = 'hqp.mail.chinaunicom.cn'
POP3_PORT = 995
POP3_USER = 'hqs-gylyw@chinaunicom.cn'
POP3_PASS = 'q4ciiFOB@'

pop3_conn = poplib.POP3_SSL(POP3_HOST, POP3_PORT)
pop3_conn.user(POP3_USER)
pop3_conn.pass_(POP3_PASS)

msg_count, _ = pop3_conn.stat()

now = datetime.now()
today_start = datetime(now.year, now.month, now.day)
today_end = today_start + timedelta(days=1)

three_hours_ago = now - timedelta(hours=4)
three_hours_ago_timestamp = int(time.mktime(three_hours_ago.timetuple()))
today_start_timestamp = int(time.mktime(today_start.timetuple()))
today_end_timestamp = int(time.mktime(today_end.timetuple()))

#attachment_folder = 'C://Users//孙先生//Desktop//串码导入//'
#E:\工作\RPA\每日串码导入
attachment_folder = 'E://工作//RPA//每日串码导入//'


for i in range(msg_count):
    try:
        _, msg_bytes, _ = pop3_conn.retr(i + 1)
        print(f"Processed {i} successfully")
        msg_cont = b'\r\n'.join(msg_bytes)
        msg = email.message_from_bytes(msg_cont)

        date_tuple = parsedate_to_datetime(msg['Date'])
        email_timestamp = int(time.mktime(date_tuple.timetuple()))

        if three_hours_ago_timestamp <= email_timestamp < today_end_timestamp:
            subject_header = decode_header(msg['Subject'])[0]
            if isinstance(subject_header[0], bytes):
                subject = subject_header[0].decode(subject_header[1])
            else:
                subject = subject_header[0]
            if '串码导入' in subject:
                print(f"Subject: {decode_header(msg['Subject'])[0][0]}")
                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_disposition() == 'attachment':
                            attachment_name = decode(part.get_filename())
                            attachment_content = part.get_payload(decode=True)
                            attachment_file = open(attachment_folder + attachment_name, 'wb')
                            attachment_file.write(attachment_content)
                            attachment_file.close()
            print('Done attachment...')
            print("---")

    except Exception as e:
        print(f"An error occurred while processing {i}")

pop3_conn.quit()