import hashlib
import os
from time import sleep


commands = os.environ["COMMANDS"]
os.environ["COMMANDS"] = str(f"{commands} logout adduser")

# Define files for login information
superuser_file = "./.config/pyshell/su.conf"
user_file = "./.config/pyshell/user.conf"

su_list = []
user_list = []
with open(superuser_file, "r") as su_file:
  su_file = su_file.read()
  su_file_split = su_file.split("\n")
  for line in su_file_split:
    if not(line.startswith("#")):
      su_list.append(line)
with open(user_file, "r") as u_file:
  u_file = u_file.read()
  u_file_split = u_file.split("\n")
  for line in u_file_split:
    if not(line.startswith("#")):
      user_list.append(line)
uline = "\x1b[5;39m"
green = "\x1b[1;32m"
reset = "\x1b[0;0m"

def login():
  os.system("clear")
  print(f"{green}<<< Welcome to pyShell 0.1 >>>{reset}\n")
  print("Post login, run 'cli_help' for the pyShell manual.\n")
  while (True):
    login_prompt = str(input("pyShell login: "))
    pswd_prompt = str(input("Password: "))
    pswd_hash = hashlib.sha256(
        (pswd_prompt + login_prompt).encode('utf-8')).hexdigest()
    superhash = pswd_hash
    for i in range(len(pswd_prompt)):
      superhash = hashlib.sha256(superhash.encode('utf-8')).hexdigest()
    if (superhash in su_list):
      debugFlag = True
      os.system("clear")
      print(f"Successfully logged into account {login_prompt}.")
      os.environ["DEBUGFLAG"] = str(debugFlag)
      os.environ["LOGIN"] = str(login_prompt)
      os.environ["DIR"] = str("~")
      return (debugFlag, login_prompt)
    elif (superhash in user_list):
      debugFlag = False
      os.system("clear")
      print(f"Successfully logged into account {login_prompt}.")
      os.environ["DEBUGFLAG"] = str(debugFlag)
      os.environ["LOGIN"] = str(login_prompt)
      os.environ["DIR"] = str("~")
      return (debugFlag, login_prompt)
    else:
      print("Login incorrect")
      print(f"DEBUG STRING BELOW: \n{superhash}")


def logout():
  os.system("clear")
  print(f"{uline}Logging out.{reset}")
  sleep(1)
  login()

def adduser():
  login = str(input("New login: "))
  pswd = "."
  pswd_conf = "!"
  while(pswd != pswd_conf):
    pswd = str(input(f"Password for {login} : "))
    pswd_conf = str(input(f"Confirm password for {login} : "))
    if(pswd != pswd_conf):
      print("Passwords do not match!")
  pswd_hash = hashlib.sha256(
        (pswd + login).encode('utf-8')).hexdigest()
  superhash = pswd_hash
  for i in range(len(pswd)):
    superhash = hashlib.sha256(superhash.encode('utf-8')).hexdigest()
  is_superuser = (" ")
  while not(is_superuser == "YES" or is_superuser == "NO" or is_superuser == "Y" or is_superuser == "N"):
    is_superuser = str(input("Is this account a superuser? (Y / N) "))
    is_superuser = is_superuser.upper()
    if(is_superuser == "Y" or is_superuser == "YES"):
      with open(superuser_file, "a") as su_file:
        su_file.write(f"\n# {login}")
        su_file.write(f"\n{superhash}")
        su_file.close()
    elif(is_superuser == "N" or is_superuser == "NO"):
      with open(user_file, "a") as u_file:
        u_file.write(f"\n# {login}")
        u_file.write(f"\n{superhash}")
        u_file.close()