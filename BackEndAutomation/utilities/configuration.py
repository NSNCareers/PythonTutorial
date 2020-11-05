from configparser import ConfigParser
import pyodbc
from pyodbc import Error
import paramiko


def getValueFromPropertiesFile(self, section, sectionkey):

    parser = ConfigParser()
    files = ["BackEndAutomation/utilities/properties.ini"]
    parser.read(files)
    value = parser.get(section, sectionkey)
    return value


def sshConnectionOut(command):
    server = getValueFromPropertiesFile(None, "SSH", "server")
    port = getValueFromPropertiesFile(None, "SSH", "port")
    user = getValueFromPropertiesFile(None, "SSH", "user")
    password = getValueFromPropertiesFile(None, "SSH", "password")

    sshClient = paramiko.SSHClient()
    sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    sshClient.connect(server, port, user, password, banner_timeout=200)
    """
    stdin=> input from user can be given through this variable
    stdout=> output of command will be stored in this variable
    stderr=> errors will be tored in this variable
    """

    try:
        # sdtin, stdout, stderr = sshClient.exec_command(command)
        print("Querry was Successfull")
        result = sshClient.exec_command(command)
        sshClient.close()
        return result
    except ValueError as error:
        print("Querry was unsuccessfull")
        return error


def getSQLConnection(databseName):
    # Some other example server values are
    # server = 'localhost\sqlexpress' # for a named instance
    # server = 'myserver,port' # to specify an alternate port
    server = getValueFromPropertiesFile(None, "SQL", "server")
    database = databseName
    username = getValueFromPropertiesFile(None, "SQL", "username")
    password = getValueFromPropertiesFile(None, "SQL", "password")
    cnxn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
        + server
        + ";DATABASE="
        + database
        + ";UID="
        + username
        + ";PWD="
        + password
    )

    try:
        if cnxn.cursor() is None:
            print("Connection faiked")
        else:
            print("Connection successfull")
            cnxn.close()
            return cnxn
    except Error as e:
        print(e)


def sshConnectionFileUpload(source, destination):
    server = getValueFromPropertiesFile(None, "SSH", "server")
    port = getValueFromPropertiesFile(None, "SSH", "port")
    user = getValueFromPropertiesFile(None, "SSH", "user")
    password = getValueFromPropertiesFile(None, "SSH", "password")

    sshClient = paramiko.SSHClient()
    sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    sshClient.connect(server, port, user, password, banner_timeout=200)
    """
    stdin=> input from user can be given through this variable
    stdout=> output of command will be stored in this variable
    stderr=> errors will be tored in this variable
    """

    try:
        # sdtin, stdout, stderr = sshClient.exec_command(command)
        print("Querry was Successfull")
        sftp = sshClient.open_sftp()
        sftp.get(source, destination)
        sshClient.close()
        return sftp
    except ValueError as error:
        print("Querry was unsuccessfull")
        return error


def sshConnectionFileDownload(source, localDestination):
    server = getValueFromPropertiesFile(None, "SSH", "server")
    port = getValueFromPropertiesFile(None, "SSH", "port")
    user = getValueFromPropertiesFile(None, "SSH", "user")
    password = getValueFromPropertiesFile(None, "SSH", "password")

    sshClient = paramiko.SSHClient()
    sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    sshClient.connect(server, port, user, password, banner_timeout=200)
    """
    stdin=> input from user can be given through this variable
    stdout=> output of command will be stored in this variable
    stderr=> errors will be tored in this variable
    """

    try:
        # sdtin, stdout, stderr = sshClient.exec_command(command)
        print("Querry was Successfull")
        sftp = sshClient.open_sftp()
        sftp.put(source, localDestination)
        sshClient.close()
        return sftp
    except ValueError as error:
        print("Querry was unsuccessfull")
        return error


def sshConnectionFileDelete(serverFilePath):
    server = getValueFromPropertiesFile(None, "SSH", "server")
    port = getValueFromPropertiesFile(None, "SSH", "port")
    user = getValueFromPropertiesFile(None, "SSH", "user")
    password = getValueFromPropertiesFile(None, "SSH", "password")

    sshClient = paramiko.SSHClient()
    sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    sshClient.connect(server, port, user, password, banner_timeout=200)
    """
    stdin=> input from user can be given through this variable
    stdout=> output of command will be stored in this variable
    stderr=> errors will be tored in this variable
    """

    try:
        # sdtin, stdout, stderr = sshClient.exec_command(command)
        print("Querry was Successfull")
        sftp = sshClient.open_sftp()
        # path = sftp.listdir(path=serverFilePath)
        sftp.remove(serverFilePath)
        sshClient.close()
        return sftp
    except ValueError as error:
        print("Querry was unsuccessfull")
        return error