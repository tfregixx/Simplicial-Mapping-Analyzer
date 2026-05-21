import itertools

# =============================
# 1. Simplicial Complex Class
# =============================
class SimplicialComplex:
    def __init__(self, vertices, simplices):
        self.vertices = vertices
        self.simplices = [tuple(sorted(s)) for s in simplices]


# =============================
# 2. Define Complexes
# =============================

# Triangle WITHOUT filling (loop exists)
K = SimplicialComplex(
    vertices=[0, 1, 2],
    simplices=[
        (0,), (1,), (2,),
        (0,1), (1,2), (0,2)
        # NOTE: No (0,1,2) → loop exists
    ]
)

# Line
L = SimplicialComplex(
    vertices=['a', 'b'],
    simplices=[
        ('a',), ('b',),
        ('a','b')
    ]
)


# =============================
# 3. Generate Vertex Maps
# =============================
def generate_maps(K, L):
    return list(itertools.product(L.vertices, repeat=len(K.vertices)))


# =============================
# 4. Check Simplicial Map
# =============================
def is_simplicial_map(mapping, K, L):
    vertex_map = dict(zip(K.vertices, mapping))

    for simplex in K.simplices:
        image = tuple(sorted(set(vertex_map[v] for v in simplex)))
        if image not in L.simplices:
            return False
    return True


# =============================
# 5. Classification
# =============================
def classify_map(mapping, K, L):
    values = list(mapping)
    injective = len(set(values)) == len(values)
    surjective = set(values) == set(L.vertices)
    return injective, surjective


# =============================
# 6. HOMOLOGY COMPUTATION
# =============================
def compute_homology(complex):
    """
    Compute:
    H0 = number of connected components
    H1 = number of loops using Euler characteristic
    """

    vertices = complex.vertices
    edges = [s for s in complex.simplices if len(s) == 2]
    triangles = [s for s in complex.simplices if len(s) == 3]

    # ---- H0 using Union-Find
    parent = {v: v for v in vertices}

    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]

    def union(a, b):
        parent[find(a)] = find(b)

    for e in edges:
        union(e[0], e[1])

    H0 = len(set(find(v) for v in vertices))

    # ---- H1 (loop count)
    H1 = max(0, len(edges) - len(vertices) + H0 - len(triangles))

    return H0, H1


# =============================
# 7. Homology Preservation
# =============================
def preserves_homology(K, L):
    return compute_homology(K) == compute_homology(L)


# =============================
# 8. Run Project
# =============================
all_maps = generate_maps(K, L)

valid_maps = []

for m in all_maps:
    if is_simplicial_map(m, K, L):
        injective, surjective = classify_map(m, K, L)
        valid_maps.append((m, injective, surjective))


# =============================
# 9. Output
# =============================
print("\n===== HOMOLOGY RESULTS =====")
print("Homology of K (Triangle loop): H0, H1 =", compute_homology(K))
print("Homology of L (Line): H0, H1 =", compute_homology(L))

if preserves_homology(K, L):
    print("✅ Homology preserved")
else:
    print("❌ Homology NOT preserved (IMPORTANT RESULT)")


print("\n===== VALID SIMPLICIAL MAPS =====\n")

for m in valid_maps:
    print("Mapping:", dict(zip(K.vertices, m[0])))
    print("Injective:", m[1], "| Surjective:", m[2])
    print("----------------------------")