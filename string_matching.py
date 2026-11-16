
def naive_search(text, pattern):
    positions = []
    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            positions.append(i)

    return positions


def rabin_karp(text, pattern):
    positions = []
    n = len(text)
    m = len(pattern)
    d = 256
    q = 101

    if m > n:
        return positions

    pattern_hash = 0
    text_hash = 0
    h = pow(d, m - 1, q)

    for i in range(m):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % q
        text_hash = (d * text_hash + ord(text[i])) % q

    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            if text[i:i + m] == pattern:
                positions.append(i)

        if i < n - m:
            text_hash = (
                d * (text_hash - ord(text[i]) * h)
                + ord(text[i + m])
            ) % q

    return positions


text = input("Enter text: ")
pattern = input("Enter pattern to search: ")

if not pattern:
    print("Pattern cannot be empty.")
else:
    import time

    start = time.perf_counter()
    naive_result = naive_search(text, pattern)
    naive_time = time.perf_counter() - start

    start = time.perf_counter()
    rabin_result = rabin_karp(text, pattern)
    rabin_time = time.perf_counter() - start

    print("\nNaive String Matching")
    print("Pattern found at indices:", naive_result)
    print("Execution time:", naive_time, "seconds")

    print("\nRabin-Karp Algorithm")
    print("Pattern found at indices:", rabin_result)
    print("Execution time:", rabin_time, "seconds")

    print("\nBoth algorithms agree:", naive_result == rabin_result)
