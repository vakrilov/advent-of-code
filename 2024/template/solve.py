# %%
import os

f = open(os.path.dirname(__file__) + "/sample.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]

# %%
