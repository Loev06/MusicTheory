from wav_writer import WavWriter
from sin_composer import SinComposer

def main():
    writer = WavWriter(44100, 1, 16)
    composer = SinComposer(44100)
    samples = []

    composer.add_note(440, 0.1, 2.0)  # C5
    samples += [[composer.sample()] for _ in range(44100)]  # 1 second of samples
    composer.add_note(440, 0.1, 2.0, 0.5)  # C5
    samples += [[composer.sample()] for _ in range(44100)]  # 1 second of samples
    samples += [[composer.sample()] for _ in range(44100)]  # 1 second of samples

    for sample in samples:
        writer.write(sample)
    writer.save("output.wav")

if __name__ == "__main__":
    main()