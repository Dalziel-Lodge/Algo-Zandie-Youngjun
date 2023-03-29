import sys

while True:
    sentence = sys.stdin.readline().rstrip('\n')
    if sentence == '.':
        break
    stack = []
    for i in sentence:
        if i in ['(', '[']:
            stack.append(i)
        elif i in [')', ']']:
            if not stack:
                sentence = "no"
                break
            if i == ')' and stack[-1] != '(':
                sentence = "no"
                break
            elif i == ']' and stack[-1] != '[':
                sentence = "no"
                break
            stack.pop()
        else:
            if not stack:
                sentence = "yes"
            else:
                sentence = "no"
    print(sentence)

