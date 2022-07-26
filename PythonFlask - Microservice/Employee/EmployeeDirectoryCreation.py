
import os

class  EmployeeDirectory:
    def __init__(self):
        pass

    def creation(self,baseLocation,ifcGuid):
        listifcClass = os.listdir(baseLocation)
        if ifcGuid in listifcClass:
            print("folder exists in the building")
            return os.path.join(baseLocation, ifcGuid)
        else:
            pathifcid = os.path.join(baseLocation, ifcGuid)
            os.mkdir(pathifcid)
            return pathifcid


