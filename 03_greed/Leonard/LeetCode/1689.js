const minPartitions = (n) => {
  return Math.max(...n.split('').map((num) => Number(num)));
};
