import numpy as np
# Generate synthetic coherence scores
np.random.seed(42)
version_a_scores = np.random.normal(6, 1, 100)  # Mean = 6, Std = 1
version_b_scores = np.random.normal(7, 1, 100)  # Mean = 7, Std = 1
def permutation_test(scores_a, scores_b, num_permutations=10000):
    observed_diff = np.mean(scores_b) - np.mean(scores_a)
    combined_scores = np.concatenate([scores_a, scores_b])
    count = 0
    
    for _ in range(num_permutations):
        np.random.shuffle(combined_scores)
        new_a = combined_scores[:len(scores_a)]
        new_b = combined_scores[len(scores_a):]
        new_diff = np.mean(new_b) - np.mean(new_a)
        if new_diff >= observed_diff:
            count += 1
    
    p_value = count / num_permutations
    return observed_diff, p_value
observed_diff, p_value = permutation_test(version_a_scores, version_b_scores)
print(f"Observed Difference: {observed_diff}")
print(f"P-value: {p_value}")
def bootstrap_test(scores_a, scores_b, num_bootstraps=10000):
    observed_diff = np.mean(scores_b) - np.mean(scores_a)
    bootstrap_diffs = []
    
    for _ in range(num_bootstraps):
        bootstrap_a = np.random.choice(scores_a, size=len(scores_a), replace=True)
        bootstrap_b = np.random.choice(scores_b, size=len(scores_b), replace=True)
        bootstrap_diff = np.mean(bootstrap_b) - np.mean(bootstrap_a)
        bootstrap_diffs.append(bootstrap_diff)
    
    bootstrap_diffs = np.array(bootstrap_diffs)
    ci_lower = np.percentile(bootstrap_diffs, 2.5)
    ci_upper = np.percentile(bootstrap_diffs, 97.5)
    
    return observed_diff, (ci_lower, ci_upper)
observed_diff, confidence_interval = bootstrap_test(version_a_scores, version_b_scores)
print(f"Observed Difference: {observed_diff}")
print(f"95% Confidence Interval: {confidence_interval}")

