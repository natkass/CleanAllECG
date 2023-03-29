import wfdb
import matplotlib.pyplot as plt

# Read the ECG data from the .hea/.dat files
record = wfdb.rdrecord('TNMG102_N1', sampfrom=0)
signals, fields = wfdb.rdsamp('TNMG102_N1', sampfrom=0, sampto=len(record.p_signal))

# Create subplots for each lead
fig, axes = plt.subplots(nrows=4, ncols=2, figsize=(10, 10))

# Plot each lead in its corresponding subplot
for i, ax in enumerate(axes.flat):
    if i < len(signals[0]):
        ax.plot(signals[:, i])
        ax.set_title(fields['sig_name'][i])
        ax.grid(True)

plt.tight_layout()
plt.show()

