const twoSum = (nums, target) => {
  let result;

  nums.map((num, index) => {
    for (let i = index + 1; i < nums.length; i++) {
      if (target - num - nums[i] === 0) {
        result = [index, i];
      }
    }
  });

  return result;
};
