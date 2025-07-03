# enginecore.py
# Shared abstract base class for Myriad simulation engines

class MyriadBaseEngine:
    def __init__(self, emotion="ego-loss", sim_count=10000, drift_factor=0.1):
        self.emotion = emotion
        self.sim_count = sim_count
        self.drift_factor = drift_factor

    def generate_frame_data(self):
        return {
            "emotion": self.emotion,
            "sim_count": self.sim_count,
            "entropy": self.drift_factor,
            "keywords": self._generate_keywords(),
            "intensity": self._calculate_intensity()
        }

    def _generate_keywords(self):
        return ["memory", "void", "pulse", "fractal"]

    def _calculate_intensity(self):
        return round(0.5 + self.drift_factor * 1.5, 2)
