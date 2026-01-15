import pandas as pd

df = pd.read_csv(
    r"C:\Users\steve\Downloads\Data_Mining\Data_Mining_Project\Data_mining_project\dataset\DM1_game_dataset.csv"
)

df_ridotto = df.sample(n=1000, random_state=42)
df_ridotto.to_csv("dataset_ridotto.csv", index=False)
print("Dataset ridotto creato con successo e salvato come 'dataset_ridotto.csv'")