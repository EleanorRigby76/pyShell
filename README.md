# pyShell

pyShell is a Python-based shell. pyShell by default has familiar commands such as `cd`, `ls`, and `cat`. Instead of `nano` as you would find on many Linux systems, you have a custom `pyedit` editor. A neofetch-esque program, `pyfetch`, is included. Any base Python command can be ran. Syntax for commands is command arg1 arg2 (so on and so forth). For instance to run `sum(10, 5)` you would run `sum 10 5`. Piping of output as would be seen in Bash and other shells is currently not supported. A minimum Python version of 3.6 is required.

## Installation

1. Ensure that `toml` is installed through pip. This [toml](https://toml.io) config file parser is needed to import packages in pyShell.
```bash
pip install toml
```

2. Clone this repository. 
```bash
git clone https://github.com/EleanorRigby76/pyShell
```

3. Navigate to the cloned repository and run `main.py`. A terminal should start with pyShell running.
Assuming the repository is located in a folder in your home directory called `pyShell` then you would run the following commands on a Linux system.
```bash
cd ~/pyShell
python3 ./main.py
```
## Login
By default pyShell comes with a login manager that uses hashes of the username and password to manage "accounts". Account permissions are handled via setting environment variables. By default a `DEBUGFLAG` environment variable is set, which determines whether a more Bash-like experience is given when a command fails, or if information pertaining to the parsing of the command is also printed. Do not assume that this login manager is secure even if the source code cannot be edited to remove calls to `login()`.

The default account is username `root` with a password of `debug` set. This account has the `DEBUGFLAG` variable set to true. Below is an example of what you will see once starting pyShell (with the login details filled out).

```
<<< Welcome to pyShell 0.1 >>>

Post login, run 'cli_help' for the pyShell manual.

pyShell login: root
Password: debug
```

## Use

pyShell attempts to translate Bash-like command syntax such as `cat a_file b_file` to a format that Python understands and then executes using the `exec()` function. "Packages" for pyShell are simply Python modules that are imported into the main file that handles syntax. Packages should be imported via editing `./.config/pyshell/shell.toml` where ./ is the location of the `main.py` file. This program does operate on real files, and does not attempt to sandbox itself any further than limitations of your interpreter. Fatal errors may occur when attempting to edit files. The built in editor, `pyEdit` is very basic and does not allow for editing as would be seen in say `nano` or `vim` in most shells. Use the `cli_help` command to view more detailed help information. By default what would typically be a home directory on UNIX systems, ~, is treated as the location where the `main.py` file is.

## License

[Public Domain / Unlicense](https://unlicense.org/)