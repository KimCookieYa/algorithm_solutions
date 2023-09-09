function solution(n, words) {
  let answer = [0, 0];
  const dict = {};
  let last_char = words[0][0];
  let idx = 0;
  for (word of words) {
    if (word in dict || last_char !== word[0]) {
      answer = [(idx % n) + 1, Math.floor(idx / n) + 1];
      break;
    } else {
      dict[word] = 1;
    }
    last_char = word.at(-1);
    idx++;
  }

  return answer;
}
