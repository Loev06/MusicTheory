from wav_writer import WavWriter

def sinwave(frequency: float, samplerate: int, duration: float, amplitude: float = 1.0, phase: float = 0.0):
    import math
    num_samples = int(samplerate * duration)
    samples = []
    for n in range(num_samples):
        t = n / samplerate
        sample = amplitude * math.sin(2 * math.pi * frequency * t + phase)
        samples.append([sample])
    return samples

def main():
    writer = WavWriter(44100, 1, 16)
    
    # Start from A4 (440 Hz) and go up by half steps
    samples = []
    freq = 440.0
    for i in range(12):
        samples += sinwave(int(freq), 44100, 0.3, amplitude=0.1)
        # Increase frequency by a half step
        freq *= 2 ** (1/12)
    samples += sinwave(int(freq), 44100, 1.2, amplitude=0.1)  # Add the last note

    for sample in samples:
        writer.write(sample)
    writer.save("output.wav")

if __name__ == "__main__":
    main()