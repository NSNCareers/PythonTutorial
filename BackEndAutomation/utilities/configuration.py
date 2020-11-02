from configparser import ConfigParser


def getValueFromPropertiesFile(self, section, sectionkey):

    parser = ConfigParser()
    files = ["BackEndAutomation/utilities/properties.ini"]
    parser.read(files)
    value = parser.get(section, sectionkey)
    return value