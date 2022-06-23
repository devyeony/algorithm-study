const minPairSum = (nums) => {
  let arr = nums.sort((a, b) => a - b);
  let result = [];

  while (arr.length) {
    result.push(arr.shift() + arr.pop());
  }

  return Math.max(...result);
};
