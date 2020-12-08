# https://www.codingame.com/training/medium/stock-exchange-losses

hi, low, v_prev = 0, 2**31, None
max_drawdown = 0
n = int(input())
for i in input().split():
    v = int(i)
    if v_prev is not None and v_prev > v:  # drawdown
        hi = max(hi, v_prev)
        low = min(low, v)
        max_drawdown = min(low - hi, max_drawdown)
    else:  # reset the low
        low = 2**31
    v_prev = v

print(max_drawdown)
