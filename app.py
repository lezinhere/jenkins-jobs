import requests
import pandas as pd
import numpy as np
import sys

def main():
    try:
        # Example: Fetch data from a public API
        response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
        if response.status_code != 200:
            print("API call failed")
            sys.exit(1)

        data = response.json()
        print("✅ API Response:", data)

        # Example: Create a DataFrame
        df = pd.DataFrame({
            "Numbers": np.arange(1, 6),
            "Squares": np.arange(1, 6) ** 2
        })
        print("\n📊 DataFrame Example:")
        print(df)

        # Exit code 0 means success
        sys.exit(0)

    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
