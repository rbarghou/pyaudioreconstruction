import lws
import librosa
import numpy as np


def griffin_lim_step(spectrogram, audio, hop_length, n_fft):
    """

    :param spectrogram:
    :param audio:
    :param hop_length:
    :param n_fft:
    :return:
    """
    D = librosa.stft(audio, hop_length=hop_length, n_fft=n_fft)
    D *= np.abs(spectrogram) / np.abs(D)
    return librosa.istft(D, hop_length=hop_length)


def griffin_lim_iterator(spectrogram, audio, hop_length, n_fft, num_steps=10):
    """

    :param spectrogram:
    :param audio:
    :param hop_length:
    :param n_fft:
    :param num_steps:
    :return:
    """
    _audio = audio
    yield _audio
    for _ in range(num_steps):
        _audio = griffin_lim_step(spectrogram, _audio, hop_length, n_fft)
        yield _audio


def griffin_lim(spectrogram, audio, hop_length, n_fft, num_steps=10):
    """
    :param spectrogram:
    :param audio:
    :param hop_length:
    :param n_fft:
    :param num_steps:
    :return:
    """
    for _audio in griffin_lim_iterator(spectrogram, audio, hop_length, n_fft, num_steps=num_steps):
        pass
    return _audio


def reconstruct(spectrogram, audio=None, hop_length=512, n_fft=2048, num_steps=10):
    if not audio:
        lws_processor = lws.lws(n_fft, hop_length, mode="music")
        D = lws_processor.run_lws(spectrogram.T.astype(np.double)).T
        audio = librosa.istft(D, hop_length=hop_length)
    return griffin_lim(spectrogram, audio, hop_length, n_fft, num_steps)


def error(spectrogram, audio, hop_length=512, n_fft=2048, mode="mean"):
    return {
        "mean": np.mean,
        "median": np.median,
        "max": np.max,
    }[mode](
        np.abs(
            np.abs(spectrogram) - np.abs(librosa.stft(audio, hop_length=hop_length, n_fft=n_fft))
        )
    )

