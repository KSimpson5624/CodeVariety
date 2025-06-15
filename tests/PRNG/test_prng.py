import numpy as np
from scipy.stats import chisquare
from collections import Counter
from src.codevariety import PRNG
import pytest

###########################################################################################
#                                                                                         #
#                                     Fixtures                                            #
#                                                                                         #
###########################################################################################
@pytest.fixture
def prng_instance():
    return PRNG()

@pytest.fixture(params=["random_integer", "random_float"])
def prng_method(request, prng_instance):
    return get_prng_method(prng_instance, request.param)

###########################################################################################
#                                                                                         #
#                                  Helper Functions                                       #
#                                                                                         #
###########################################################################################

def get_prng_method(prng_instance, method_name):
    '''
    Helper function to dynamically fetch methods from the PRNG instance.
    
    Args:
        prng_instance: The PRNG instance.
        method_name (str): The name of the method to fetch.
        
    Returns:
        Callable: The resolved method.
    '''
    return getattr(prng_instance, method_name)

###########################################################################################
#                                                                                         #
#                                       Tests                                             #
#                                                                                         #
###########################################################################################
def test_uniformity(prng_instance, prng_method):

    max_value = prng_instance.max_value
    prng_output = [prng_method() / max_value for _ in range(1000)]

    mean = np.mean(prng_output)
    variance = np.var(prng_output)

    expected_mean = 0.5
    expected_variance = 1 / 12

    # Assert the mean is close to .5 (expected for uniform distribution [0,1])
    assert np.isclose(mean, expected_mean, atol=0.01), f'Mean is outside expected range: {mean}. Expected: {expected_mean}. Tolerance: ±0.01'

    # Assert the variance is close to the theorectical value (1/12 for uniform [0,1])
    assert np.isclose(variance, expected_variance, atol=0.01), f'Variance is outside expected range: {variance}. Expected: {expected_variance}. Tolerance: ±0.01'

def test_max_value_check(prng_instance, prng_method):

    current_max_value = prng_instance.max_value
    prng_output = [prng_method() for _ in range(10000)]
    real_max_value = max(prng_output)

    assert current_max_value >= real_max_value, (
        'PRNG max_value is too low! '
        f'Current max: {current_max_value}, New max: {real_max_value} '
        f'Increase the max_value to at least {real_max_value}')
    
def test_entropy_measurement(prng_method):
    prng_output = [prng_method() for _ in range(10000)]

    frequencies = Counter(prng_output)
    total = sum(frequencies.values())
    probabilities = [freq / total for freq in frequencies.values()]

    # Caluclate Shannon entropy
    entropy = -sum(p * np.log2(p) for p in probabilities)

    # Assert the entropy meets the threshold
    threshold = 13
    assert entropy > threshold, f'Test fails entropy_measurement. Entropy: {entropy:.5f}, Threshold: {threshold}'
    
def test_chi_square_goodness(prng_method):
    prng_output = [prng_method() for _ in range(10000)]
    observed, bins = np.histogram(prng_output, bins=20)
    expected = [len(prng_output) / 20] * 20 #Uniform distribution

    chi2, p = chisquare(observed, expected)

    assert p > 0.05, f'Chi-Square test failed with p-value: {p}, Chi2: {chi2}'

    
def test_autocorrelation(prng_method):
    prng_output = np.array([prng_method() for _ in range(100000)])
    lags = [1, 2, 5, 10]
    threshold = 0.1

    for lag in lags:
        correlation = np.corrcoef(prng_output[:-lag], prng_output[lag:])[0, 1]
        assert abs(correlation) < threshold, (
            f'Autocorrelation test failed (lag {lag}): '
            f'Correlation = {correlation:.5f}, Threshold = {threshold}')

def test_periodicity(prng_method):
    prng_output = [prng_method() for _ in range(10000)]
    unique_values = len(set(prng_output))

    assert unique_values == len(prng_output), (
        f'Test fails periodicity check. Number of unique values: {unique_values}'
        f'Total values: {len(prng_output)}')
    
def test_random_letter(prng_instance):
    numerical_values = []
    prng_output = [prng_instance.random_letter() for _ in range(10000)]
    for letter in prng_output:
        numerical_values.append(ord(letter))
    
    # Setting min and max threshold (65 = A, 90 = Z)
    min_threshold = 65
    max_threshold = 90

    assert max(numerical_values) <= max_threshold, (
        'Max value is higher than threshold. '
        f'Max value: {max(numerical_values)} '
        f'Max threshold: {max_threshold}')
    
    assert min(numerical_values) >= min_threshold, (
        'Min value is lower than threshold '
        f'Min value: {min(numerical_values)} '
        f'Min threshold: {min_threshold}')
    
    # Validate all letters are in the expected set
    valid_letters = set(chr(i) for i in range(min_threshold, max_threshold + 1))
    assert all(letter in valid_letters for letter in prng_output), 'Invalid letter generated. '

@pytest.mark.parametrize('min_value', [0, 10, 50, 100])
@pytest.mark.parametrize('max_value', [20, 50, 100, 1000])
def test_integer_parameters(prng_method, min_value, max_value):
    if min_value >= max_value:
        pytest.skip(f'Skipping invalid combination: min_value={min_value}, max_value={max_value}')
    prng_output = [prng_method(min_value=min_value, max_value=max_value) for _ in range(10000)]
    for number in prng_output:
        assert number >= min_value, (
            'Output is lower than minimum value '
            f'Min value expected: {min_value} '
            f'Actual value: {number}'
        )
        assert number <= max_value, (
            'Output is higher than maximum value '
            f'Max value expected: {max_value} '
            f'Actual value: {number} '
        )
@pytest.mark.parametrize('min_letter', ['A', 'D', 'K', 'M'])
@pytest.mark.parametrize('max_letter', ['N', 'P', 'S', 'Z'])
def test_letter_parameters(prng_instance, min_letter, max_letter):
    if ord(min_letter) > ord(max_letter):
        pytest.skip(f'Skipping invalid combination: min_letter={min_letter}, max_letter={max_letter}')
    prng_output = [prng_instance.random_letter(min_letter=min_letter, max_letter=max_letter) for _ in range(10000)]
    for letter in prng_output:
        assert letter >= min_letter, (
            'Output is lower than min value '
            f'Min letter expected: {min_letter} '
            f'Actual letter: {letter}'
        )

        assert letter <= max_letter, (
            'Output is higher than max value '
            f'Max letter expected: {max_letter} '
            f'Actual letter: {letter}'
        )

def test_performance(prng_method, benchmark):
    @benchmark
    def generate_random_values():
        return [prng_method() for _ in range(10000)]
