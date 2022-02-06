var isValid = function (s) {
  let queue = [];
  let hash = {
    "}": "{",
    ")": "(",
    "]": "[",
  };

  for (let i = 0; i < s.length; i++) {
    if (["(", "{", "["].indexOf(s[i]) !== -1) {
      queue.push(s[i]);
    } else {
      if (queue.slice(-1)[0] !== hash[s[i]]) {
        return false;
      }
      queue.pop();
    }
  }
  if (queue.length) return false;
  return true;
};
