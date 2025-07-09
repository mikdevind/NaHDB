from NaHDB import NaHDB

db = NaHDB('databasePath', b'Nbjhh6NfNSrz7UJ3ZpSkXFRTX1jxM9K618nrRVNx2gBpvj0NLF2yt14jEZmP')

if db.login("root", ""):
	print("Success login root")
else:
	print("Failed login root")

# Create Table
db.create_table("table",[{"nameColom" : {"type": "str", "default": ""}}])

# Tunggu Proses Sampai Selesai
db.wait_until_done()

# Get List Table
listTable = db.list_table()
print(listTable)

# Update Table
db.update_table("table",{"nameColom" : {"type": "str", "default": ""},"nameColom2" : {"type": "str", "default": ""}})

# Wait for the process to complete
db.wait_until_done()

# Get Schema Table
schemaTable = db.get_schema("table")
print(schemaTable)

# Delete Table
db.delete_table("table")

# Wait for the process to complete
db.wait_until_done()

# Show List Table
listTable = db.list_table()
print(listTable)

# Create Table
db.create_table("table",{"nameColom" : {"type": "str", "default": ""}})

# Wait for the process to complete
db.wait_until_done()

# Add Data
db.create("table", {"nameColom":"value"})

# Wait for the process to complete
db.wait_until_done()

# Get Data
data = db.select("table")
print(data)

# Get Data With Where
data = db.select("table", {"nameColom":"value"})
print(data)

# Update Data
db.update("table", {"nameColom":"value"}, {"nameColom":"valueUpdate"})

# Wait for the process to complete
db.wait_until_done()

# Get Data
data = db.select("table")
print(data)

# Remove Data
db.delete("table", {"nameColom":"valueUpdate"})

# Wait for the process to complete
db.wait_until_done()

# Get Data
data = db.select("table")
print(data)

# Create Table Users
db.create_table("users", {
    "user_id": {"type": "int", "default": 0},
    "name": {"type": "str", "default": ""},
    "email": {"type": "str", "default": ""}
})

# Wait for the process to complete
db.wait_until_done()

# Add Data Users
db.create("users", {"user_id": 1, "name": "Alice", "email": "alice@example.com"})
db.create("users", {"user_id": 2, "name": "Bob", "email": "bob@example.com"})
db.create("users", {"user_id": 3, "name": "Charlie", "email": "charlie@example.com"})

# Wait for the process to complete
db.wait_until_done()

# Create Table Orders
db.create_table("orders", {
    "order_id": {"type": "int", "default": 0},
    "user_id": {"type": "int", "default": 0},
    "order_date": {"type": "str", "default": ""}
})

# Wait for the process to complete
db.wait_until_done()

# Add Data Orders
db.create("orders", {"order_id": 101, "user_id": 1, "order_date": "2025-07-08"})
db.create("orders", {"order_id": 102, "user_id": 2, "order_date": "2025-07-09"})
db.create("orders", {"order_id": 103, "user_id": 1, "order_date": "2025-07-10"})

# Wait for the process to complete
db.wait_until_done()

# Create Table Products
db.create_table("products", {
    "product_id": {"type": "int", "default": 0},
    "order_id": {"type": "int", "default": 0},
    "product_name": {"type": "str", "default": ""},
    "price": {"type": "float", "default": 0.0}
})

# Wait for the process to complete
db.wait_until_done()

# Add Data Products
db.create("products", {"product_id": 1001, "order_id": 101, "product_name": "Laptop", "price": 1200.0})
db.create("products", {"product_id": 1002, "order_id": 101, "product_name": "Mouse", "price": 25.0})
db.create("products", {"product_id": 1003, "order_id": 102, "product_name": "Keyboard", "price": 45.0})
db.create("products", {"product_id": 1004, "order_id": 103, "product_name": "Monitor", "price": 300.0})

# Wait for the process to complete
db.wait_until_done()

# Get Data Join Table Singgle Kolom
data = db.join("orders", "user_id", [{"table": "users", "on": "user_id", "as": "user"}])
print(data)

# Get Data Join Table Multiple Colomn
data = db.join_field([
	{ "table": "users"},
	{"table": "orders","on": "user_id","where": {"table": "users", "on": "user_id"},"as": "orders"},
	{"table": "products","on": "order_id","where": {"table": "orders", "on": "order_id"},"as": "products"}
])
print(data)

# Fulsh Table
db.flush_table("users")

# Wait for the process to complete
db.wait_until_done()

# Get Data
data = db.select("users")
print(data)

# Add User
db.add_user("username","password", "role",{ "users": ['select', 'create'] })

# Wait for the process to complete
db.wait_until_done()

# Get Users
users = db.get_users()
print(users)

# Forget Password
db.forget_password("username","passwordNew1")

# Wait for the process to complete
db.wait_until_done()

# Get Users
users = db.get_users()
print(users)

# Get ID by Username
idUser = db.get_user_id_by_username("username")

# Update Username
db.update_username("usernameNew",idUser)

# Wait for the process to complete
db.wait_until_done()

# Get Users
users = db.get_users()
print(users)

# Update Password
db.change_password("passwordNew",idUser)

# Wait for the process to complete
db.wait_until_done()

# Get Username by ID
username = db.get_username_by_id(idUser)

# Update Permision User
db.update_permission(username, {"users":["select","create","update","delete"]})

# Wait for the process to complete
db.wait_until_done()

# Get Users
users = db.get_users()
print(users)

# Check Login
islogin = db.is_login()
print(islogin)

# Get User by ID
user = db.get_user_by_id(idUser)
print(user)