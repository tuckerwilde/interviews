def reverse(n):
    res = 0

    for _ in range(32):
        # If our current bit is a one, append that one. keep moving forward.
        res = (res << 1) + (n & 1)
        # Bit shift down 1.
        n >>= 1
    return res