const NUMBERS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];

function solution(s) {
  let answer = s;

  NUMBERS.forEach(
    (number) => (answer = answer.replace(new RegExp(`${number}`, 'gi'),toNumber(number))))

  return Number(answer);
}

function toNumber(val) {
  switch (val) {
    case "zero":
      return "0";
    case "one":
      return "1";
    case "two":
      return "2";
    case "three":
      return "3";
    case "four":
      return "4";
    case "five":
      return "5";
    case "six":
      return "6";
    case "seven":
      return "7";
    case "eight":
      return "8";
    case "nine":
      return "9";
  }
}

solution("one4seveneight")