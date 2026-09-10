import math
from client import HilbertTransformEngine

def main():
    print("=== Testing Hilbert Transform & Analytic Signal ===")
    hilb = HilbertTransformEngine()
    sig = [math.sin(2 * math.pi * 0.1 * i) for i in range(16)]
    z, env, phase = hilb.analytic_signal(sig)
    print("Envelope magnitudes:", [round(e, 3) for e in env])
    assert len(env) == 16
    assert all(e >= 0 for e in env)
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
