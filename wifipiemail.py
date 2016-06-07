import smtplib
import credentials
server = smtplib.SMTP('smtp.gmail.com', 587)

def connect():
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(credentials.email0, credentials.password0)


def send_message(msg):
    try:
        connect()
        server.sendmail(credentials.email0, credentials.email0, msg)
        server.close()
    except:
        print 'Sending the Message Failed'







# This was done with the help of https://en.wikibooks.org/wiki/Python_Programming/Email



# Note: At the time of this writing, this requires gmail to support a less secure sign-on.
#  http://stackoverflow.com/questions/11981907/python-when-sending-email-always-blocked-in-the-clause-smtpserver-smtplib-s
# Not wanting to compromise my own account, I created another.
#  According to the forum, the changes could be changed here:
# https://www.google.com/settings/u/0/security/lesssecureapps