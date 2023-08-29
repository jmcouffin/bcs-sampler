# -*- coding: utf-8 -*-

from pyrevit import revit, forms, script
from pyrevit import DB as DB
from pyrevit.revit.db import query

output = script.get_output()
output.close_others()

doc = revit.doc
# uidoc = revit.uidoc

wall_instances = (
    DB.FilteredElementCollector(doc)
    .OfCategory(DB.BuiltInCategory.OST_Walls)
    .WhereElementIsNotElementType()
    .ToElements()
)

walls_windows = query.get_elements_by_categories([DB.BuiltInCategory.OST_Walls, DB.BuiltInCategory.OST_Windows])

for elem in walls_windows:
    output.print_md(elem.Name)

# output.print_md('# Hello World')
# output.print_md("{0} walls found in the model. J'ai écris cela".format(len(wall_instances)))
