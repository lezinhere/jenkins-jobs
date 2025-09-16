import requests
import pandas as pd
import numpy as np

def main():
    # Example: Fetch data from a public API
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    data = response.json()
    print("API Response:", data)

    # Example: Create a small DataFrame
    df = pd.DataFrame({
        "Numbers": np.arange(1, 6),
        "Squares": np.arange(1, 6) ** 2
    })
    print("\nDataFrame Example:")
    print(df)

if __name__ == "__main__":
    main()
