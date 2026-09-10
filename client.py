import math
import cmath

class CooleyTukeyFFT:
    def fft(self, x):
        n = len(x)
        if n <= 1:
            return x
        even = self.fft(x[0::2])
        odd = self.fft(x[1::2])
        t = [cmath.exp(-2j * math.pi * k / n) * odd[k] for k in range(n // 2)]
        return [even[k] + t[k] for k in range(n // 2)] + [even[k] - t[k] for k in range(n // 2)]

    def ifft(self, x):
        n = len(x)
        x_conj = [z.conjugate() for z in x]
        transformed = self.fft(x_conj)
        return [z.conjugate() / n for z in transformed]

class HilbertTransformEngine:
    """
    Hilbert Transform Engine creating complex analytic signals
    z(t) = x(t) + j*H[x(t)] for instantaneous parameter extraction.
    """
    def __init__(self):
        self.fft_engine = CooleyTukeyFFT()

    def analytic_signal(self, x):
        n = len(x)
        X = self.fft_engine.fft([complex(val, 0) for val in x])
        H = [0j] * n
        H[0] = 1.0
        if n % 2 == 0:
            H[n // 2] = 1.0
            for k in range(1, n // 2):
                H[k] = 2.0
        else:
            for k in range(1, (n + 1) // 2):
                H[k] = 2.0
        Z = [X[i] * H[i] for i in range(n)]
        z = self.fft_engine.ifft(Z)
        envelopes = [abs(val) for val in z]
        instantaneous_phases = [math.atan2(val.imag, val.real) for val in z]
        return z, envelopes, instantaneous_phases
