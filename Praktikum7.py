def identity_law():
    print("=== Identity Law ===")
    p = True
    print(f"p OR False: {p or False}")
    print(f"p AND True: {p and True}")
    print("=======================================\n")

def commutative_law():
    print("=== Commutative Law ===")
    p = True
    q = False
    print(f"p OR q: {p or q}")
    print(f"q OR p: {q or p}")
    print(f"p AND q: {p and q}")
    print(f"q AND p: {q and p}")
    print("===========================================\n")

def associative_law():
    print("=== Associative Law ===")
    p = True
    q = False
    r = True
    print(f"(p OR q) OR r: {(p or q) or r}")
    print(f"p OR (q OR r): {p or (q or r)}")
    print(f"(p AND q) AND r: {(p and q) and r}")
    print(f"p AND (q AND r): {p and (q and r)}")
    print("===========================================\n")

def distributive_law():
    print("=== Distributive Law ===")
    p = True
    q = False
    r = True
    print(f"p AND (q OR r): {p and (q or r)}")
    print(f"(p AND q) OR (p AND r): {(p and q) or (p and r)}")
    print(f"p OR (q AND r): {p or (q and r)}")
    print(f"(p OR q) AND (p OR r): {(p or q) and (p or r)}")
    print("===========================================\n")

def converse():
    print("=== Converse (Konversi) ===")
    p = False
    q = True
    print(f"q -> p: {q} -> {p}")
    print("===========================================\n")

def inverse():
    print("=== Inverse (Invers) ===")
    p = False
    q = True
    print(f"~p -> ~q: {not p} -> {not q}")
    print("===========================================\n")

def contrapositive():
    print("=== Contrapositive (Kontraposisi) ===")
    p = False
    q = True
    print(f"~q -> ~p: {not q} -> {not p}")
    print("===========================================\n")

def modus_ponens():
    print("=== Modus Ponens ===")
    p = True
    q = False
    print(f"q: {q}")
    print("===========================================\n")

def modus_tollens():
    print("=== Modus Tollens ===")
    p = True
    q = False
    print(f"~q: {not p}")
    print("===========================================\n")

def syllogism():
    print("=== Syllogism ===")
    p = True
    q = False
    r = False
    print(f"p -> r: {p} -> {r}")
    print("===========================================\n")

if __name__ == "__main__":

    identity_law()
    commutative_law()
    associative_law()
    distributive_law()

    converse()
    inverse()
    contrapositive()

    modus_ponens()
    modus_tollens()
    syllogism()

