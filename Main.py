import os.path


def TakeNotes():
  isRunning = True
  print(bcolors.HEADER + "Welcome to TakeNotes!" + bcolors.ENDC)
  print(getCommandList())
  while isRunning:
    commandInput = input(">>> ")
    if commandInput == "create":
      createFile()
    elif commandInput == "delete":
      deleteFile()
    elif commandInput == "read":
      readFile()
    elif commandInput == "write":
      writeFile()
    elif commandInput == "exit":
      isRunning = False
    elif commandInput == "help":
      print(getCommandList())
    else:
      print("Command not found. Run 'help' to list all commands.")


def createFile():
  fileNameCreate = getTextFile()
  try:
    fileCreated = open(fileNameCreate, "x")
    print(f"File {fileCreated.name} created!")
    fileCreated.close()
  except Exception as exception:
    print(exception)


def deleteFile():
  fileNameDelete = getTextFile()
  try:
    os.remove(os.getcwd() + "\\" + fileNameDelete)
    print(f"File {fileNameDelete} deleted!")
  except Exception as exception:
    print(exception)


def readFile():
  fileNameRead = getTextFile()
  try:
    fileRead = open(fileNameRead, "r")
    print(fileRead.read())
    fileRead.close()
  except Exception as exception:
    print(exception)


def writeFile():
  fileNameWrite = getTextFile()
  try:
    fileWritten = open(fileNameWrite, "r")
    lines = fileWritten.readlines()
    fileWritten.close()
    if len(lines) != 0:
      for index in range(len(lines)-1):
        print(f"#{index+1}  {lines[index]}", end = "")
      print(f"#{len(lines)}  {lines[len(lines)-1]}")
      lineIndexInput = input("Enter the index of the line that you want to change, type 'new' to add new line: ")
      lineTextInput = input("Enter your new text: ")
      if lineIndexInput == "new":
        fileWritten = open(fileNameWrite, "a")
        fileWritten.write("\n" + lineTextInput)
        print(bcolors.OKGREEN + "Changes saved!" + bcolors.ENDC)
        fileWritten.close()
      else:
        lines[int(lineIndexInput)-1] = lineTextInput
        fileWritten = open(fileNameWrite, "w")
        fileWritten.writelines(lines)
        print(bcolors.OKGREEN + "Changes saved!" + bcolors.ENDC)
        fileWritten.close()
    else:
      fileWritten = open(fileNameWrite, "w")
      textInput = input("Enter your new text: ")
      fileWritten.write(textInput)
      print(bcolors.OKGREEN + "Changes saved!" + bcolors.ENDC)
      fileWritten.close()
  except Exception as exception:
    print(exception)

def getTextFile():
  fileNameInput = input("Enter a file name: ")
  fileName = ""
  if not ".txt" in fileNameInput:
    fileName = fileNameInput + ".txt"
  else:
    fileName = fileNameInput
  return fileName


def getCommandList():
  commandList = (
    bcolors.OKBLUE + 
    "create: Create a txt file\n"
    "delete: Delete a file\n"
    "read: Read a file\n"
    "write: Write to a file\n"
    "exit: Exit program"
    + bcolors.ENDC
  )
  return commandList


class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
  def disable(self):
    self.HEADER = ''
    self.OKBLUE = ''
    self.OKGREEN = ''
    self.WARNING = ''
    self.FAIL = ''
    self.ENDC = ''
    self.BOLD = ''
    self.UNDERLINE = ''


TakeNotes()