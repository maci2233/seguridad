def build_table(key):
    n = 5
    coords = {}
    mat = [['-' for i in range(n)] for i in range(n)]
    m = len(key)
    i,j,k,char = 0,0,0,65
    while i < n:
        while j < n:
            if k < m:
                mat[i][j] = key[k]
                coords[key[k]] = [i, j]
                k += 1
                j += 1
            else:
                letter = chr(char)
                if letter != 'J' and letter not in coords:
                    mat[i][j] = letter
                    coords[letter] = [i, j]
                    j += 1
                char += 1
        i += 1
        j = 0
    return [mat, coords]


def encrypt(message, mat, coords):
    res = ''
    enc = list()
    for word in message:
        for c in word:
            enc.append(coords[c][0])
    for word in message:
        for c in word:
            enc.append(coords[c][1])
    n = len(enc)
    for i in range(0, n, 2):
        res += mat[enc[i]][enc[i+1]]
    return res


def decrypt(message, mat, coords):
    res = ''
    dec = list()
    for word in message:
        for c in word:
            coord = coords[c]
            dec.append(coord[0])
            dec.append(coord[1])
    n = len(dec)
    mid = n // 2
    for i in range(mid):
        res += mat[dec[i]][dec[i+mid]]
    return res


def main():
    key = input()
    message = input().split()
    mat, coords = build_table(key)
    if len(message) > 1:
        print(encrypt(message, mat, coords))
    else:
        print(decrypt(message, mat, coords))


main()
