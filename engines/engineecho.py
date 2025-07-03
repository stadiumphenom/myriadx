# engine_echo.py
from engines.enginecore import MyriadBaseEngine

class MyriadEchoEngine(MyriadBaseEngine):
    def _generate_keywords(self):
        return ["reverb", "afterglow", "ghost", "hollow harmony"]

    def _calculate_intensity(self):
        return round(0.6 + self.drift_factor * 1.8, 2)
