import re

def prepare_text(text: str) -> list:
    text = text.lower()
    wordlist = re.findall(r"[\w'’]+", text, flags=0)
    return wordlist



def wer(reference: str, hypothesis: str):
    ref = prepare_text(reference)
    hyp = prepare_text(hypothesis)

    N = len(ref)
    M = len(hyp)

    d = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(N + 1):
        d[i][0] = i
    for j in range(M + 1):
        d[0][j] = j

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if ref[i - 1] == hyp[j - 1]:
                cost = 0
            else:
                cost = 1
            d[i][j] = min(
                d[i - 1][j] + 1,
                d[i][j - 1] + 1,
                d[i - 1][j - 1] + cost
                )

    for row in d:
        print(row)

    S = I = D = 0
    i, j = N, M

    while i > 0 or j > 0:
        if i > 0 and j > 0 and ref[i - 1] == hyp[j - 1] and d[i][j] == d[i - 1][j - 1]:
            i -= 1
            j -= 1
        elif i > 0 and j > 0 and d[i][j] == d[i - 1][j - 1] + 1:
            S += 1
            i -= 1
            j -= 1
        elif i > 0 and d[i][j] == d[i - 1][j] + 1:
            D += 1
            i -= 1
        else:
            I += 1
            j -= 1

    if N == 0:
        wer_value = 0.0 if M == 0 else 1.0
    else:
        wer_value = (S + D + I) / N

    return round(wer_value, 2), S, D, I, N