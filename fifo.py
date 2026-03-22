def fifo_alg(frames : int, pages : list[int]) -> int:
    cont = 0
    memory = []

    for page in pages:
        if page not in memory and len(memory) < frames:
            memory.append(page)
            cont += 1
        
        if page not in memory and len(memory) == frames:
            memory.pop(0)
            memory.append(page)
            cont += 1

    return cont