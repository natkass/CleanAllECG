# CleanAllECG

This code applies a DCT-based baseline removal method to ECG signals stored as PhysioNet WFDB files. The baseline removal method is applied to all leads in each file and the resulting baseline-corrected ECG signals are saved to CSV files.

The code first defines a function baseline_dct that takes an ECG signal, the sample rate, and a cutoff frequency as inputs. The function first detrends the ECG signal by fitting a 5th order polynomial to the signal and subtracting it. The detrended signal is then transformed using the DCT (Discrete Cosine Transform). The high-frequency components of the DCT are removed by setting coefficients above the specified cutoff frequency to zero. The inverse DCT is then applied to the filtered coefficients to obtain the baseline-corrected ECG signal.

The code then sets the cutoff frequency and directory path where the ECG data files are stored. For each file in the directory that has a .hea extension, the code loads the header file using wfdb.rdheader, gets the sampling frequency from the header, and loads the ECG data using wfdb.rdsamp. The DCT-based baseline removal is then applied to each lead in the ECG data, and the resulting baseline-corrected ECG signal is saved to a CSV file using np.savetxt.

Finally, the length of the signal is updated in the header and a plot of the original and baseline-corrected ECG signal is shown using wfdb.plot_items.


#Plotcsv

reads a CSV file containing ECG signal data, extracts the signal data into a NumPy array, and creates subplots for each lead. It then plots each lead in its corresponding subplot.

The subplots are arranged in a 4x2 grid using the subplots() function from the matplotlib.pyplot module. The nrows and ncols arguments specify the number of rows and columns in the grid, while the figsize argument specifies the size of the figure in inches.

The enumerate() function is used to iterate over the subplots and assign each subplot to a lead. The flat attribute of the axes object flattens the subplots into a 1-dimensional array, allowing them to be easily iterated over.

If there are fewer than 8 leads, the remaining subplots will be left empty.

Each lead is plotted using the plot() function, and the subplot title is set using the set_title() function. The grid() function is used to display a grid on each subplot.

Finally, the tight_layout() function is called to adjust the spacing between the subplots, and the show() function is called to display the plot.



#plothea

 reads ECG data from a set of .hea/.dat files using the WFDB (Waveform Database) Python package. The rdrecord() function is used to read the header information, and the rdsamp() function is used to read the signal data.

The sampfrom and sampto arguments are used to specify the start and end points of the signal data to be read. In this case, the entire signal is read, from the beginning to the end of the record.

The rdrecord() function returns a Record object, which contains information about the recording, such as the sampling frequency and the number of leads. The p_signal attribute of the Record object contains the actual signal data as a 2-dimensional NumPy array.

The rdsamp() function returns two values: the signal data as a NumPy array, and a dictionary containing metadata about the signals, such as their names and units.

The subplots are created in the same way as in the previous example, using the subplots() function. The enumerate() function is used to iterate over the subplots and assign each subplot to a lead.

Each lead is plotted using the plot() function, and the subplot title is set using the set_title() function, which retrieves the lead name from the fields dictionary using its index. The grid() function is used to display a grid on each subplot.

Finally, the tight_layout() function is called to adjust the spacing between the subplots, and the show() function is called to display the plot.
