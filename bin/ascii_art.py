import os
import sys

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

def py():
    print(f"""

{blu}          .?77777777777777$.              {rst}Interpreter: Python {ver}
{blu}          777..777777777777$+             {rst}Host: pyShell
{blu}         .77    7777777777$$$             {rst}Packages: {pkgs} (Modules)
{blu}         .777 .7777777777$$$$             {rst}Shell: pyShell 0.1
{blu}         .7777777777777$$$$$$             {rst}Editor: pyShell Editor 0.1
{blu}         __________:77$$$$$$$             {rst}Resolution: {termSize}
{blu}  .77777777777777777$$$$$$$$${ylw} =======.    {rst}Terminal: /dev/tty1
{blu} 777777777777777777$$$$$$$$$${ylw} ========    {rst}License: Public Domain
{blu}7777777777777777$$$$$$$$$$$$${ylw} =========   {rst}
{blu}77777777777777$$$$$$$$$$$$$$${ylw} =========   {rst}
{blu}777777777777$$$$$$$$$$$$$$$${ylw} :========+.  {rst}
{blu}77777777777$$$$$$$$$$$$$$+{ylw}  =========++~  {rst}
{blu}777777777$$  {ylw}~=====================+++++  {rst}
{blu}77777777$~ {ylw}~~~~=~=================+++++.  {rst}
{blu}777777$$$ {ylw}~~~===================+++++++.  {rst}
{blu}77777$$$$ {ylw}~~==================++++++++:   {rst}
{blu} 7$$$$$$$ {ylw}==================++++++++++.   {rst}
{blu}  ,$$$$$$ {ylw}================++++++++++~.    {rst}
{ylw}          =========~_________             {rst}
{ylw}          =============++++++             {rst}
{ylw}          ===========+++..+++             {rst}
{ylw}          ==========+++.  .++             {rst}
{ylw}           =======++++++,,++,             {rst}
{ylw}            =====+++++++++=.              {rst}Run the cli_help command to
{ylw}                ..~+=...                  {rst}view available commands.
{rst}
  """)

def trans():
  print(f"""
 
{blu}          .?77777777777777$.              {rst}Interpreter: Python {ver}
{blu}          777..777777777777$+             {rst}Host: pyShell
{blu}         .77    7777777777$$$             {rst}Packages: {pkgs} (Modules)
{blu}         .777 .7777777777$$$$             {rst}Shell: pyShell 0.1
{blu}         .7777777777777$$$$$$             {rst}Editor: pyShell Editor 0.1
{pnk}         __________:77$$$$$$$             {rst}Resolution: {termSize}
{pnk}  .77777777777777777$$$$$$$$$ =======.    {rst}Terminal: /dev/tty1
{pnk} 777777777777777777$$$$$$$$$$ ========    {rst}License: Public Domain
{pnk}7777777777777777$$$$$$$$$$$$$ =========   {rst}
{pnk}77777777777777$$$$$$$$$$$$$$$ =========   {rst}
{rst}777777777777$$$$$$$$$$$$$$$$: ========+.  {rst}
{rst}77777777777$$$$$$$$$$$$$$+  =========++~  {rst}
{rst}777777777$$  ~=====================+++++  {rst}
{rst}77777777$~ ~~~~=~=================+++++.  {rst}
{rst}777777$$$ ~~~===================+++++++.  {rst}
{pnk}77777$$$$ ~~==================++++++++:   {rst}
{pnk} 7$$$$$$$ ==================++++++++++.   {rst}
{pnk}  ,$$$$$$ ================++++++++++~.    {rst}
{pnk}          =========~_________             {rst}
{pnk}          =============++++++             {rst}
{blu}          ===========+++..+++             {rst}
{blu}          ==========+++.  .++             {rst}
{blu}           =======++++++,,++,             {rst}
{blu}            =====+++++++++=.              {rst}Run the cli_help command to
{blu}                ..~+=...                  {rst}view available commands.
{rst}
""")

