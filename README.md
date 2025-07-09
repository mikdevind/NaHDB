
# NaHDB

NaHDB adalah solusi key-value database modern yang 💨 ringan, ⚡ cepat, dan 🔒 aman dengan dukungan enkripsi AES-256. Dirancang untuk developer 🐍 Python, 🟦 Node.js, dan 🐘 PHP, NaHDB memudahkan Anda menyimpan data dengan tingkat keamanan tinggi tanpa harus bergantung pada sistem database yang kompleks.

## ☕ Dukung Pengembangan

Jika Anda merasa terbantu dengan proyek ini, Anda bisa mendukung pengembangan lebih lanjut dengan berdonasi melalui:

### 💳 Bank Transfer
- **🏦 Bank Jago**  
  **No. Rekening:** `105361441776`  
  **Atas Nama:** *ILMAN HENDRAWAN SAPUTRA*  

### 🌐 Cryptocurrency
- **🪙 Litecoin (LTC):** `MSdWrJR8eHZEF9PFBKzyiSXcvAsTdrsg3D`
- **₿ Bitcoin (BTC):** `3LDgRxf5sAky8ejJJE7tR4L6uvJzmwoH4k`
- **💵 Bitcoin Cash (BCH):** `bitcoincash:qrrqattarsej5m3v05rtgfulcqqlxy840yls0rh56w`


## 📦 Instalasi

### 🐍 Python
Salin file `NaHDB.cp312-win_amd64.pyd` ke dalam proyek Anda. atau
```bash
pip install NaHDB
```

### 🟦 Node.js
Salin file `NaHDB.js` ke dalam proyek Anda. atau
```bash
npm install nahdb
```

### 🐘 PHP
Salin file `NaHDB.php` ke dalam proyek Anda.

---

## 🚀 Contoh Kode Penggunaan

### Inisialisasi

#### 🐍 Python

**Liblary yang di butuhkan:**
- pycryptodome
```python
from NaHDB import NaHDB

db = NaHDB('databasePath', b'key')
```

### 🟦 Node.js
tambahkan "type": "module" kedalam package.json
```json
{
  "name": "nahdb",
  "version": "1.0.0",
  "type": "module",
  "description": "NaHDB adalah solusi key-value database modern yang  ringan,  cepat, dan  aman dengan dukungan enkripsi AES-256.",
  "main": "app.js",
  "scripts": {
    "test": "node app.js"
  },
  "author": "Ilman Hendrawan Saputra",
  "license": "ISC"
}
```
```javascript
import { NaHDB } from './NaHDB.js';

const db = new NaHDB('databasePath', Buffer.from('key', 'utf-8'));
await db.init();
```

### 🐘 PHP
```php
require_once "NaHDB.php";

$db = new NaHDB(__DIR__ . "/databasePath", "key");
```
### Login
Default password root adalah '' dan mengembalikan boolean.

#### 🐍 Python
```python
db.login("root", "")
```

### 🟦 Node.js
```javascript
(async () => {
    await db.login('root', '');
})()
```

### 🐘 PHP
```php
$db->login("root", "")
```

### Create Table

#### 🐍 Python
```python
# Create Table
db.create_table("table",{"nameColom" : {"type": "str", "default": ""}})

# Wait for the process to complete
db.wait_until_done()

# Get List Table
listTable = db.list_table()
print(listTable)
```

### 🟦 Node.js
```javascript
(async () => {
    // Create Table
    await db.createTable("table",{"nameColom" : {"type": "str", "default": ""}});

    // Get List Table
    let listTable = db.listTable();
    console.log(listTable);
})()
```

### 🐘 PHP
```php
// Create Table
$db->create_table("table",["nameColom" => ["type" => "str", "default" => ""]]);

// Get List Table
$listTable = $db->list_table();
print_r($listTable);
```

### Update Table

#### 🐍 Python
```python
# Update Table
db.update_table("table",{"nameColom" : {"type": "str", "default": ""},"nameColom2" : {"type": "str", "default": ""}})

# Wait for the process to complete
db.wait_until_done()

# Get Schema Table
schemaTable = db.get_schema("table")
print(schemaTable)
```

### 🟦 Node.js
```javascript
(async () => {
    // Update Table
    await db.updateTable("table",{"nameColom" : {"type": "str", "default": ""},"nameColom2" : {"type": "str", "default": ""}});

    // Get Schema Table
    let schemaTable = db.getSchema("table");
    console.log(schemaTable);
})()
```

