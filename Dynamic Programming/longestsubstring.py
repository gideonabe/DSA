def longest_common_substring(a, b):
  m, n = len(a), len(b)
  dp = [[0]*(n+1) for _ in range(m+1)]
  max_len, end = 0, 0
  for i in range(m):
    for j in range(n):
      if a[i] == b[j]:
        dp[i+1][j+1] = dp[i][j] + 1
        if dp[i+1][j+1] > max_len:
          max_len = dp[i+1][j+1]
          end = i + 1
  # extracts (slice) the substring from index end - max to end(exclusive)
  return max_len, a[end - max_len:end]


def longest_common_subsequence(a, b):
  m, n = len(a), len(b)
  dp = [[0]*(n+1) for _ in range(m+1)]
  for i in range(m):
    for j in range(n):
      if a[i] == b[j]:
        dp[i+1][j+1] = dp[i][j] + 1
      else:
        dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
  # Backtrack
  i, j = m, n
  lcs = []
  while i > 0 and j > 0:
    if a[i-1] == b[j-1]:
      lcs.append(a[i-1])
      i -= 1
      j -= 1
    elif dp[i-1][j] >= dp[i][j-1]:
      i -= 1
    else:
      j -= 1
  return dp[m][n], ''.join(reversed(lcs))


# Test input
a, b = "BLUES", "CLUES"

# Run both
sub_len, substring = longest_common_substring(a, b)
seq_len, subsequence = longest_common_subsequence(a, b)

# Output
print(f"Substring: {substring} (Length: {sub_len})")
print(f"Subsequence: {subsequence} (Length: {seq_len})")
