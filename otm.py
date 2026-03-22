def otm_alg(frames : int, pages : list[int]) -> int:
    cont = 0
    memory = []
    pos_atual = 0

    for page in pages:
        if page not in memory and len(memory) < frames:
            memory.append(page)
            cont += 1

        if page not in memory and len(memory) == frames:
            memo_test = memory.copy()
            pos = []
            for m in memo_test:
                if m not in pages[pos_atual+1:]:
                    pos.append(100000000000000)
                else:
                    pos.append(pages[pos_atual+1:].index(m))
            
            last_page = 0
            cont_aux = 0
            maior_pos = 0
            for p in pos:
                if cont_aux == 0:
                    maior_pos = p
                    last_page = cont_aux
                else:
                    if p > maior_pos:
                        maior_pos = p
                        last_page = cont_aux
                cont_aux += 1
            memory[last_page] = page
            cont+=1
        pos_atual += 1
    return cont

frames = 4
pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]

print(otm_alg(frames, pages))