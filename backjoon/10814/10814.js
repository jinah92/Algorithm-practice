const path = require("path");
const fs = require("fs");

const filePath =
  process.platform === "linux"
    ? "/dev/stdin"
    : path.join(__dirname, "input.txt");

let input = fs.readFileSync(filePath).toString().split("\n");

const users = [];
for (let i = 1; i < Number(input[0]) + 1; i++) {
  const [age, name] = input[i].split(" ");

  users.push({ age, name });
}
users
  .sort((a, b) => a.age - b.age)
  .map((user) => console.log(user.age, user.name));
