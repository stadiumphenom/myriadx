# engineform.py
from engines.enginecore import MyriadBaseEngine

class MyriadFormEngine(MyriadBaseEngine):
    def _generate_keywords(self):
        return ["structure", "symmetry pulse", "fossil pattern", "dream logic"]

    def _calculate_intensity(self):
        return round(0.7 + self.drift_factor * 1.2, 2)
