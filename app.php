<?php
require_once "obfuscator/dist/NaHDB.php";

$db = new NaHDB(__DIR__ . "/databasePath", "Nbjhh6NfNSrz7UJ3ZpSkXFRTX1jxM9K618nrRVNx2gBpvj0NLF2yt14jEZmP");

if ($db->login("root", "")) {
	echo "Success login root";
} else {
	echo "Failed login root";
}

// Create Table
$db->create_table("table",["nameColom" => ["type" => "str", "default" => ""]]);

// Get List Table
$listTable = $db->list_table();
print_r($listTable);

// Update Table
$db->update_table("table",["nameColom" => ["type" => "str", "default" => ""],"nameColom2" => ["type" => "str", "default" => ""]]);

// Get Schema Table
$schemaTable = $db->get_schema("table");
print_r($schemaTable);

//Delete Table
$db->delete_table("table");

// Get List Table
$listTable = $db->list_table();
print_r($listTable);

// Create Table
$db->create_table("table",["nameColom" => ["type" => "str", "default" => ""]]);

// add Data
$db->create("table",["nameColom" => "value"]);

// Get Data
$data = $db->select("table");
print_r($data);

// Get Data With Where
$data = $db->select("table",["nameColom" => "value"]);
print_r($data);

// Update Data
$db->update("table",["nameColom" => "value"],["nameColom" => "valueUpdate"]);

// Get Data
$data = $db->select("table");
print_r($data);

// Delete Data
$db->delete("table",["nameColom" => "valueUpdate"]);

// Get Data
$data = $db->select("table");
print_r($data);

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

// Flush Table
$db->flush_table("users");

// Get Data
$data = $db->select("users");
print_r($data);

// Add Users
$db->add_user("username","password", "role",[ "users" => ['select', 'create'] ]);

// Get Users
$users = $db->get_users();
print_r($users);

// Forget Password
$db->forget_password("username","passwordNew1");

// Get Users
$users = $db->get_users();
print_r($users);

// Get ID by Username
$idUser = $db->get_user_id_by_username("username");

// Update Username
$db->update_username("usernameNew",$idUser);

// Get Users
$users = $db->get_users();
print_r($users);

// Update Password
$db->change_password("passwordNew", $idUser);

// Get Username by ID
$username = $db->get_username_by_id($idUser);

// Update Permision User
$db->update_permission($username, ["users" => ["select","create","update","delete"]]);

// Get Users
$users = $db->get_users();
print_r($users);

// Check Login
$isLogin = $db->is_login();
print_r($isLogin);

// Get User by ID
$user = $db->get_user_by_id($idUser);
print_r($user);
?>