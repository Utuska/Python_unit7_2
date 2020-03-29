def solve(lst):
    st = []
    z = 0
    for i in lst:
        if i.isdigit():
            st.append(int(i))
            continue
    for j in lst:
        if not j.isdigit():
            z = j
            break
    try:
        y = int(st.pop())
        x = int(st.pop())
        assert z in ['+', '-', '/', '*'], 'Матимотическое выражение не верно'
        n = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x // y
        }[z](x, y)
    except ZeroDivisionError:
        n = 'Делишь на ноль'
    except IndexError:
        n = 'Проблема с индексами'
    return n


lst = input('Enter expression:').split()
print(solve(lst))