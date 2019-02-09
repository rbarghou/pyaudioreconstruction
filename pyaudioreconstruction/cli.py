import argparse

import librosa
from scipy.misc import imread

from . import reconstruct


parser = argparse.ArgumentParser(
    description=(
        "PyReconstructAudio\n"
        "A python tool for reconstructing audio from a spectrogram image."
    )
)
parser.add_argument("spectrogram_file", help="Spectrogram image file.")
parser.add_argument("hop_length", type=int, help="The hop length between STFT frames")
parser.add_argument("n_ftt", type=int, help="The width of STFT frames")
parser.add_argument("output_file", help="Output audio file .wav format")
parser.add_argument("sample_rate", help="Sample rate of output audio file (and any warm-up audio file)")

parser.add_argument(
    "--audio-file", dest="audio_file", required=False, help="Warm-up audio file. (Griffin Lim only)", default=None)
parser.add_argument(
    "--num-gl-steps", dest="num_steps", required=False, help="Number of times to run Griffin Lim", default=10)


def main():
    args = parser.parse_args()
    spectrogram = imread(args.spectrogram_file, flatten=True)
    audio = None
    if args.audio_file:
        audio, sample_rate = librosa.load(args.audio_file, sr=args.sample_rate)
    reconstructed_audio = reconstruct(
        spectrogram, audio=audio, hop_length=args.hop_length, n_fft=args.n_fft, num_steps=args.num_steps)

    librosa.output.write_wav(args.output_file, reconstructed_audio, sample_rate, norm=True)
