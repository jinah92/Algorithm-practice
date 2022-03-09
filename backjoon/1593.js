/* 문자해독 */
const W = "cAda";
const S = "AbrAcadAbRa";

const W_LEN = W.length;

let answer = 0;

let w_list = Array.from({ length: 58 }, () => 0);
let s_list = Array.from({ length: 58 }, () => 0);

for (let w of W) {
  w_list[w.charCodeAt(w) - 65] += 1;
}

let start = 0,
  S_LEN = 0;

for (let s of S) {
  console.log(s, s.charCodeAt(s) - 65);
  s_list[s.charCodeAt(s) - 65] += 1;
  S_LEN += 1;

  if (S_LEN === W_LEN) {
    console.clear();
    console.log("s :: ", s_list);
    console.log("w :: ", w_list);
    if (JSON.stringify(w_list) === JSON.stringify(s_list)) {
      answer += 1;
    }
    s_list[S.charCodeAt(start) - 65] -= 1;
    start += 1;
    S_LEN -= 1;
    console.log(s_list, start, S_LEN);
  }
}
