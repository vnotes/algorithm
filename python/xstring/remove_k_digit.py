def removeKdigits(num: str, k: int) -> str:
    if not num or k >= len(num):
        return '0'
    if k <= 0:
        return num
    stack = [num[0]]
    for i in range(1, len(num)):
        while k > 0 and stack and stack[-1] > num[i]:
            stack.pop()
            k -= 1
        stack.append(num[i])
    if k > 0:
        stack = stack[:-k]
    while stack and stack[0] == '0':
        stack.pop(0)
        if stack and stack[0] != '0':
            break
    return ''.join(stack) or '0'


if __name__ == '__main__':
    removeKdigits("1432219", 3)
