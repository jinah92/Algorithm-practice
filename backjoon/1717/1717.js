const path = require("path");
const fs = require("fs");

const filePath =
  process.platform === "linux"
    ? "/dev/stdin"
    : path.join(__dirname, "input.txt");

let input = fs.readFileSync(filePath).toString().split("\n");

const [n, m] = input[0].split(" ").map((e) => Number(e));

let parents = [];
for (let i = 0; i < n + 1; i++) {
  parents[i] = i;
}

for (let i = 1; i < m + 1; i++) {
  const [check, p1, p2] = input[i].split(" ").map((e) => Number(e));

  if (check) {
    if (FindParent(p1) === FindParent(p2)) {
      console.log("YES");
    } else {
      console.log("NO");
    }
  } else {
    let parent1 = FindParent(p1);
    let parent2 = FindParent(p2);
    if (parent1 !== parent2) {
      parents[parent1] = parent2;
    }
  }
}

function FindParent(x) {
  if (x === parents[x]) return x;

  let p = FindParent(parents[x]);
  parents[p] = p;
  return p;
}
