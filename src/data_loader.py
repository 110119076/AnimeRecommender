import pandas as pd

class AnimeDataLoader:
    def __init__(self, original_csv_path: str, updated_csv_path: str):
        self.original_csv_path = original_csv_path
        self.updated_csv_path = updated_csv_path
    
    def load_and_update(self):
        df = pd.read_csv(self.original_csv_path, encoding="utf-8", on_bad_lines="skip").dropna()

        required_cols = {"Name", "Genres", "synopsis"}
        missing_cols = required_cols - set(df.columns)

        if missing_cols:
            raise ValueError("Missing required column in CSV file")
        
        df["anime_info"] = ("Title: " + df["Name"] + "Overview: " + df["synopsis"] + "Genres: " + df["Genres"])

        df[["anime_info"]].to_csv(self.updated_csv_path, index=False, encoding="utf-8")

        return self.updated_csv_path