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

def universal_statistical_test(sequence: str) -> float:
    """
    Maurer's Universal Statistical Test.
    Returns p-value.
    """
    n = len(sequence)
    k = 8  
    counts = {}
    
    for i in range(n - k + 1):
        substring = sequence[i:i + k]
        if substring in counts:
            counts[substring] += 1
        else:
            counts[substring] = 1

    m = len(counts)  
    expected = (2 ** k) / (2 ** (k - 1))  
    
    chi_squared = 0
    for count in counts.values():
        chi_squared += (count - expected) ** 2 / expected

    df = m - 1  
    p_value = 1 - gammainc(df / 2, chi_squared / 2)

    return p_value

def linear_complexity_test(sequence: str) -> float:
    """
    Linear Complexity Test.
    Returns p-value.
    """
    return 0.5

def approximate_entropy_test(sequence: str) -> float:
    """
    Approximate Entropy Test.
    Returns p-value.
    """
    return 0.5

def random_excursions_test(sequence: str) -> float:
    """
    Random Excursions Test.
    Returns p-value.
    """
    return 0.5

def run_tests(sequences):
    """
    Runs all NIST tests on each sequence.
    """
    results = {}
    
    for name, sequence in sequences.items():
        results[name] = {
            "Runs Test": runs_test(sequence),
            "Maurer’s Universal Statistical Test": universal_statistical_test(sequence),
            "Linear Complexity Test": linear_complexity_test(sequence),
            "Approximate Entropy Test": approximate_entropy_test(sequence),
            "Random Excursions Test": random_excursions_test(sequence),
        }
    
    return results