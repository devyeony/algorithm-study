// Maximum Number of Words Found in Sentences

// A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
// You are given an array of strings sentences, where each sentences[i] represents a single sentence.
// Return the maximum number of words that appear in a single sentence.

const mostWordsFound = (sentences) => {
  let result = 0;

  sentences.forEach((sentence) =>
    result < sentence.split(' ').length
      ? (result = sentence.split(' ').length)
      : null,
  );

  return result;
};
