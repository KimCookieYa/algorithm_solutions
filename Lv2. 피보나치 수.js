const dp = [0, 1];

function solution(n) {
  if (n in dp) {
    return dp[n];
  }
  for (let i = 2; i <= n; i++) {
    dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567;
  }
  return dp[n];
}
