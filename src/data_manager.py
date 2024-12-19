from tinydb import TinyDB, Query

def save_data(db, data, config):
    table = db.table(config['element_type'] )

    NovelQuery = Query()
    existing = table.get(
        (NovelQuery.draft == config['draft_number']) &
        (NovelQuery.element_name == config['element_name'])
    )
    
    if existing:
        print(f"Duplicate entry found: {existing}. Skipping save.")
        return
    
    table.insert({
        'element_name': config['element_name'],
        "draft": config['draft_number'],
        'data':data
    })
    print(f"Data saved under {config['element_type'] } > {config['element_name']}")

def load_data(db, config):
    """
    Loads data from the database based on the specified configuration.

    Args:
        db: The database object.
        config (dict): A dictionary containing the search criteria, e.g., 
                       {'element_type': 'table_name', 'draft_number': 1, 'element_name': 'name'}.

    Returns:
        dict or None: The retrieved data, or None if no matching entry is found.
    """
    table = db.table(config['element_type'])

    NovelQuery = Query()
    result = table.get(
        (NovelQuery.draft == config['draft_number']) & 
        (NovelQuery.element_name == config['element_name'])
    )

    if result:
        print(f"Data loaded for {config['element_type']} > {config['element_name']}.")
        return result['data']
    else:
        print(f"No data found for {config['element_type']} > {config['element_name']}.")
        return None