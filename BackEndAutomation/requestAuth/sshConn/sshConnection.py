import paramiko
from BackEndAutomation.utilities.configuration import *


class SSHCnnect:
    def sendCommandToServer(self, command):
        stdout = sshConnectionOut(command)
        return stdout

    def uploadFileToServer(self):
        source = "BackEndAutomation/bashFiles/startJenkins.py"
        destination = "/home/elvis/pythonDemo/startJenkins.py"
        stdout = sshConnectionFileDownload(source, destination)
        return stdout

    def downloadFileFromServer(self):
        destination = "BackEndAutomation/outPutFolder/startJenkins.py"
        source = "/home/elvis/pythonDemo/startJenkins.py"
        stdout = sshConnectionFileUpload(source, destination)
        return stdout

    def deleteFileFromServer(self):
        filePath = "/home/elvis/pythonDemo/startJenkins.py"
        stdout = sshConnectionFileDelete(filePath)
        return stdout


if __name__ == "__main__":
    # SSHCnnect().deleteFileFromServer()
    # SSHCnnect().downloadFileFromServer()
    # SSHCnnect().uploadFileToServer()
    SSHCnnect().sendCommandToServer("sudo service jenkins restart")
