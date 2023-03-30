import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file containing the ECG signal data
df = pd.read_csv('TNMG102_N1.csv')

# Extract the signal data into a numpy array
signals = df.values[:, 0:]

# Create subplots for each lead
fig, axes = plt.subplots(nrows=4, ncols=2, figsize=(10, 10))

# Plot each lead in its corresponding subplot
for i, ax in enumerate(axes.flat):
    if i < len(signals[0]):
        ax.plot(signals[:, i])
        ax.set_title('Cleaned Lead ' + str(i+1))
        ax.grid(True)

plt.tight_layout()
plt.show()
