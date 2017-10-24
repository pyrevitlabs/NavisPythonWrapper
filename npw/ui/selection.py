from npw import db
from npw import doc


selection = [db.wrap(x) for x in doc.CurrentSelection.SelectedItems]
