import math

class Note:
    frequency: float
    amplitude: float
    phase: float
    sample_rate: int
    t: int
    max_t: int

    def __init__(self, frequency: float, duration: float, amplitude: float, phase: float, sample_rate: int):
        self.frequency = frequency
        self.amplitude = amplitude
        self.phase = phase
        self.t = 0
        self.max_t = int(duration * sample_rate)
        self.sample_rate = sample_rate
    
    def next_sample(self) -> float:
        if self.t >= self.max_t:
            return 0.0

        t = self.t / self.sample_rate
        sample = self.amplitude * math.sin(2 * math.pi * (self.frequency * t + self.phase))
        self.t += 1
        return sample