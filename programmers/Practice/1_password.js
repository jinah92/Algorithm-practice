/*
    연습문제
    레벨 1
    비밀번호 번호 가리기
*/

function solution(phone_number) {
    return phone_number.substr(-4, 4) + phone_number.substr(-4, 4);
}

const phone_number = "01033334444";

console.log(solution(phone_number))
