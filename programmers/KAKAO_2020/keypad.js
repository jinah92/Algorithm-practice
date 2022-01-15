const LEFT_SIDE = [1, 4, 7, '*']
const MIDDLE_SIDE = [2, 5, 8, 0]
const RIGHT_SIDE = [3, 6, 9, '#']

function solution(numbers, hand) {

  let answer = '';
  let current = {'L': '*', 'R': '#'};

  numbers.forEach(number => {
    if (LEFT_SIDE.includes(number)) {
      answer += 'L';
      current.L = number;
    } else if (RIGHT_SIDE.includes(number)) {
      answer += 'R';
      current.R = number;
    } else {
      let distanceFromLeft = getDistance(MIDDLE_SIDE.indexOf(number), LEFT_SIDE.indexOf(current.L), MIDDLE_SIDE.indexOf(current.L))
      let distanceFromRight = getDistance(MIDDLE_SIDE.indexOf(number), RIGHT_SIDE.indexOf(current.R), MIDDLE_SIDE.indexOf(current.R))
      
      if (distanceFromLeft < distanceFromRight) {
        answer += 'L';
        current.L = number
      } else if (distanceFromLeft > distanceFromRight) {
        answer += 'R';
        current.R = number
      } else {
        // 값이 같음
        if (hand === "left") {
          answer += 'L';
          current.L = number
        } else {
          answer += 'R';
          current.R = number
        }
      }
    }
  })
  return answer
}

function getDistance(midleIdx, currIdx, currIdxBasedMiddle) {
  return currIdx === -1 ? Math.abs(midleIdx - currIdxBasedMiddle) : Math.abs(midleIdx - currIdx) + 1
}

