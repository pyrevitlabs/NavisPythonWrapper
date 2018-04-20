import clr

clr.AddReference('Autodesk.Navisworks.Api')
clr.AddReference('Autodesk.Navisworks.ComApi')
clr.AddReference('Autodesk.Navisworks.Interop.ComApi')
import Autodesk.Navisworks.Api as API
import Autodesk.Navisworks.Api.ComApi as COMAPI
import Autodesk.Navisworks.Api.Interop.ComApi as ICOMAPI

doc = API.Application.ActiveDocument
