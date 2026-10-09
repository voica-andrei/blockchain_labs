## E:Y^2 = X^3 + 497X + 1768 mod 9739
p = 9739
a = 497
b = 1768

def point_add(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P

    x1, y1 = P
    x2, y2 = Q

    # Opposite points cancel each other
    if x1 == x2 and (y1 + y2) % p == 0:
        return None

    # Calculate lambda
    if P == Q:
        # Point doubling
        lam = ((3 * x1**2 + a) * pow(2 * y1, -1, p)) % p
    else:
        # Addition of different points
        lam = ((y2 - y1) * pow(x2 - x1, -1, p)) % p

    # Calculate resulting coordinates
    x3 = (lam**2 - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p

    return (x3, y3)



P = (493, 5564)
Q = (1539, 4742)
R = (4403, 5202)

S = point_add(P, P)
S = point_add(S, Q)
S = point_add(S, R)

print(f"crypto{{{S[0]},{S[1]}}}")

