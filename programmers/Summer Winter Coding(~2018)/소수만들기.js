// 주어진 배열에서 3개의 수를 뽑아 소수를 만들 수 있는 경우의 수를 리턴
const reducer = (acc, num) => acc + num;

function solution(nums) {
    let totalCount = 0;
    const cases = getCombinations(nums, 3);

    cases.map((arr) => {
        if(isPrimeNumber(arr.reduce(reducer))) {
            totalCount += 1;
        }
    })

    return totalCount;
}

// 배열의 조합 구하기
function getCombinations(nums, selectNumber) {
    const results = [];
    if (selectNumber === 1) {
        return nums.map(el => [el]);
    }
    
    nums.forEach((fixed, index, array) => {
        const restArray = array.slice(index+1); // fixed를 제외한 나머지 배열
        const combinations = getCombinations(restArray, selectNumber-1);
        const attachedArray = combinations.map(el => [fixed, ...el]);

        results.push(...attachedArray);
    });

    return results;
} 

// 소수 판단
function isPrimeNumber(num) {
    if (num === 2) return true;
    
    // 제곱근까지만 검사
    for (let i=2; i <= Math.sqrt(num); i++) {
        if (num%i === 0) return false;
    }
    return true;
}

solution([1,2,3,4])
solution([1,2,7,6,4])