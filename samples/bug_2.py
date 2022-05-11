from time import perf_counter
t = perf_counter()
from vitrix_engine import *

app = Ursina()

print('----', perf_counter() - t)

app.run()
