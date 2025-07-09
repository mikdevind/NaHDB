import { NaHDB } from './NaHDB.js';

const db = new NaHDB('databasePath', Buffer.from('Nbjhh6NfNSrz7UJ3ZpSkXFRTX1jxM9K618nrRVNx2gBpvj0NLF2yt14jEZmP', 'utf-8'));
await db.init();
(async () => {
	// Login
	if (await db.login('root', '')) {
		console.log("Success login root");
	} else {
		console.log("Failed login root");
	}

	// Create Table
	await db.createTable("table",{"nameColom" : {"type": "str", "default": ""}});

	// Get List Table
	let listTable = db.listTable();
	console.log(listTable);

	// Update Table
	await db.updateTable("table",{"nameColom" : {"type": "str", "default": ""},"nameColom2" : {"type": "str", "default": ""}});

	// Get Schema Table
	let schemaTable = db.getSchema("table");
	console.log(schemaTable);

	// Delete Table
	await db.deleteTable("table");

	// Show List Table
	listTable = db.listTable();
	console.log(listTable);

	// Create Table
	await db.createTable("table",{"nameColom" : {"type": "str", "default": ""}});

	// Add Data
	await db.create("table", {"nameColom":"value"});

	// Get Data
	let data = db.select("table");
	console.log(data);

	// Get Data With Where
	data = db.select("table", {"nameColom":"value"});
	console.log(data);

	// Update Data
	await db.update("table", {"nameColom":"value"}, {"nameColom":"valueUpdate"});

	// Get Data
	data = db.select("table");
	console.log(data);

	// Delete Data
	db.delete("table", {"nameColom":"valueUpdate"});

	// Get Data
	data = db.select("table");
	console.log(data);

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

	// Flush Table
	await db.flushTable("users")

	// Get Data
	data = db.select("users");
	console.log(data);

	// Add Users
	await db.addUser("username","password", "role" , { users: ['select', 'create'] })

	// Get Users
	let users = db.getUsers()
	console.log(users)

	// Forget Password
	await db.forgetPassword("username","passwordNew1")

	// Get Users
	users = db.getUsers()
	console.log(users)

	// Get ID by Username
	let idUser = await db.getUserIdByUsername('username')

	// Update Username
	await db.updateUsername('usernameNew', idUser)

	// Get Users
	users = db.getUsers()
	console.log(users)

	// Update Password
	await db.changePassword("passwordNew",idUser)

	// Get Username by ID
	let username = db.getUsernameById(idUser)

	// Update Permision User
	await db.updatePermission(username, {"users":["select","create","update","delete"]})

	// Get Users
	users = db.getUsers()
	console.log(users)

	// Check Login
	let isLogin = db.isLogin()
	console.log(isLogin)

	// Get User by ID
	let user = db.getUserById(idUser)
	console.log(user)
})()