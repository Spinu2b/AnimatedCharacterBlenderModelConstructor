

class FloatComparisonHelper:
    @classmethod
    def is_equal(cls, float_a: float, float_b: float):
        return abs(float_a - float_b) < 0.0000001
