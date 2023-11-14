from tinydb import TinyDB, Query

db = TinyDB('db.json')

test_data = {
    "first_name": "text",
    "last_name": "text",
    "personal_phone": "phone",
    "user": "text",
}

res = db.search(Query().fragment(test_data))
print(res)

