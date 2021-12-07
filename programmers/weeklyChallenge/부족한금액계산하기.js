function solution(price, money, count) {
    let i = 0;
    let total_pirce = 0;
    while (i < 4) {
        total_pirce += price * (i+1);
        i = i + 1;
    }

    return total_pirce > money ? total_pirce - money : 0;
}

solution(3, 20, 4)