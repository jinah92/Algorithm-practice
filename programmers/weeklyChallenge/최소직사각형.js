function solution(sizes) {
    let maxSize = [0, 0]; // 명함의 최대 크기
    let rowArr = [], colArr = [];
    
    sizes.map((size, key) => {
        rowArr.push(size[0]);
        colArr.push(size[1]);
        
        maxSize[0] = Math.min(...maxSize) < Math.min(...size) ? Math.min(...size) :  Math.min(...maxSize);
        maxSize[1] = Math.max(...maxSize) < Math.max(...size) ? Math.max(...size) :  Math.max(...maxSize);
    })
    
    /* 최대 크기가 특정 지갑의 크기인 경우 */
    if (findIndexOfArray(sizes, maxSize) !== -1 || findIndexOfArray(sizes, maxSize.reverse()) !== -1){
        return maxSize.reduce((accum, item) => {
            return accum * item
        })
    }
    
    const maxRow = Math.max(...rowArr);
    const maxCol = Math.max(...colArr);

    const swapIndexRow = swapRowCol(sizes, maxRow);
    const swapIndexCol = swapRowCol(sizes, maxCol);
    
    /* 최대 가로길이 * 최대 세로길이 비교 */
    const case2 = getMaxSize(swapItems(sizes, swapIndexRow));
    const case3 = getMaxSize(swapItems(sizes, swapIndexCol));

    return Math.min(maxRow * maxCol, Math.max(...case2.rowArr) * Math.max(...case2.colArr), Math.max(...case3.rowArr) * Math.max(...case3.colArr));
}

function swapItems(items, swapIndex) {
    let deepCopyItems = JSON.parse(JSON.stringify(items));
    return deepCopyItems.map((item, key) => {
        if (key === swapIndex) {
            return [item[0], item[1]] = [item[1], item[0]];
        }
        return item;
    })
}

function swapRowCol(items, index) {
    return items.findIndex((item) => {
        if(item.indexOf(index) !== -1) return true});
}

function getMaxSize(items) {
    let rowArr = [], colArr = []
    items.map((size, key) => {
        rowArr.push(size[0]);
        colArr.push(size[1]);        
    })
    return {rowArr, colArr}
}

function findIndexOfArray(arr, maxSize) {
    arr.findIndex((item) => {
        return item === maxSize
    })
}

// const sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]];

// console.log(solution(sizes));