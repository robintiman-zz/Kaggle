import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read file using pandas
train_variants = pd.read_csv("training_variants")

# Fetch the column values
ids = train_variants.ID.values
genes = train_variants.Gene.values
variations = train_variants.Variation.values
classes = train_variants.Class.values

unique_genes = np.unique(genes)
unique_variations = np.unique(variations)
print(unique_genes,"\n\n",unique_variations)

"""
Finds all the genes and variations for a given class and counts the 
number of occurrences. 
"""
def analyze(cls):
    indices = np.where(classes == cls)[0]
    class_genes = genes[indices]
    class_variations = variations[indices]
    unique_class_genes = np.unique(class_genes, return_counts=True)
    unique_class_variations = np.unique(class_variations, return_counts=True)
    return unique_class_genes, unique_class_variations

"""
Visualizes it in scatter plot with the number of occurrences for a given class as 
the y value. The indices as x values.  
"""
def vizualise(cls):
    gene_count, variations_count = analyze(cls)
    plt.title("class=1")
    x_genes = np.arange(0, len(gene_count[1]))
    x_variations = np.arange(0, len(unique_variations))
    plt.scatter(x_genes, gene_count[1])

vizualise(1)
vizualise(2)
vizualise(3)
vizualise(4)
vizualise(5)

plt.show()

