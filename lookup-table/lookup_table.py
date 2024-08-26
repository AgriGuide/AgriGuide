import pandas as pd
import sys

def lookup_table(temp : int, rainfall : int, soil_type : str):
    df = pd.read_excel('data/lookup.xlsx')

    #select rows which matches with soil_type parameter from soil-type or soil-type2 column
    df = df[(df['soil-type'] == soil_type) | (df['soil-type2'] == soil_type)]

    #select rows which the parameters fall within the optimal range
    df = df[(df['temp-opt-min'] <= temp) & (df['temp-opt-max'] >= temp)]
    df = df[(df['rainfall-opt-min'] <= rainfall) & (df['rainfall-opt-max'] >= rainfall)]

    #calculate a score for each row based on the distance from the middle of the optimal range
    df['temp-score'] = abs(df['temp-opt-min'] + df['temp-opt-max'] / 2 - temp)
    df['rainfall-score'] = abs(df['rainfall-opt-min'] + df['rainfall-opt-max'] / 2 - temp)

    #calculate the total score for each row
    df['total-score'] = df['temp-score'] + df['rainfall-score']

    #sort the rows based on the total score
    df = df.sort_values('total-score', ascending=True)

    #return the first three crops from the sorted rows
    return df['crop'].head(3).tolist()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python lookup_table.py temp rainfall soil_type")
        sys.exit(1)

    temp = int(sys.argv[1])
    rainfall = int(sys.argv[2])
    soil_type = sys.argv[3]
    result = lookup_table(temp, rainfall, soil_type)

    sys.exit(result)



    