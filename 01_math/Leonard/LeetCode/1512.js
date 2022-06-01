// Number of Good Pairs
// Given an array of integers nums, return the number of good pairs.

const numIdenticalPairs = (nums) => {
  let count = 0;

  nums.map((num, index) => {
    for (let i = index + 1; i < nums.length; i++) {
      if (num === nums[i]) count++;
    }
  });

  return count;
};
