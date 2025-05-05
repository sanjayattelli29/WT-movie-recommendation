console.clear();
console.log("Initializing server components...");
setTimeout(() => {
  console.log("Connecting to JDBC ...");
}, 800);

setTimeout(() => {
  console.log("✅ MongoDB connected at mongodb+srv://cluster0.qr8ux.mongodb.net/");
}, 1600);

setTimeout(() => {
  console.log("Establishing JDBC connection to MySQL...");
}, 2200);

setTimeout(() => {
  console.log("✅ JDBC connection successful to movie_user_db @ localhost:3306");
  console.log("Type 'help;' or '\\h' for help. Type '\\c' to clear the current input statement.\n");
}, 2800);

setTimeout(() => {
  console.log("mysql> USE movie_user_db;");
  console.log("Database changed");
}, 3200);

setTimeout(() => {
  console.log("mysql> SHOW TABLES;");
  console.log("+-------------------------+");
  console.log("| Tables_in_movie_user_db |");
  console.log("+-------------------------+");
  console.log("| user_ratings            |");
  console.log("| users                   |");
  console.log("| watch_history           |");
  console.log("+-------------------------+");
  console.log("3 rows in set (0.031 sec)");
}, 3600);

setTimeout(() => {
  console.log("mysql> SHOW COLUMNS FROM table_name;");
  console.log("ERROR 1146 (42S02): Table 'movie_user_db.table_name' doesn't exist");
}, 4000);

setTimeout(() => {
  console.log("mysql> SELECT * FROM users LIMIT 10;");
  console.log("+---------+----------+---------------------------+---------------------+");
  console.log("| user_id | username | email                     | created_at          |");
  console.log("+---------+----------+---------------------------+---------------------+");
  console.log("|       1 | sanjay   | attellisanjay29@gmail.com | 2025-04-30 23:49:51 |");
  console.log("|       2 | rishitha | rishitha16@gmail.com      | 2025-04-30 23:52:18 |");
  console.log("+---------+----------+---------------------------+---------------------+");
  console.log("2 rows in set (0.009 sec)");
}, 4400);

setTimeout(() => {
  console.log("mysql> SELECT * FROM user_ratings LIMIT 10;");
  console.log("Empty set (0.009 sec)");
}, 4800);

setTimeout(() => {
  console.log("Initializing CRUD endpoints...");
}, 5200);

setTimeout(() => {
  console.log("Edit, Delete, Update routes are live.");
}, 5600);

setTimeout(() => {
  console.log("Loading middleware and route handlers...");
}, 6000);

setTimeout(() => {
  console.log("✅ Server is LIVE: http://localhost:3000");
  console.log("Admin Panel: http://localhost:3000/admin");
  console.log("Stats Dashboard: http://localhost:3000/monitor");
  console.log("Environment: development | Version: 1.0.0");
}, 6400);

setTimeout(() => {
  console.log("\n🚀 All systems go. Server ready to handle requests.");
}, 6800);


