# Simulador de Algoritmos de Substituição de Páginas

Simulação dos algoritmos de substituição de páginas em sistemas operacionais, retornando o número de **page faults** (faltas de página) para cada estratégia.

---

## Conceitos

A memória física é dividida em **quadros** (frames). Quando um processo acessa uma página que não está carregada em nenhum quadro, ocorre uma **falta de página** (page fault) e o SO precisa carregá-la. Se todos os quadros estiverem ocupados, uma página precisa ser **substituída** — e é aí que cada algoritmo age de forma diferente.

---

## Algoritmos Implementados

### FIFO — First In, First Out (`fifo_alg`)

A página que **entrou primeiro** na memória é a primeira a ser removida quando um quadro precisa ser liberado.

**Exemplo** com 4 quadros e páginas `[1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]`:

| Página | Memória após acesso | Page Fault? |
|--------|---------------------|-------------|
| 1 | [1] | ✅ |
| 2 | [1, 2] | ✅ |
| 3 | [1, 2, 3] | ✅ |
| 4 | [1, 2, 3, 4] | ✅ |
| 1 | [1, 2, 3, 4] | ❌ |
| 2 | [1, 2, 3, 4] | ❌ |
| 5 | [5, 2, 3, 4] | ✅ |
| ... | ... | ... |

---

### Ótimo — OPT (`otm_alg`)

Substitui a página que **será usada mais longe no futuro** (ou que não será mais usada). É um algoritmo teórico — exige conhecimento prévio de toda a sequência de acessos — mas serve como **referência do menor número possível de page faults**.

---

### LRU — Least Recently Used (`lru_alg`)

Substitui a página que **foi usada há mais tempo**. A lista de memória funciona como um ranking de recência — índice `0` é a mais antiga, índice `-1` é a mais recente. Toda vez que uma página é acessada, ela é movida para o final.

---

### IO Handler (`io_handler`)

Lê o arquivo de entrada e retorna o número de quadros e o vetor de páginas.

---

## Uso

```python
frames = 4
pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]

print(fifo_alg(frames, pages))  # page faults com FIFO
print(lru_alg(frames, pages))   # page faults com LRU
print(otm_alg(frames, pages))   # page faults com algoritmo ótimo
```

---

## Estrutura do Projeto

```
.
├── fifo.py
├── io_handler.py
├── lru.py
├── main.py
├── otm.py
├── teste.txt   #arquivo com a numeração de entrada
└── README.md
```