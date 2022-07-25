// Best Time to Buy and Sell Stock

const maxProfit = (prices) => {
  const minimumPrice = Math.min(...prices);
  const deletePointer = prices.indexOf(minimumPrice);
  prices.splice(0, deletePointer + 1);
  const maximumPrice = Math.max(...prices);

  return prices.length === 0 ? 0 : maximumPrice - minimumPrice;
};
