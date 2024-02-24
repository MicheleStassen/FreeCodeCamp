import numpy as np

def calculate(lists):
    if len(lists)==9:
        matrix = np.array(lists).reshape(3,3)
    
        m_mean = [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean()]
        m_variance = [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var()]
        m_std = [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std()]
        m_max = [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max()]
        m_min = [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min()]
        m_sum = [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum()]
    
        calculations = {
            "mean": m_mean,
            "variance": m_variance,
            "standard deviation": m_std,
            "max": m_max,
            "min": m_min,
            "sum": m_sum
        }
    else:
        raise ValueError('List must contain nine numbers.')

    return calculations
