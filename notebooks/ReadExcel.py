#%%
import pathlib
import pandas as pd

#%%
# Get the path to the Excel file.
repo_dir = pathlib.PurePath(__file__).parent.parent
data_dir = pathlib.PurePath(repo_dir, 'data')
peaks_xls = str(pathlib.PurePath(data_dir, 'Peaks.xlsx'))
print(peaks_xls)

#%%
# Get the first sheet.
simple_peaks = pd.read_excel(peaks_xls)
print(simple_peaks.head())

#%%
# Get the "Offset" sheet.
offset_peaks = pd.read_excel(peaks_xls, 'Offset', usecols='B:G', skiprows=2)
print(offset_peaks.head())

#%%
# Get the "Gap" sheet, and name the columns.
gap_peaks = pd.read_excel(
    peaks_xls,
    'Gap',
    names=[
        'Name',
        'Z',
        'Prettiness',
        'Walkability',
        'When'
    ],
    usecols='B:F',
    skiprows=4
)
print(gap_peaks.head())


#%%
