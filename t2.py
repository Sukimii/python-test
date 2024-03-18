import sys

def main():
    for line in sys.stdin:
        str = line.strip()
        res = ""
        stack = []
        for i in range(len(str)):
            if str[i] != '(' and str[i] != ')':
                res += " "
            elif str[i] == '(':
                stack.append(('(', i))
                res += "x"
            elif str[i] == ')':
                if len(stack) == 0 or stack[-1][0] == ')':
                    res += "?"
                elif stack[-1][0] == '(':
                    res += " "
                    t = stack[-1][1]
                    res = res[:t] + ' ' + res[t + 1:]
                    stack.pop()
        print(str)
        print(res)


if __name__ == "__main__":
    main()