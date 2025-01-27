import matplotlib.pyplot as plt
import numpy as np

# Simulate data: Random ages of 1000 cancer patients (assume age between 20 and 80)
np.random.seed(42)  # For reproducibility
data = np.random.randint(20, 81, 1000)  # Generate 1000 random ages between 20 and 80

# Create a histogram
plt.hist(data, bins=15, edgecolor='black', color='skyblue')

# Set the title and labels for the plot
plt.title('Histogram of Cancer Patients Age Distribution')
plt.xlabel('Age')
plt.ylabel('Number of Patients')

# Show the plot
plt.show()