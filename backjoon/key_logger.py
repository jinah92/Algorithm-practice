test_case = int(input())

for _ in range(test_case):
    string = list(map(str, input()))
    left_stack, right_stack = list(), list()
    cur = 0

    for text in string:
        if text == '<':
            if len(left_stack) > 0:
                right_stack.append(left_stack.pop())
            else:
                continue
        elif text == '>':
            if len(right_stack) > 0:
                left_stack.append(right_stack.pop())
            else:
                continue
        elif text == '-':
            if len(left_stack) > 0:
                left_stack.pop()
            else:
                continue
        else:
            left_stack.append(text)
    left_stack.extend(reversed(right_stack))
    print(''.join(left_stack))