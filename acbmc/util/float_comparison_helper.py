

class FloatComparisonHelper:
    @classmethod
    def is_close_to(cls, float_a: float, float_b: float, tolerance: float=0.0001):
        return abs(float_a - float_b) < tolerance
