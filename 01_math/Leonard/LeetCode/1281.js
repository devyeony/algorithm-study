// Subtract the Product and Sum of Digits of an Integer

// Given an integer number n, return the difference between the product of its digits and the sum of its digits.

const subtractProductAndSum = (n) => {
  const splitNumber = String(n).split('');

  const multiplyValue = splitNumber.reduce((a, b) => Number(a) * Number(b), 1);
  const plusValue = splitNumber.reduce((a, b) => Number(a) + Number(b), 0);

  return multiplyValue - plusValue;
};
