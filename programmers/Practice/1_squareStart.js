/*
    연습문제
    레벨 1
    직사각형 발찍기
*/

process.stdin.setEncoding('utf8');
process.stdin.on('data', data => {
    const [n, k] = data.split(" ");
    for (let i=0; i < k; i++) {
        console.log('*'.repeat(n));        
    }
});