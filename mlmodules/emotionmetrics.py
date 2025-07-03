# emotionmetrics.py
# Analyze emotion vector consistency and detect drift patterns

def compute_emotional_drift(prev_vec, curr_vec):
    """
    Given two emotional vectors (dicts), compute a scalar drift score.
    """
    keys = set(prev_vec.keys()) & set(curr_vec.keys())
    diffs = [abs(prev_vec[k] - curr_vec[k]) for k in keys if isinstance(prev_vec[k], (int, float))]
    return round(sum(diffs) / len(diffs), 3) if diffs else 0.0

def summarize_emotion_vector(vec):
    """
    Print a compact summary for debugging or logging.
    """
    summary = {k: round(v, 2) for k, v in vec.items() if isinstance(v, (int, float))}
    return f"Emotion Snapshot: {summary}"
