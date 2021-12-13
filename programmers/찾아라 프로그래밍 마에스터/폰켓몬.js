function solution(nums) {
    let selectMonster = nums.length / 2;

    // 폰켓몬 종류의 중복값 없애기
    const setNums = nums.filter((element, index) => {
        return nums.indexOf(element) === index;
    });

    // 중복제거된 폰켓몬 종류의 수와 최대 가져갈 수 있는 폰켓몬 수 비교 (작은 값을 리턴)
    return setNums.length >= selectMonster ? selectMonster : setNums.length;
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

let testCases = [[3,1,2,3], [3,3,3,2,2,4], [3,3,3,2,2,2]];

testCases.forEach(el => {
    console.log(solution(el))
})