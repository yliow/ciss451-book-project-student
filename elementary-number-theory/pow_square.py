def pow(a, n):
    p = 1
    factor = a
    while n != 0:
        bit = n % 2
        n //= 2
        if bit == 1:
            p *= factor
        factor = factor * factor
    return p


for n in range(0, 5):
    print("%s^%s" % (2, n), pow(2, n))
