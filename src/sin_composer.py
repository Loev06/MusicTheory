from note import Note

class SinComposer:
    current_frequencies: list[Note]
    sample_rate: int

    def __init__(self, sample_rate: int = 44100):
        self.current_frequencies = []
        self.sample_rate = sample_rate

    def add_note(self, frequency: float, amplitude: float, duration: float, phase: float = 0.0):
        note = Note(frequency, duration, amplitude, phase, self.sample_rate)
        self.current_frequencies.append(note)

    def sample(self) -> float:
        return sum(note.next_sample() for note in self.current_frequencies)
