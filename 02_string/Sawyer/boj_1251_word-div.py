import sys
from collections import deque

input = sys.stdin.readline

result = []

word = str(input().strip())

word_len = len(word)

for i in range(word_len):
    for j in range(i,word_len):
        one_word = word[:i][::-1]
        two_word = word[i:j][::-1]
        three_word = word[j:][::-1]
        if len(one_word) != 0 and len(two_word) != 0 and len(three_word) != 0 :
            new_word = one_word + two_word + three_word
            result.append(new_word)

result.sort()


print(result[0])