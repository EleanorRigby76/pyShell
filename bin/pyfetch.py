import os
import sys

def pyfetch(ascii="Default"):
  ascii = ascii.upper()
  cli_list = os.environ["COMMANDS"].split()
  pkgs = len(cli_list)
  try:
    ver = f"{sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}"
  except Exception:
    ver = "UNDEFINED"
  try:
    termSize = f"{os.get_terminal_size()[0]} COL. x {os.get_terminal_size()[1]} LN."
    cols = os.get_terminal_size()[0]
  except Exception:
    termSize = "UNDEFINED"
    cols = 0
  rst = "\x1b[1;0m"
  blu = "\x1b[1;34m"
  ylw = "\x1b[1;33m"
  pnk = "\x1b[38;5;212m"
  if (cols >= 80):
    if(ascii == "TRANS"):
      from bin.ascii_art import trans
      trans()
    else:
      from bin.ascii_art import py
      py()
  else:
    if(ascii == "TRANS"):
      from bin.ascii_art import trans_sm
      trans_sm()
    else:
      from bin.ascii_art import py_sm
      py_sm()
    print(" ")
