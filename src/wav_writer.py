def little_endian(value, length):
    if value < 0:
        value = (1 << (length * 8)) + value
    return value.to_bytes(length, 'little')

class WavWriter:
    samplerate: int
    channels: int
    bitdepth: int
    data: bytearray

    def __init__(self, samplerate: int, channels: int, bitdepth: int):
        self.samplerate = samplerate
        self.channels = channels
        self.bitdepth = bitdepth
        self.data = bytearray()

    def write(self, sample: list[float]):
        for channel in sample:
            # Clamp to [-1.0, 1.0]
            channel = max(-1.0, min(1.0, channel))
            # Scale to PCM range
            scaled = int(channel * (2 ** (self.bitdepth - 1) - 1))
            # Write to data
            self.data.extend(little_endian(scaled, self.bitdepth // 8))

    def save(self, filename: str):
        subchunk2_size = len(self.data)
        byte_rate = self.samplerate * self.channels * self.bitdepth // 8
        block_align = self.channels * self.bitdepth // 8

        with open(filename, 'wb') as f:
            # Write WAV header
            # http://soundfile.sapp.org/doc/WaveFormat/
            
            # RIFF chunk descriptor
            # ChunkID
            f.write(b'RIFF')
            # ChunkSize
            f.write(little_endian(36 + subchunk2_size, 4))
            # Format
            f.write(b'WAVE')

            # fmt subchunk
            # Subchunk1ID
            f.write(b'fmt ') # note the space
            # Subchunk1Size
            f.write(little_endian(16, 4))
            # AudioFormat
            f.write(little_endian(1, 2))
            # NumChannels
            f.write(little_endian(self.channels, 2))
            # SampleRate
            f.write(little_endian(self.samplerate, 4))
            # ByteRate
            f.write(little_endian(byte_rate, 4))
            # BlockAlign
            f.write(little_endian(block_align, 2))
            # BitsPerSample
            f.write(little_endian(self.bitdepth, 2))

            # data subchunk
            # Subchunk2ID
            f.write(b'data')
            # Subchunk2Size
            f.write(little_endian(subchunk2_size, 4))
            # Data
            f.write(self.data)
