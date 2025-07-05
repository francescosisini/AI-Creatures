import numpy as np
import matplotlib.pyplot as plt


def ecg_pqrst(t, fs, pa=30, na=20):
    ecg = np.zeros_like(t)
    base_bpm = 70
    freq = base_bpm + (na-20)*1.5 - (pa-20)*0.5  # bpm
    beat_len = 60 / freq
    # Ampiezza onda T: PA ↑ = T ↑, NA ↑ = T ↓
    t_amp = 0.2 + 0.012*(pa-20) - 0.008*(na-20)
    t_amp = max(0.05, t_amp)
    # Picco R: NA ↑ = R ↑
    r_amp = 1 + 0.04*(na-20)
    duration = t[-1]
    nbeats = int(duration / beat_len)
    for i in range(nbeats):
        beat_start = i * beat_len
        p_time = beat_start + 0.1 * beat_len
        p_width = 0.04 * beat_len
        ecg += np.exp(-((t-p_time)/p_width)**2)*0.1
        q_time = beat_start + 0.22 * beat_len
        q_width = 0.015 * beat_len
        ecg -= np.exp(-((t-q_time)/q_width)**2)*0.18
        r_time = beat_start + 0.24 * beat_len
        r_width = 0.008 * beat_len
        ecg += np.exp(-((t-r_time)/r_width)**2)*r_amp
        s_time = beat_start + 0.27 * beat_len
        s_width = 0.012 * beat_len
        ecg -= np.exp(-((t-s_time)/s_width)**2)*0.3
        t_time = beat_start + 0.4 * beat_len
        t_width = 0.045 * beat_len
        ecg += np.exp(-((t-t_time)/t_width)**2)*t_amp
    return ecg, freq

def plot_ecg_pa_na_svg(pa, na, duration=4):
    fs = 500
    t = np.linspace(0, duration, int(fs*duration))
    ecg,freq = ecg_pqrst(t, fs, pa=pa, na=na)
    plt.figure(figsize=(10,2.5))
    plt.plot(t, ecg, color='#c00', linewidth=2)
    plt.title(f"ECG f={freq} PANAS: PA={pa} NA={na}")
    plt.axis('off')
    plt.tight_layout()
    fname = f"ecg_panas_pa{pa}_na{na}.svg"
    plt.savefig(fname, bbox_inches='tight', pad_inches=0, transparent=True, format='svg')
    plt.close()
    print(f"Salvato SVG come {fname}")

# Esempi:
#plot_ecg_pa_na_svg(pa=36, na=12)  # Relax, energia positiva
#plot_ecg_pa_na_svg(pa=8, na=34)   # Ansia, tensione, nervosismo
#plot_ecg_pa_na_svg(pa=22, na=22)  # Stato neutro

plot_ecg_pa_na_svg(pa=12, na=31)  
