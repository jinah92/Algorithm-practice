function solution(a, b) {
    let result = 0;

    for (let i=0; i<a.length; i++) {
        result += (a[i] * b[i]);
    }
    return result;
}

solution([1,2,3,4], [-3,-1,0,2]); //  result : 3
solution([-1,0,1], [1,0,-1]); //  result : -2
