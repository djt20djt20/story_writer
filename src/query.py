from tinydb import Query

def query_data(db, element_type=None, draft=None):
    NovelQuery = Query()

    table = db.table(element_type) if element_type else db

    query = None
    if draft:
        query = (NovelQuery.draft == draft)

    if query:
        return table.search(query)
    return table.all()