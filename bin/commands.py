import os
import toml

reset = "\x1b[1;0m"
yellow = "\x1b[1;33m"
blue = "\x1b[1;34m"
cyan = "\x1b[1;36m"
conf = os.environ["CONF"]

with open(conf, "r") as config_file:
  conf_dict = toml.load(config_file)
  conf_parsed = toml.dumps(conf_dict)

def ls(path="Not provided"):
  if(path == "Not provided"):
    path = os.environ["DIR"]
  elif not(path.startswith("/")):
    path = os.environ["DIR"] + "/" + path
  path = path.replace("~", ".")
  files = []
  dirs = []
  for (dirpath, dirnames, filenames) in os.walk(path):
    files.extend(filenames)
    dirs.extend(dirnames)
    if dirpath.startswith("."):
      dirpath = f"~{dirpath[1:]}"
    print(f"{cyan}{dirpath}{reset}")
    break
  dirs = sorted(dirs)
  files = sorted(files)
  for dir in dirs:
    if not (dir.startswith(".") or dir == "__pycache__" or dir == "store"):
      print(f"├─ {blue}{dir}/{reset}")
      rec_files = []
      rec_dirs = []
      for (dirpath, rec_dirnames, rec_filenames) in os.walk(f"{path}/{dir}/"):
        rec_files.extend(rec_filenames)
        rec_dirs.extend(rec_dirnames)
        break
      rec_files = sorted(rec_files)
      rec_dirs = sorted(rec_dirs)
      for rec_dir in rec_dirs:
        if not (rec_dir.startswith(".") or dir == "__pycache__"):
            print(f"│  ├─ {yellow}{rec_dir}{reset}/")
      for rec_file in rec_files:
        if not (rec_file.startswith(".")):
          print(f"│  ├─ {rec_file}")
  for file in files:
    if not (file.startswith(".")):
      print(f"├─ {file}")


def clear():
  os.system("clear")


def cat(*files):
  if(len(files) == 0):
    print("cat: syntax error")
  
  else:
    for file in files:
      try:
        if (file.startswith("./")):
          file = os.environ["DIR"] + "/" + file[2:]
        elif not(file.startswith("/")):
          file = os.environ["DIR"] + "/" + file
        file = file.replace("~", ".")
        if not(os.path.isfile(file)):
          raise Exception
      except Exception:
        print(f"cat: {file}: No such file")
        return()
      with open(file, "r") as convFile:
        print(convFile.read())
        convFile.close()
        print("\n")


def cd(dir="~"):
  if (dir != "~"):
    try:
      if (dir.startswith("./")):
        dir = os.environ["DIR"] + "/" + dir[2:]
      elif not(dir.startswith("/")):
        dir = os.environ["DIR"] + "/" + dir
      dir = dir.replace("~", ".")
      if not(os.path.isdir(dir)):
        raise Exception
    except Exception:
      print(f"cd: {dir}: No such directory")
      return()
  os.environ["DIR"] = f"{dir}"

def cli_help(com="ALL"):
  cli_list = os.environ["COMMANDS"].split()
  cli_list = sorted(cli_list)
  pkg = "UNDEFINED"
  try:
    if(com == "ALL"):
      print("""
pyShell v0.1
Commands:
  """)
      for command in cli_list:
        print(command)
      print("\nUse cli_help {command} for more information on a command or cli_help ALL to see this page.")
    elif(com in cli_list):
      for package in conf_dict["pkgs"]:
        for command in conf_dict["pkgs"][package]["commands"]:
          if com == command:
            pkg = package
      print(f"{com} is from package {pkg}")
      if(conf_dict["pkgs"][pkg]["man"] != "DEFAULT"):
        man_page = f"{conf_dict['pkgs'][pkg]['man']}/{com}.md"
      else:
        man_page = f"./man/{pkg}/{com}.md"
      if(os.path.isfile(man_page)):
        with open(man_page, "r") as man_file:
          print(man_file.read())
          man_file.close()
      else:
        print(f"cli_help: CONFIG ERROR FOR {com} FROM PACKAGE {pkg}")
    else:
      raise Exception
  except Exception:
    print(f"cli_help: {com}: No such command")