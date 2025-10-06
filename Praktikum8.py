def biconditional_logic():
    print("=== Bikondisional (Bi-implikasi) ===")
    p = True
    q = False
    # Bikondisional (p <-> q) terjasi ketika p dan q memiliki nilai yang sama
    biconditional = (p and q) or (not p and not q)
    print(f"p: {p}, q: {q}, p <-> q: {biconditional}")
    print("===========================================\n")

def inference():
    print("=== Inferensi ===")
    p = True
    q = False
    # Inferensi: Jika p -> q dan p benar, maka q juga benar
    implication = not p or q
    print(f"p: {p}, q: {q}, p -> q: {implication}")
    if p and implication: 
        print(f"Dengan p benar, q harus: {q}")
    print("===========================================\n")

def argument():
    print("=== Argumen ===")
    p = True
    q = False
    r = True
    # Argumen dalam logika, contoh sederhna:
    # Jika p -> q dan q -> r, maka p -> r
    premise_1 = not p or q # p -> q
    premise_2 = not q or r # q -> r
    conclusion = not p or r # p -> r
    print(f"Premis 1 (p -> q): {premise_1}")
    print(f"Premis 2 (q -> r): {premise_2}")
    print(f"Kesimpulan (p -> r): {conclusion}")
    print("===========================================\n")

def axioms_theorems():
    print("=== Aksioma, Teorema, Lemma, dan Corollary ===")
    # Aksioma: Pernyataan dasar yang diasumsikan benar tanpa pembuktian 
    aksioma = True # Contoh aksioma yang selalu benar
    print(f"Aksioma: {aksioma} (selalu dianggap benar)")

    #Teorema: Pernyataan yang dibuktikan benar berdasarkan aksioma atau proposisi lain 
    teorema = aksioma and True # Teorema dibuktikan dari aksioma
    print(f"Teorema: {teorema} (berdasarkan aksioma)")

    #Lemma: Pernyataan yang digunakan untuk membantu pembuktian teorema
    lemma = teorema # Lenna adalah bagian dari pembuktian teorema 
    print(f"Lemma: {lemma} (digunakan untuk membantu membuktikan teorema)")

    #Corollary: Pernyataan yang merupakan konsekuensi langsung dari teorema 
    corollary = teorema # Corollary adalah hasil langsung dari teorema
    print(f"Corollary: {corollary} (konsekuensi langsung dari teorema)")
    print("===========================================\n")


if __name__ == "__main__":
    biconditional_logic()
    inference()
    argument()
    axioms_theorems()


