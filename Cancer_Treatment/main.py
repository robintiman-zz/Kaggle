import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read file using pandas
train_variants = pd.read_csv("data/training_variants")

# Fetch the column values
ids = train_variants.ID.values
genes = train_variants.Gene.values
variations = train_variants.Variation.values
classes = train_variants.Class.values

unique_genes = np.unique(genes)
unique_variations = np.unique(variations)
unique_classes = np.unique(classes)

"""
Finds all the genes and variations for a given class and counts the 
number of occurrences. 
"""
def analyze(cls):
    # Find the instances where class is set to the given cls
    indices = np.where(classes == cls)[0]

    # Count the number of occurrences of each gene for this class.
    class_genes = np.unique(genes[indices], return_counts=True)

    all_genes = np.zeros((len(unique_genes), 1))

    j = 0
    for i in range(len(unique_genes)):
        if unique_genes[i] == class_genes[0][j]:
            all_genes[i] = class_genes[1][j]
            j += 1
        if j == len(class_genes[0]):
            break

    plt.scatter(np.arange(0, len(all_genes)), np.transpose(all_genes), label="class={}".format(cls))

for cls in unique_classes:
    analyze(cls)

plt.legend()
plt.xticks(range(len(unique_genes)), unique_genes, rotation=90)
plt.show()

