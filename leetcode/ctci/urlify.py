def test(s):
    length = len(s)
    comp = []
    cur, count = s[0], 1

    for char in s[1:]:
        if char == cur:
            count += 1
        else:
            comp.append(cur)
            comp.append(str(count))
            cur = char
            count = 1

    comp.append(cur)
    comp.append(str(count))

    print ''.join(comp)


test('aabccccaca ')

