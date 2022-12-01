# %%
with open('input-day8.txt') as f:
    a = [[x.split()[0], int(x.split()[1])]
         for x in [line for line in f.read().splitlines()]]
    accumulator = 0
    visited = [False for _ in a]
# %%
    i = 0
    while (0 <= i < len(a)) and (not visited[i]):
        visited[i] = True
        operation, arg = a[i]
        if operation == 'acc':
            accumulator += arg
            i += 1
        elif operation == 'jmp':
            i += arg
        elif operation == 'nop':
            i += 1
    terminated = i == len(a)
    _, ans = terminated, accumulator
    print(ans)

# %%
