/*
    연습문제
    레벨 1
    행렬의 덧셈
*/

function solution(arr1, arr2) {
    let answer = []
    for (let a in arr1) {
        let tempArray = []
        for (let b in arr1[a]){
            // console.log(arr1[a][b])
            tempArray.push(arr1[a][b] + arr2[a][b])
        }
        answer.push(tempArray);
    }
  }

arr1 = [[1,2],[2,3]];
arr2 = [[3,4],[5,6]]; 

solution(arr1, arr2);