### 🐘 PHP
```php
// Update Table
$db->update_table("table",["nameColom" => ["type" => "str", "default" => ""],"nameColom2" => ["type" => "str", "default" => ""]]);

// Get Schema Table
$schemaTable = $db->get_schema("table");
print_r($schemaTable);

```

### Delete Table

#### 🐍 Python
```python
# Delete Table
db.delete_table("table")
```

### 🟦 Node.js
```javascript
(async () => {
    // Delete Table
    await db.deleteTable("table");
})()
```

### 🐘 PHP
```php
//Delete Table
$db->delete_table("table");
```

### Add Data

#### 🐍 Python
```python
# Add Data
db.create("table", {"nameColom":"value"})
```

### 🟦 Node.js
```javascript
(async () => {
    // Add Data
    await db.create("table", {"nameColom":"value"});
})()
```

### 🐘 PHP
```php
// add Data
$db->create("table",["nameColom" => "value"]);
```

### Update Data

#### 🐍 Python
```python
# Update Data
db.update("table", {"nameColom":"value"}, {"nameColom":"valueUpdate"})
```

### 🟦 Node.js
```javascript
(async () => {
    // Update Data
    await db.update("table", {"nameColom":"value"}, {"nameColom":"valueUpdate"});
})()
```

### 🐘 PHP
```php
// Update Data
$db->update("table",["nameColom" => "value"],["nameColom" => "valueUpdate"]);
```

### Delete Data

#### 🐍 Python
```python
# Remove Data
db.delete("table", {"nameColom":"valueUpdate"})
```

### 🟦 Node.js
```javascript
(async () => {
    // Delete Data
    db.delete("table", {"nameColom":"valueUpdate"});
})()
```

### 🐘 PHP
```php
// Delete Data
$db->delete("table",["nameColom" => "valueUpdate"]);
```

### Join Table

#### 🐍 Python
```python
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
```

### 🟦 Node.js
```javascript
(async () => {
    // Create Table Users
    await db.createTable("users", {
        "user_id": {"type": "int", "default": 0},
        "name": {"type": "str", "default": ""},
        "email": {"type": "str", "default": ""}
    })

    // Add Data Users
    await db.create("users", {"user_id": 1, "name": "Alice", "email": "alice@example.com"})
    await db.create("users", {"user_id": 2, "name": "Bob", "email": "bob@example.com"})
    await db.create("users", {"user_id": 3, "name": "Charlie", "email": "charlie@example.com"})

    // Create Table Orders
    await db.createTable("orders", {
        "order_id": {"type": "int", "default": 0},
        "user_id": {"type": "int", "default": 0},
        "order_date": {"type": "str", "default": ""}
    })

    // Add Data Orders
    await db.create("orders", {"order_id": 101, "user_id": 1, "order_date": "2025-07-08"})
    await db.create("orders", {"order_id": 102, "user_id": 2, "order_date": "2025-07-09"})
    await db.create("orders", {"order_id": 103, "user_id": 1, "order_date": "2025-07-10"})

    // Create Table Products
    await db.createTable("products", {
        "product_id": {"type": "int", "default": 0},
        "order_id": {"type": "int", "default": 0},
        "product_name": {"type": "str", "default": ""},
        "price": {"type": "float", "default": 0.0}
    })

    // Add Data Products
    await db.create("products", {"product_id": 1001, "order_id": 101, "product_name": "Laptop", "price": 1200.0})
    await db.create("products", {"product_id": 1002, "order_id": 101, "product_name": "Mouse", "price": 25.0})
    await db.create("products", {"product_id": 1003, "order_id": 102, "product_name": "Keyboard", "price": 45.0})
    await db.create("products", {"product_id": 1004, "order_id": 103, "product_name": "Monitor", "price": 300.0})

    // Get Data Join Table Singgle Kolom
    data = db.join("orders", "user_id", [{"table": "users", "on": "user_id", "as": "user"}])
    console.log(data)

    // Get Data Join Table Multiple Colomn
    data = db.joinField([
        { "table": "users"},
        {"table": "orders","on": "user_id","where": {"table": "users", "on": "user_id"},"as": "orders"},
        {"table": "products","on": "order_id","where": {"table": "orders", "on": "order_id"},"as": "products"}
    ])
    console.log(data)
})()
```

