from tinydb import TinyDB
import json

if __name__ == '__main__':
    db = TinyDB('db.json')
    schemas = []
    with open('schemas.json', 'r') as file:
        schemas = json.load(file)
    
    for schema in schemas:
        db.insert(schema)