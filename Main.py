import os.path


def TakeNotes():
  isRunning = True
  print(bcolors.HEADER + "Welcome to TakeNotes!" + bcolors.ENDC)
  print(getCommandList())
  while isRunning:
    commandInput = input(">>> ")
    if commandInput == "help":
      print(getCommandList())
    elif commandInput == "exit":
      isRunning = False
    elif commandInput == "create":
      createFile()
    elif commandInput == "delete":
      deleteFile()
    elif commandInput == "read":
      readFile()
    else:
      print("Command not found. Run 'help' to list all commands.")


def getCommandList():
  commandList = bcolors.BOLD + \
  "create: Create a txt file\n \
  delete: Delete a file\n \
  read: Read a file\n \
  write: Write to a file\n \
  isopen: Check if a file is open in current Python process\n \
  help: List all commands\n \
  exit: Exit program" \
  + bcolors.ENDC
  return commandList


def createFile():
  fileNameCreate = getTextFile()
  try:
    fileCreated = open(fileNameCreate, "x")
    print(f"File {fileCreated.name} created!")
  except Exception as exception:
    print(exception)
  fileCreated.close()


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


def getTextFile():
  fileNameInput = input("Enter a file name: ")
  fileName = ""
  if not ".txt" in fileNameInput:
    fileName = fileNameInput + ".txt"
  else:
    fileName = fileNameInput
  return fileName


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