### 🐘 PHP
```php
// Create Table Users
$db->create_table("users", [
    "user_id" => ["type" => "int", "default" => 0],
    "name" => ["type" => "str", "default" => ""],
    "email" => ["type" => "str", "default" => ""]
]);

// Add Data Users
$db->create("users", ["user_id" => 1, "name" => "Alice", "email" => "alice@example.com"]);
$db->create("users", ["user_id" => 2, "name" => "Bob", "email" => "bob@example.com"]);
$db->create("users", ["user_id" => 3, "name" => "Charlie", "email" => "charlie@example.com"]);

// Create Table Orders
$db->create_table("orders", [
    "order_id" => ["type" => "int", "default" => 0],
    "user_id" => ["type" => "int", "default" => 0],
    "order_date" => ["type" => "str", "default" => ""]
]);

// Add Data Orders
$db->create("orders", ["order_id" => 101, "user_id" => 1, "order_date" => "2025-07-08"]);
$db->create("orders", ["order_id" => 102, "user_id" => 2, "order_date" => "2025-07-09"]);
$db->create("orders", ["order_id" => 103, "user_id" => 1, "order_date" => "2025-07-10"]);

// Create Table Products
$db->create_table("products", [
    "product_id" => ["type" => "int", "default" => 0],
    "order_id" => ["type" => "int", "default" => 0],
    "product_name" => ["type" => "str", "default" => ""],
    "price" => ["type" => "float", "default" => 0.0]
]);

// Add Data Products
$db->create("products", ["product_id" => 1001, "order_id" => 101, "product_name" => "Laptop", "price" => 1200.0]);
$db->create("products", ["product_id" => 1002, "order_id" => 101, "product_name" => "Mouse", "price" => 25.0]);
$db->create("products", ["product_id" => 1003, "order_id" => 102, "product_name" => "Keyboard", "price" => 45.0]);
$db->create("products", ["product_id" => 1004, "order_id" => 103, "product_name" => "Monitor", "price" => 300.0]);

// Get Data Join Table Singgle Kolom
$data = $db->join("orders", "user_id", [["table" => "users", "on" => "user_id", "as" => "user"]]);
print_r($data);

// Get Data Join Table Multiple Colomn
$data = $db->join_field([
    [ "table" => "users"],
    ["table" => "orders","on" => "user_id","where" => ["table" => "users", "on" => "user_id"],"as" => "orders"],
    ["table" => "products","on" => "order_id","where" => ["table" => "orders", "on" => "order_id"],"as" => "products"]
]);
print_r($data);
```

### Flush Table

#### 🐍 Python
```python
# Fulsh Table
db.flush_table("users")
```

### 🟦 Node.js
```javascript
(async () => {
    // Flush Table
    await db.flushTable("users")
})()
```

### 🐘 PHP
```php
// Flush Table
$db->flush_table("users");
```

### Add User

**Permision**:
1. `__user__` :
    - `get_users`
    - `get_user_id_by_username`
    - `add_user`
    - `update_permission`
    - `forget_password`
    - `change_password`
    - `get_username_by_id`
    - `get_user_by_id`
    - `update_username`
2. `table` :
    - `select`
    - `create`
    - `update`
    - `delete`
    - `flush`
    - `get_schema`
    - `list`
    - `update_table`
    - `delete_table`
    - `create_table`

#### 🐍 Python
```python
# Add User
db.add_user("username","password", "role",{ "users": ['select', 'create'] })

# Wait for the process to complete
db.wait_until_done()

# Get Users
users = db.get_users()
print(users)
```

### 🟦 Node.js
```javascript
(async () => {
    // Add Users
    await db.addUser("username","password", "role" , { users: ['select', 'create'] })

    // Get Users
    let users = db.getUsers()
    console.log(users)
})()
```

### 🐘 PHP
```php
// Add Users
$db->add_user("username","password", "role",[ "users" => ['select', 'create'] ]);

// Get Users
$users = $db->get_users();
print_r($users);
```

### Forget Password

#### 🐍 Python
```python
# Forget Password
db.forget_password("username","passwordNew")
```

### 🟦 Node.js
```javascript
(async () => {
    // Forget Password
    await db.forgetPassword("username","passwordNew")
})()
```

