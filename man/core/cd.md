  # NAME
cd - changes the current working directory.

  # SYNOPSIS
cd [path]

  # DESCRIPTION
Changes the working directory used by pyShell packages. This modifies an environment variable named "DIR" which is referenced by other packages and programs that refer to the current direcrory. Running 'cd' without a path will restore the working directory to pyShell's default - which is the directory containing 'main.py', your 'bin' folder, and other core components of pyShell.

  # ADD. INFO
This implementation of 'cd' in Python for pyShell is packaged alongside the main pyShell package in the core command library. It is public domain software made by Ellie.