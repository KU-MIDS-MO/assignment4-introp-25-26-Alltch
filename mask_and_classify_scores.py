import numpy as np

def mask_and_classify_scores(arr):
    if not isinstance(arr, np.ndarray):
        return None
    if arr.ndim != 2:
        return None
    n_rows, n_cols = arr.shape
    if n_rows != n_cols or n_rows < 4:
        return None
    n = n_rows 
    cleaned = np.clip(arr, 0, 100)
    levels = np.zeros_like(cleaned, dtype=int)
    medium_mask = (cleaned >= 40) & (cleaned < 70)
    levels[medium_mask] = 1
    high_mask = cleaned >= 70
    levels[high_mask] = 2
    row_pass_counts = np.zeros(n, dtype=int)

    for i in range(n):
        count = 0
        for value in cleaned[i]:
            if value >= 50:
                count += 1
        row_pass_counts[i] = count

    return (cleaned, levels, row_pass_counts)