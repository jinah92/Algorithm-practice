const bridge_length = 2;
const weight = 10;
const truck_weights = [7, 4, 5, 6];

solution(bridge_length, weight, truck_weights);

function solution(bridge_length, weight, truck_weights) {
  let answer = 0;
  let onBridge = [];
  let arrived = [];
  let totalWeight = 0;
  const count = truck_weights.length;

  let currentCount = 0;

  while (arrived.length !== count) {
    while (true) {
      answer += 1;
      // 다리를 건너는 트럭 선택하기
      if (totalWeight + truck_weights[0] <= weight) {
        const target = truck_weights.shift();
        onBridge.push(target);
        totalWeight += target;
      } else {
        break;
      }
    }

    const minWeight = truck_weights.length
      ? Math.min.apply(null, truck_weights)
      : weight;

    while (true) {
      if (weight - totalWeight < minWeight) {
        const out = onBridge.shift();
        arrived.push(out);
        // answer += 1;
        totalWeight -= out;
        // currentCount -= 1;
      } else {
        // back = true;
        break;
      }
    }
  }

  return answer;
}
