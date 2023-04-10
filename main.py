import pandas as pd

def main():
    calculateCompensation()

def calculateCompensation():
    df = pd.read_excel('data11.xlsx', header=0, sheet_name='data')
    print(df)

if __name__ == "__main__":
    main()