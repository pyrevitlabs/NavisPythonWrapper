import clr

clr.AddReference('Autodesk.Navisworks.Api')
clr.AddReference('Autodesk.Navisworks.ComApi')
import Autodesk.Navisworks.Api as API
import Autodesk.Navisworks.Api.ComApi as COMAPI


doc = API.Application.ActiveDocument
