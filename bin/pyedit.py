def pyedit(file, mode):
  if(mode=="a"):
    print(f"{file} is being APPENDED.")
    print("Hit enter to write new line to file. Type ':q' and press enter to quit.")
    print("BEGIN FILE CONTENTS ON NEW LINE\n")
    with open(file, "r") as readFile:
      for line in readFile:
        print(line)
    with open(file, "a") as convFile:
      convFile.write("\n")
      while(True):
        line = input()
        if(line==":q"):
          convFile.close()
          break
        else:
          convFile.write(f"{line}\n")
  if(mode=="ow"):
    print(f"{file} is being OVERWRITTEN.")
    print("Hit enter to write line to file. Type ':q' and press enter to quit.")
    print(" ")
    with open(file, "w") as convFile:
      while(True):
        line = input()
        if(line==":q"):
          convFile.close()
          break
        else:
          convFile.write(f"{line}\n")