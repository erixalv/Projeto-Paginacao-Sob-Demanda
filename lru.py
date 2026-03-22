def lru_alg(frames : int, pages : list[int]) -> int:
    cont = 0
    memory = []

    for page in pages:
        if page not in memory:
            cont += 1
            if len(memory) == frames:
                # O índice 0 é SEMPRE a página acessada há mais tempo
                memory.pop(0)
            
            # Adiciona a nova página; como ela acabou de ser acessada, ela entra no final (mais recente)
            memory.append(page)
        else:
            memory.remove(page)
            memory.append(page) # Definindo uma nova idade ao elemento

    return cont