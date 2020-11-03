from configparser import ConfigParser
import pyodbc


def getValueFromPropertiesFile(self, section, sectionkey):

    parser = ConfigParser()
    files = ["BackEndAutomation/utilities/properties.ini"]
    parser.read(files)
    value = parser.get(section, sectionkey)
    return value


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

    if cnxn:
        pass
    return cnxn