const maximum69Number = (num) => {
  let nums = String(num).split('');
  const firstSix = nums.indexOf('6');

  nums[firstSix] = '9';

  return Number(nums.join(''));
};
