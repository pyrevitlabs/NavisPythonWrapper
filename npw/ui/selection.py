from npw import db
from npw import doc, API

from System.Collections.Generic import List


selection = [db.wrap(x) for x in doc.CurrentSelection.SelectedItems]


def select_items(modelitems):
    doc.CurrentSelection.Clear()
    doc.CurrentSelection.AddRange(List[API.ModelItem](modelitems))
