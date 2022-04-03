var solution = function (isBadVersion) {
  /**
   * @param {integer} n Total versions
   * @return {integer} The first bad version
   */
  return function (n) {
    let start = 1,
      end = n;
    let middle = 0;
    while (start <= end) {
      middle = parseInt((start + end) / 2);
      if (isBadVersion(middle)) {
        end = middle - 1;
      } else {
        start = middle + 1;
      }
    }
    return start;
  };
};
