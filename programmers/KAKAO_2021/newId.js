function solution(new_id) {
  let answer = "";
  answer = new_id.toLowerCase();
  answer = answer.match(/[\w\-\_\.]/g).join("");
  answer = answer.replace(/\.{1,}/g, ".");
  answer = answer.replace(/^\./, "");
  answer = answer.replace(/\.$/, "");

  if (answer === "") answer = "a";
  if (answer.length > 15) {
    answer = answer.slice(0, 15);
    answer = answer.replace(/\.$/, "");
  }
  while (answer.length < 3) {
    answer += answer[answer.length - 1];
  }
  return answer;
}
