function solution(s) {
  const stack = [];
  const temp = Array.from(s);
  temp.forEach((value) => {
    if (value === stack.at(-1)) {
      stack.pop();
    } else {
      stack.push(value);
    }
  });

  if (stack.length > 0) {
    return 0;
  }
  return 1;
}