def trans_sm():
  print(f"""

{blu}          .?77777777777777$.              {rst}
{blu}          777..777777777777$+             {rst}
{blu}         .77    7777777777$$$             {rst}
{blu}         .777 .7777777777$$$$             {rst}
{blu}         .7777777777777$$$$$$             {rst}
{pnk}         __________:77$$$$$$$             {rst}
{pnk}  .77777777777777777$$$$$$$$$ =======.    {rst}
{pnk} 777777777777777777$$$$$$$$$$ ========    {rst}
{pnk}7777777777777777$$$$$$$$$$$$$ =========   {rst}
{pnk}77777777777777$$$$$$$$$$$$$$$ =========   {rst}
{rst}777777777777$$$$$$$$$$$$$$$$: ========+.  {rst}
{rst}77777777777$$$$$$$$$$$$$$+  =========++~  {rst}
{rst}777777777$$  ~=====================+++++  {rst}
{rst}77777777$~ ~~~~=~=================+++++.  {rst}
{rst}777777$$$ ~~~===================+++++++.  {rst}
{pnk}77777$$$$ ~~==================++++++++:   {rst}
{pnk} 7$$$$$$$ ==================++++++++++.   {rst}
{pnk}  ,$$$$$$ ================++++++++++~.    {rst}
{pnk}          =========~_________             {rst}
{pnk}          =============++++++             {rst}
{blu}          ===========+++..+++             {rst}
{blu}          ==========+++.  .++             {rst}
{blu}           =======++++++,,++,             {rst}
{blu}            =====+++++++++=.              {rst}
{blu}                ..~+=...                  {rst}
{rst}
Interpreter: Python {ver}
Host: pyShell
Packages: {pkgs} (Modules)
Shell: pyShell 0.1
Editor: pyShell Editor 0.1
Resolution: {termSize}
Terminal: /dev/tty1
License: Public Domain
Run the cli_help command to view aval. commands.
""")

def py_sm():
    print(f"""

  {blu}          .?77777777777777$.              {rst}
  {blu}          777..777777777777$+             {rst}
  {blu}         .77    7777777777$$$             {rst}
  {blu}         .777 .7777777777$$$$             {rst}
  {blu}         .7777777777777$$$$$$             {rst}
  {blu}         __________:77$$$$$$$             {rst}
  {blu}  .77777777777777777$$$$$$$$${ylw} =======.    {rst}
  {blu} 777777777777777777$$$$$$$$$${ylw} ========    {rst}
  {blu}7777777777777777$$$$$$$$$$$$${ylw} =========   {rst}
  {blu}77777777777777$$$$$$$$$$$$$$${ylw} =========   {rst}
  {blu}777777777777$$$$$$$$$$$$$$$${ylw} :========+.  {rst}
  {blu}77777777777$$$$$$$$$$$$$$+{ylw}  =========++~  {rst}
  {blu}777777777$$  {ylw}~=====================+++++  {rst}
  {blu}77777777$~ {ylw}~~~~=~=================+++++.  {rst}
  {blu}777777$$$ {ylw}~~~===================+++++++.  {rst}
  {blu}77777$$$$ {ylw}~~==================++++++++:   {rst}
  {blu} 7$$$$$$$ {ylw}==================++++++++++.   {rst}
  {blu}  ,$$$$$$ {ylw}================++++++++++~.    {rst}
  {ylw}          =========~_________             {rst}
  {ylw}          =============++++++             {rst}
  {ylw}          ===========+++..+++             {rst}
  {ylw}          ==========+++.  .++             {rst}
  {ylw}           =======++++++,,++,             {rst}
  {ylw}            =====+++++++++=.              {rst}
  {ylw}                ..~+=...                  {rst}
  {rst}
  Interpreter: Python {ver}
  Host: pyShell
  Packages: {pkgs} (Modules)
  Shell: pyShell 0.1
  Editor: pyShell Editor 0.1
  Resolution: {termSize}
  Terminal: /dev/tty1
  License: Public Domain
  Run the cli_help command to view aval. commands.
  """)