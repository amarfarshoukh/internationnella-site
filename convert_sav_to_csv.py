import pyreadstat


input_sav = r"C:\Users\user\OneDrive - Lebanese University\Desktop\adaptive-learning-system\CY08MSP_STU_QQQ.SAV"
output_csv = r"C:\Users\user\OneDrive - Lebanese University\Desktop\adaptive-learning-system\student_dataset.csv"

print("Reading .sav file...")
df, meta = pyreadstat.read_sav(input_sav)

print("Saving to .csv...")
df.to_csv(output_csv, index=False)

print("Done!")


 