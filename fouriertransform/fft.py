import numpy as np
import scipy.io.wavfile as wav
from scipy.signal import find_peaks
import matplotlib.pyplot as plt
import os
import requests

def download_song(url, filename):
  r = requests.get(url)
  with open(filename, 'wb') as f:
    f.write(r.content)

def get_spectrogram_peaks(audio, samplerate, n_fft=4096, hop_length=2048, peak_threshold=10):
  # Compute spectrogram (magnitude)
  frames = []
  peaks = []
  for start in range(0, len(audio) - n_fft, hop_length):
    window = audio[start:start+n_fft] * np.hanning(n_fft)
    spectrum = np.abs(np.fft.rfft(window))
    # Find peaks in the spectrum
    peak_idxs, _ = find_peaks(spectrum, height=peak_threshold)
    # Save peak frequencies and time
    peaks.append((start / samplerate, peak_idxs))
  return peaks

def build_database(urls):
  db = {}
  os.makedirs("songs", exist_ok=True)
  for i, url in enumerate(urls):
    filename = f'songs/song{i}.wav'
    print(f"Downloading {url}...")
    download_song(url, filename)
    samplerate, audio = wav.read(filename)
    if audio.ndim > 1:
        audio = audio.mean(axis=1)  # convert to mono
    print(f"Extracting peaks for {filename}...")
    peaks = get_spectrogram_peaks(audio, samplerate)
    db[filename] = peaks
  return db

def record_audio(duration=5, samplerate=44100):
  print("Recording...")
  recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
  sd.wait()
  return recording.flatten()

def match_peaks(db, sample_peaks, tolerance=0.5):
  # Naive matching: compare sample peaks with each song peaks by counting matching frequencies at close timestamps
  best_match = None
  best_score = 0

  for song, song_peaks in db.items():
    score = 0
    for t_sample, freqs_sample in sample_peaks:
      for t_song, freqs_song in song_peaks:
        if abs(t_song - t_sample) < tolerance:
          # Count overlapping frequencies
          common = np.intersect1d(freqs_sample, freqs_song)
          score += len(common)
    if score > best_score:
      best_score = score
      best_match = song
  return best_match, best_score

# Example usage:
urls = [
  "https://file-examples-com.github.io/uploads/2017/11/file_example_WAV_1MG.wav",  # sample wav
    # Add your songs here
]

db = build_database(urls)

recorded_audio = record_audio(duration=5)
sample_peaks = get_spectrogram_peaks(recorded_audio, 44100)

match, score = match_peaks(db, sample_peaks)
print(f"Best match: {match} with score {score}")
