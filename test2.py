import numpy as np

def tone_with_noise(fc, fs=48000, duration=3.0, noise_level=0.1):
    """
    Genera un tono senoidal en frecuencia fc con ruido añadido.

    fc: frecuencia del tono (Hz)
    fs: frecuencia de muestreo (Hz)
    duration: duración en segundos
    noise_level: nivel de ruido (0 = sin ruido, 1 = solo ruido)

    Retorna:
      signal: arreglo float32 para Audio(...)
      fs: frecuencia de muestreo
    """

    t = np.linspace(0, duration, int(fs * duration), endpoint=False)

    # Tono puro
    tone = np.sin(2 * np.pi * fc * t)

    # Ruido blanco
    noise = np.random.randn(len(t))

    # Mezcla ajustada
    s = (1 - noise_level) * tone + noise_level * noise

    # Normalizar
    s = s / np.max(np.abs(s))

    return s.astype(np.float32), fs
from IPython.display import Audio, display

for fc in [3000, 5000, 8000, 10000, 12000]:
    print(f"Tono con ruido en {fc} Hz")
    s, fs = tone_with_noise(fc, noise_level=0.15)
    display(Audio(s, rate=fs))
