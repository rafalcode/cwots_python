#!/usr/bin/env python3
# this script does what?

data = [
    (0, 0.15),
    (1, 0.60),
    (1, 0.75),
    (0, 0.30),
    (0, 0.40),
    (1, 0.85),
    (1, 0.95),
    (0, 0.20),
    (1, 0.70),
    (0, 0.45),
]

# Sort the data by predicted probabilities in descending order
data.sort(key=lambda x: x[1], reverse=True)

# The sorted data will now be in descending order of predicted probabilities
print(data)
