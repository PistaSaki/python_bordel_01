import matplotlib.pyplot as pl
import numpy as np
from time import sleep

t = 3

print("Crate a figure.")
fig, ax = pl.subplots()
xxx = np.linspace(-1, 1, 100)
ax.plot(xxx, xxx**2)

print(f"Figure created, waiting {t} seconds.")
sleep(t)

print(f"Call `pl.show`.")
pl.show(block = False)

print("This message is probably shown only after plot has been killed.")