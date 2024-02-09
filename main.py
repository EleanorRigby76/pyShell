import os
import toml

os.environ["DIR"] = str("~")
os.environ["COMMANDS"] = str("")

from login_man import login, logout, adduser
from correct import correct_command

# This defines your TOML config file, used for packages and in the future other settings
conf = "./.config/pyshell/shell.toml"
os.environ["CONF"] = conf
with open(conf, "r") as config_file:
  conf_dict = toml.load(config_file)
  conf_parsed = toml.dumps(conf_dict)

green = "\x1b[1;32m"
reset = "\x1b[0;0m"

# Logic for initializing packages from shell.toml
print("Initializing packages.")
for package in conf_dict["pkgs"]:
  file = conf_dict["pkgs"][package]["file"]
  for command in conf_dict["pkgs"][package]["commands"]:
    exec(f"from bin.{file} import {command}")
    commands = os.environ["COMMANDS"]
    os.environ["COMMANDS"] = str(f"{commands} {command}")
    print(f"Initialized {command} from package {package}")


# Logic for the shell prompt - getting command, parsing, and executing.
def shell():
  # Ensures that variables are updated before displaying prompt.
  debugFlag = bool(os.environ["DEBUGFLAG"] == "True")
  dir = os.environ["DIR"]
  if(dir.startswith(".")):
    dir = f"~{dir[1:]}"
  user = os.environ["LOGIN"]
  doCorrect = ""
  # Prompts user for command.
  shell_prompt = str(input(f"{green}[{user}@pyShell:{dir}]${reset} "))
  # Splits the prompt for processing.
  splitPrompt = shell_prompt.split()
  com = "print(f'ERROR: No command entered.'"
  try:  # Parses and executes the command.
    if (len(splitPrompt) == 1):
      com = f"{splitPrompt[0]}()"
      exec(f"{splitPrompt[0]}()")
    else:
      for position, split in enumerate(splitPrompt):
        com = split + "(" if position == 0 else com + f"'{split}'" + ","
      comstr = str(com)
      if (comstr.endswith(",")):
        com = com[:-1]
      exec(f"{com})")
  # Exception handling
  except Exception as ncom:
    if (str(ncom).endswith("not defined")):
      acor = correct_command(splitPrompt[0])
      print(
          f"No command '{splitPrompt[0]}' found, did you mean: \n command '{acor}'"
      )
    else:
      print(f"{splitPrompt[0]}: syntax error")
    if (debugFlag):
      print(f"DEBUG IFNO: {ncom}")
      print(f"ATTEMPTED RUNNING COMMAND: {com})")
      print(' ')
    # Command correction attempt
    if (str(ncom).endswith("not defined")):
      acor = correct_command(splitPrompt[0])
      while (doCorrect != "YES" and doCorrect != "NO"):
        doCorrect = str(input("Attempt to correct? (Y / N) "))
        doCorrect = doCorrect.upper()
        if (doCorrect == "Y"):
          doCorrect = "YES"
        if (doCorrect == "N"):
          doCorrect = "NO"
        if (doCorrect == "YES"):
          count = 0
          for split in splitPrompt:
            count += 1
            com = acor + "(" if count == 1 else com + f"'{split}'" + ","
          comstr = str(com)
          if (comstr.endswith(",")):
            com = com[:-1]
          try:
            exec(f"{com})")
          except Exception as ncom:
            print(f"{splitPrompt[0]}: syntax error")
            if (debugFlag):
              print(f"DEBUG IFNO: {ncom}")
              print(f"ATTEMPTED RUNNING COMMAND: {com})")
              print(' ')


login()
while (True):
  shell()
