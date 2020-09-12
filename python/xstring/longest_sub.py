def length_of_longest_substring(s: str) -> int:
    m = set()
    rs, l = 0, 0

    for r in range(len(s)):
        while s[r] in m:
            m.remove(s[l])
            l += 1
        m.add(s[r])
        print(r - l + 1)
        rs = max(rs, r - l + 1)
    return rs


if __name__ == '__main__':
    print(length_of_longest_substring("bacabcbb"))
