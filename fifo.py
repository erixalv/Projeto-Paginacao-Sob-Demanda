def fifo_alg(frames : int, pages : list[int]) -> int:
    cont = 0      
    memory = []   
 
    for page in pages:
        # página não está na memória e ainda há quadros livres
        if page not in memory and len(memory) < frames:
            memory.append(page)
            cont += 1
 
        # página não está na memória e todos os quadros estão ocupados
        if page not in memory and len(memory) == frames:
            memory.pop(0)       # remove a página mais antiga (primeira a ter entrado)
            memory.append(page) # insere a nova página no final da fila
            cont += 1
 
    return cont