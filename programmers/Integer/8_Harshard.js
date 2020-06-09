function solution(x) {
  let divisor = 0;
  let number = x.toString();
  for (let i = 0; i < number.length; i++) {
    divisor += Number(number[i]);
  }
  return x % divisor === 0 ? true : false;
}
