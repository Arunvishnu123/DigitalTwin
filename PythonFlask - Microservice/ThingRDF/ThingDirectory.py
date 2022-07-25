import os
class ThingDirectory:
    def __init__(self):
        pass

    def creation(self,ifcClass,ifcGuid,parameterName,location):
        listifcClass =os.listdir(location)
        if ifcClass in listifcClass:
          print("ifc Class exist in the thing directory")
          pathIFCguid =  os.path.join(location,ifcClass)
          listifcGuid = os.listdir(pathIFCguid)
          if ifcGuid in listifcGuid:
              pathifcid = os.path.join(pathIFCguid , ifcGuid)
              return pathifcid
          else:
              pathifcid = os.path.join(pathIFCguid, ifcGuid)
              os.mkdir(pathifcid)
              return pathifcid
        else:
          path = os.path.join(location, ifcClass)
          os.mkdir(path)
          path1 = os.path.join(path, ifcGuid)
          os.mkdir(path1)
          return path1







