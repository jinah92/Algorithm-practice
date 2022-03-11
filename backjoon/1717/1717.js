const path = require("path");
const fs = require("fs");

const filePath =
  process.platform === "linux"
    ? "/dev/stdin"
    : path.join(__dirname, "input.txt");

let input = fs.readFileSync(filePath).toString().split("\n");

const [n, m] = input[0].split(" ").map((e) => Number(e));

let sets = [];
for (let i = 0; i < n + 1; i++) {
  sets[i] = [i];
}

for (let i = 1; i < m + 1; i++) {
  const [check, s1, s2] = input[i].split(" ").map((e) => Number(e));

  if (check) {
    console.log(
      sets.filter((i) => i.includes(s1) && i.includes(s2)).length ? "YES" : "NO"
    );
  } else {
    const filtered = sets
      .filter((i) => i.includes(s1) || i.includes(s2))
      .flat();
    const remains = sets.filter((i) => !(i.includes(s1) || i.includes(s2)));
    sets = [...remains, filtered];
  }
}
