# pyaudioreconstruction
Audio reconstruction from spectrogram

# Overview
Audio data is often presented in the form of an absolute spectrogram, but this usually omits much data regarding phase that is used in reconstructing the original audio.  This is increasingly true in the python world as more python programmers are interested in using image processing techniques to modify spectrograms.

Consiquently a need arose for a simple method to recover approximations of a waveform that matches a spectrogram, even if that spectrogram is missing the phase data.

# Approach
Two conventional approaches are combined in this library to provide a reasonably high quality reconstruction, Locally Weighted Sums and the Griffin Lim algorithm.  The combination of these two approaches produces a reliable reconstruction with an understandable implementation.

As the library grows, I hope to add additional features to make use in realtime settings more reasonable and to make it more paramaterized.
