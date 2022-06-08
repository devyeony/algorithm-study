// Minimum Sum of Four Digit Number After Splitting Digits
// You are given a positive integer num consisting of exactly four digits. Split num into two new integers new1 and new2 by using the digits found in num. Leading zeros are allowed in new1 and new2, and all the digits found in num must be used.

const minimumSum = (num) => {
  const splitNumber = String(num)
    .split('')
    .sort((a, b) => a - b)
    .map((num) => num);

  return (
    Number(splitNumber[0] + splitNumber[2]) +
    Number(splitNumber[1] + splitNumber[3])
  );
};
