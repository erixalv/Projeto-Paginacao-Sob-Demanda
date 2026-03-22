from fifo import fifo_alg
from otm import otm_alg
from lru import lru_alg

from io_handler import io_handler

FILE_PATH = "teste.txt"

frames, pages = io_handler(FILE_PATH)

print(f'FIFO {fifo_alg(frames, pages)}')
print(f'OTM {otm_alg(frames, pages)}')
print(f'LRU {lru_alg(frames, pages)}')