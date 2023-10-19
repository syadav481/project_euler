def generate_pythagorean_triples(limit):
    triples = []
    m = 2

    while True:
        for n in range(1, m):
            a = m**2 - n**2
            b = 2 * m * n
            c = m**2 + n**2

            if c > limit:
                return triples

            triples.append((a, b, c))

        m += 1


# Example: Generate Pythagorean triples with c <= 50
limit = 50
triples = generate_pythagorean_triples(1000)
for triple in triples:
    if sum(triple) == 1000:
        print(triple)
        print(triple[0] * triple[1] * triple[2])
        break
