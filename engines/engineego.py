# engine_ego.py
from engines.enginecore import MyriadBaseEngine

class MyriadEgoEngine(MyriadBaseEngine):
    def _generate_keywords(self):
        return ["dissolve", "oneness", "lightwave", "transcend"]

    def _calculate_intensity(self):
        return round(0.75 + self.drift_factor * 2, 2)