### 🐘 PHP
```php
// Forget Password
$db->forget_password("username","passwordNew");
```

### Update Username

#### 🐍 Python
```python
# Get ID by Username
idUser = db.get_user_id_by_username("username")

# Update Username
db.update_username("usernameNew",idUser)

# Wait for the process to complete
db.wait_until_done()
```

### 🟦 Node.js
```javascript
(async () => {
    // Get ID by Username
    let idUser = await db.getUserIdByUsername('username')

    // Update Username
    await db.updateUsername('usernameNew', idUser)
})()
```

### 🐘 PHP
```php
// Get ID by Username
$idUser = $db->get_user_id_by_username("username");

// Update Username
$db->update_username("usernameNew",$idUser);
```

### Forget Password

#### 🐍 Python
```python
# Forget Password
db.forget_password("username","passwordNew")
```

### 🟦 Node.js
```javascript
(async () => {
    // Forget Password
    await db.forgetPassword("username","passwordNew")
})()
```

### 🐘 PHP
```php
// Forget Password
$db->forget_password("username","passwordNew");
```

### Update Password

#### 🐍 Python
```python
# Update Password
db.change_password("passwordNew",idUser)

# Wait for the process to complete
db.wait_until_done()
```

### 🟦 Node.js
```javascript
(async () => {
    // Update Password
    await db.changePassword("passwordNew",idUser)
})()
```

### 🐘 PHP
```php
// Update Password
$db->change_password("passwordNew", $idUser);
```

### Update Permision

#### 🐍 Python
```python
# Get Username by ID
username = db.get_username_by_id(idUser)

# Update Permision User
db.update_permission(username, {"users":["select","create","update","delete"]})

# Wait for the process to complete
db.wait_until_done()

# Get Users
users = db.get_users()
print(users)
```

### 🟦 Node.js
```javascript
(async () => {
    // Get Username by ID
    let username = db.getUsernameById(idUser)

    // Update Permision User
    await db.updatePermission(username, {"users":["select","create","update","delete"]})

    // Get Users
    users = db.getUsers()
    console.log(users)
})()
```

### 🐘 PHP
```php
// Get Username by ID
$username = $db->get_username_by_id($idUser);

// Update Permision User
$db->update_permission($username, ["users" => ["select","create","update","delete"]]);

// Get Users
$users = $db->get_users();
print_r($users);
```

### Check Login

#### 🐍 Python
```python
# Check Login
islogin = db.is_login()
print(islogin)
```

### 🟦 Node.js
```javascript
(async () => {
    // Check Login
    let isLogin = db.isLogin()
    console.log(isLogin)
})()
```

### 🐘 PHP
```php
// Check Login
$isLogin = $db->is_login();
print_r($isLogin);
```

### Get User by ID

#### 🐍 Python
```python
# Get User by ID
user = db.get_user_by_id(idUser)
print(user)
```

### 🟦 Node.js
```javascript
(async () => {
    // Get User by ID
    let user = db.getUserById(idUser)
    console.log(user)
})()
```

### 🐘 PHP
```php
// Get User by ID
$user = $db->get_user_by_id($idUser);
print_r($user);
```
---

## 🔒 Fitur
- AES-256 Encryption untuk semua data.
- Cepat & ringan tanpa dependensi eksternal.
- Lintas platform: Python, Node.js, PHP.
- Penyimpanan berbasis file.


## 📜 Lisensi
MIT License.

## ☕ Dukung Pengembangan

Jika Anda merasa terbantu dengan proyek ini, Anda bisa mendukung pengembangan lebih lanjut dengan berdonasi melalui:

### 💳 Bank Transfer
- **🏦 Bank Jago**  
  **No. Rekening:** `105361441776`  
  **Atas Nama:** *ILMAN HENDRAWAN SAPUTRA*  

### 🌐 Cryptocurrency
- **🪙 Litecoin (LTC):** `MSdWrJR8eHZEF9PFBKzyiSXcvAsTdrsg3D`
- **₿ Bitcoin (BTC):** `3LDgRxf5sAky8ejJJE7tR4L6uvJzmwoH4k`
- **💵 Bitcoin Cash (BCH):** `bitcoincash:qrrqattarsej5m3v05rtgfulcqqlxy840yls0rh56w`

🙏 Terima kasih atas dukungan Anda!
