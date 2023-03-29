import wfdb
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.signal import butter, filtfilt

# Define the DCT-based baseline removal function
def baseline_dct(ecg_signal, sample_rate, cutoff):
    n = len(ecg_signal)
    t = np.arange(n) / float(sample_rate)
    p = np.polyfit(t, ecg_signal, 5)
    ecg_detrend = ecg_signal - np.polyval(p, t)
    ecg_dct = np.fft.fft(ecg_detrend)
    ecg_dct[int(cutoff * n):] = 0
    ecg_baseline = np.real(np.fft.ifft(ecg_dct))
    return ecg_baseline

# Set cutoff frequency (in Hz) for the DCT
cutoff_freq = 0.05 # adjust this value as needed

# Set the directory path where ECG data files are stored
directory_path = './S0000000'

# Loop through all files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.hea'):  # Load header file
        record_name = os.path.splitext(filename)[0]
        record_path = os.path.join(directory_path, record_name)
        header = wfdb.rdheader(record_path)
        
        # Get sampling frequency
        sample_rate = header.fs

        # Load ECG data
        data = wfdb.rdsamp(record_path)[0]
        
        # Apply the DCT-based baseline removal to the ECG signal for each lead
        ecg_corrected = np.zeros_like(data)
        for i in range(data.shape[1]):
            ecg_signal = data[:, i] - np.mean(data[:, i])
            ecg_baseline = baseline_dct(ecg_signal, sample_rate, cutoff_freq)
            ecg_corrected[:, i] = ecg_baseline
        
        # Update the signal length in the header
        header.sig_len = len(ecg_baseline)
        wfdb.plot_items(signal=ecg_signal,
                    title='MIT-BIH Record 100', time_units='seconds',
                    figsize=(10,4), ecg_grids='all')
        # Save the baseline-corrected ECG signal to a CSV file
        output_folder = os.path.join(directory_path, 'baseline_corrected_ecg')
        if not os.path.exists(output_folder):
            os.mkdir(output_folder)
        output_filename = os.path.join(output_folder, record_name + '.csv')
        np.savetxt(output_filename, ecg_corrected, delimiter=',')
        print(f"Baseline-corrected ECG signal saved to {output_filename}")
