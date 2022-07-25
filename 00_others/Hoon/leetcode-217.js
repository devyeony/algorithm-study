// 217. Contains Duplicate
// https://leetcode.com/problems/contains-duplicate/

const containsDuplicate = (nums) => {
  const deleteDuplication = new Set(nums);

  return deleteDuplication.size !== nums.length;
};
