import numpy as np
import pandas as pd

TOSSES = 5
PATHS = 50

np.random.seed(1)
samples = pd.DataFrame(data=np.random.rand(PATHS, TOSSES),
                       columns=range(1, 1+TOSSES))
