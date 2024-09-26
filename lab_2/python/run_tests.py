import json
from tests import run_tests

def load_sequences(filename="sequences.json"):
    """
    Loads bit sequences from a JSON file.
    """
    with open(filename, 'r') as f:
        return json.load(f)

if __name__ == "__main__":
    sequences = load_sequences()
    results = run_tests(sequences)
    for seq_name, result in results.items():
        print(f"Results for {seq_name}:")
        for test, value in result.items():
            print(f"{test}: {value}")
        print()
