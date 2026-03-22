def otm_alg(frames : int, pages : list[int]) -> int:
    cont = 0
    memory = []
    pos_atual = 0

    for page in pages:
        # página não está na memória e ainda há quadros livres
        if page not in memory and len(memory) < frames:
            memory.append(page)
            cont += 1
        # página não está na memória e todos os quadros estão ocupados
        if page not in memory and len(memory) == frames:
            memo_test = memory.copy()   # cópia da memória para análise
            pos = []                    # lista com a próxima posição de uso de cada página

            # para cada página na memória, descobre quando ela será usada novamente
            for m in memo_test:
                if m not in pages[pos_atual + 1:]:
                    # página não será usada no futuro, candidata para remoção
                    pos.append(100000000000000)
                else:
                    # índice da próxima ocorrência da página no vetor restante
                    pos.append(pages[pos_atual + 1:].index(m))

            # encontra qual página na memória tem o uso mais distante no futuro
            last_page = 0    # índice (em memory) da página a ser substituída
            cont_aux = 0     # contador auxiliar para percorrer pos
            maior_pos = 0    # maior distância futura encontrada até agora

            for p in pos:
                if cont_aux == 0:
                    # inicializa com o primeiro elemento
                    maior_pos = p
                    last_page = cont_aux
                else:
                    # atualiza se encontrar uma página com uso ainda mais distante
                    if p > maior_pos:
                        maior_pos = p
                        last_page = cont_aux
                cont_aux += 1

            # substitui a página mais distante no futuro pela nova página
            memory[last_page] = page
            cont += 1

        pos_atual += 1  # avança para a próxima posição no vetor de páginas

    return cont