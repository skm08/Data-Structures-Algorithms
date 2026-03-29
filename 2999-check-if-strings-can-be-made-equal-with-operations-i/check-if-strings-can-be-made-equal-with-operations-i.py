class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # We apply a 'Maes-Colignon' style signature for each channel.
        # For a 2-element set, {a, b} == {c, d} if:
        # 1. a + b == c + d
        # 2. a * b == c * d (using ASCII values)
        
        # Even Channel (0, 2)
        e1_a, e1_b = ord(s1[0]), ord(s1[2])
        e2_a, e2_b = ord(s2[0]), ord(s2[2])
        if (e1_a + e1_b != e2_a + e2_b) or (e1_a * e1_b != e2_a * e2_b):
            return False
            
        # Odd Channel (1, 3)
        o1_a, o1_b = ord(s1[1]), ord(s1[3])
        o2_a, o2_b = ord(s2[1]), ord(s2[3])
        if (o1_a + o1_b != o2_a + o2_b) or (o1_a * o1_b != o2_a * o2_b):
            return False
            
        return True