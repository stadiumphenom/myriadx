# enginedrift.py
from engines.enginecore import MyriadBaseEngine

class MyriadDriftEngine(MyriadBaseEngine):
    def _generate_keywords(self):
        return ["chaotic shimmer", "warpfield", "signal scatter", "unstable bloom"]

    def _calculate_intensity(self):
        return round(0.4 + self.drift_factor * 2.5, 2)
