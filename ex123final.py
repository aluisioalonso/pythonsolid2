#Desafio Tideman
from itertools import combinations

MAX = 9
candidates = []
candidate_count = 0
preferences = [[0] * MAX for _ in range(MAX)]
pairs = []

class Pair:
    def __init__(self, winner, loser):
        self.winner = winner
        self.loser = loser

def vote(rank, name, ranks):
    """
    Atualiza ranks com a posição do candidato votado.
    """
    if name in candidates:
        ranks[rank] = candidates.index(name)
        return True
    return False

def record_preferences(ranks):
    """
    Atualiza a matriz de preferências com base no voto do eleitor.
    """
    for i in range(len(ranks)):
        for j in range(i + 1, len(ranks)):
            preferences[ranks[i]][ranks[j]] += 1

def add_pairs():
    """
    Cria pares de candidatos que venceram uns aos outros.
    """
    global pairs
    for i, j in combinations(range(candidate_count), 2):
        if preferences[i][j] > preferences[j][i]:
            pairs.append(Pair(i, j))
        elif preferences[j][i] > preferences[i][j]:
            pairs.append(Pair(j, i))

def sort_pairs():
    """
    Ordena os pares com base na força da vitória.
    """
    pairs.sort(key=lambda pair: preferences[pair.winner][pair.loser] - preferences[pair.loser][pair.winner], reverse=True)

def is_cycle(locked, winner, loser):
    """
    Verifica se adicionar uma aresta criaria um ciclo no grafo.
    """
    if winner == loser:
        return True
    for i in range(candidate_count):
        if locked[loser][i] and is_cycle(locked, winner, i):
            return True
    return False

def lock_pairs():
    """
    Constrói o grafo direcionado dos pares ordenados, evitando ciclos.
    """
    locked = [[False] * MAX for _ in range(MAX)]
    for pair in pairs:
        if not is_cycle(locked, pair.winner, pair.loser):
            locked[pair.winner][pair.loser] = True
    return locked

def find_winner(locked):
    """
    Determina o vencedor, que é o candidato sem nenhuma aresta apontando para ele.
    """
    for i in range(candidate_count):
        if all(not locked[j][i] for j in range(candidate_count)):
            print(f"Vencedor: {candidates[i]}")
            return


candidates = ["Alice", "Bob", "Charlie"]
candidate_count = len(candidates)


votes = [
    ["Alice", "Charlie", "Bob"],
    ["Charlie", "Alice", "Bob"],
    ["Bob", "Charlie", "Alice"]
]

for vote_set in votes:
    ranks = [0] * candidate_count
    for rank, name in enumerate(vote_set):
        vote(rank, name, ranks)
    record_preferences(ranks)

add_pairs()
sort_pairs()
locked = lock_pairs()
find_winner(locked)

