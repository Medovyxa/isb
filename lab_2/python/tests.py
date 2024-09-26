from scipy.special import gammainc, erfc
import numpy as np


def runs_test(sequence: str) -> float:
    """
    Runs Test based on the sequence.
    Returns p-value.
    """
    n = len(sequence)
    ones = sequence.count('1')
    pi = ones / n

    
    if abs(pi - 0.5) >= (2 / np.sqrt(n)):
        return 0.0  
    
    v_n = sum(1 for i in range(1, n) if sequence[i] != sequence[i - 1]) + 1
    p_value = erfc(abs(v_n - 2 * n * pi * (1 - pi)) / (2 * np.sqrt(2 * n) * pi * (1 - pi)))
    
    return p_value

def run_tests(sequences):
    """
    Runs all NIST tests on each sequence.
    """
    results = {}
    
    for name, sequence in sequences.items():
        results[name] = {
            "Runs Test": runs_test(sequence),
        }
    
    return results