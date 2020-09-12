def remove_duplicates(S: str) -> str:
    l = []
    for i in S:
        if l and l[-1] == i:
            l.pop()
        else:
            l.append(i)
    return ''.join(l)


if __name__ == '__main__':
    rs = remove_duplicates("aaaa")
    print(rs)
