const balancedStringSplit = (s) => {
  let array = s.split('');
  let currentTerm = array.shift();
  let countSameWord = 1;
  let isNewTerm = false;
  let result = 0;

  while (array.length) {
    if (currentTerm === array[0] || isNewTerm) {
      isNewTerm = false;
      countSameWord++;
      array.shift();
    } else {
      countSameWord--;

      if (countSameWord === 0) {
        isNewTerm = true;
        currentTerm = array[1];
        result++;
      }

      array.shift();
    }
  }

  return result;
};
