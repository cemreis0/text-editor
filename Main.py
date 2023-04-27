import os.path


def Main():
  isRunning = True
  print(bcolors.HEADER + "Welcome to TakeNotes!" + bcolors.ENDC)
  commandList = bcolors.BOLD + \
  "create: Create a txt file\ndelete: Delete a file\nread: Read a file\nwrite: Write to a file\nhelp: List all commands" \
  + bcolors.ENDC
  print(commandList)
  while isRunning:
    commandInput = input(">>> ")
    if commandInput == "help":
      print(commandList)
    elif commandInput == "create":
      fileNameCreate = input("Enter a name for the file: ")
      try:
        with open(fileNameCreate + ".txt", 'x'):
          print("File created!")
      except Exception as exception:
        print(exception)
        continue
    elif commandInput == "delete":
      fileNameDelete = input("Enter the file name to delete: ")
      try:
        os.remove(os.getcwd() + "\\" + fileNameDelete + ".txt")
        print("File deleted!")
      except Exception as exception:
        print(exception)
        continue
    else:
      print("Command not found. Run help to list all commands.")


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


Main()