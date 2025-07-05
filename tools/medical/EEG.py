import numpy as np
import matplotlib.pyplot as plt

# --- Parametri PANAS (modifica qui) ---
PA = 2  # Positive Affect (0-10)
NA = 7  # Negative Affect (0-10)

# --- Parametri EEG ---
durata = 2
fs = 250
t = np.arange(0, durata, 1/fs)

def generate_band(freq, amp, phase=0):
    return amp * np.sin(2 * np.pi * freq * t + phase)

# --- Bande (5 classiche) ---
delta = generate_band(2,   (PA / 10) * 0.5 + (NA / 10) * 0.2)
theta = generate_band(6,   (NA / 10) * 0.4 + (PA / 10) * 0.2, phase=np.pi/2)
alpha = generate_band(10,  (PA / 10) * 1.0)
beta  = generate_band(20,  (NA / 10) * 0.7, phase=np.pi/4)
gamma = generate_band(40,  (NA / 10) * 0.5 + (PA / 10) * 0.2, phase=np.pi/3)

# --- Rumore ---
noise = 0.1 * np.random.randn(len(t))

# --- Segnale totale ---
eeg_signal = delta + theta + alpha + beta + gamma + noise

# --- Calcolo della potenza (varianza) di ciascuna banda ---
def power(y):
    return np.mean(y ** 2)

P_delta = power(delta)
P_theta = power(theta)
P_alpha = power(alpha)
P_beta  = power(beta)
P_gamma = power(gamma)

# --- Rapporti tra bande ---
theta_beta = P_theta / P_beta if P_beta else np.nan
alpha_beta = P_alpha / P_beta if P_beta else np.nan
theta_alpha = P_theta / P_alpha if P_alpha else np.nan
delta_alpha = P_delta / P_alpha if P_alpha else np.nan

# --- Valutazione dello stato emotivo/cognitivo in base ai ratios ---
def valutazione(theta_beta, alpha_beta, theta_alpha, delta_alpha):
    # Esempi di soglie indicative, ispirate alla letteratura
    if theta_beta > 4:
        return "Stato di possibile distrazione, sonnolenza o basso controllo esecutivo (Theta/Beta ↑)"
    elif theta_beta < 2 and alpha_beta < 1:
        return "Stato di attivazione mentale intensa o stress (Theta/Beta ↓, Alpha/Beta ↓)"
    elif alpha_beta > 2 and theta_beta < 3:
        return "Stato di rilassamento vigile, meditazione o benessere (Alpha/Beta ↑)"
    elif delta_alpha > 1.5:
        return "Predominanza di attività lenta: sonno, stanchezza o deterioramento"
    else:
        return "Stato intermedio o non specifico. Valori nei range di normalità."

valutazione_testo = valutazione(theta_beta, alpha_beta, theta_alpha, delta_alpha)

# --- Plot solo il segnale totale e stampa ratio ---
plt.figure(figsize=(12,4))
plt.plot(t, eeg_signal, color='purple')
plt.title(f'Simulazione EEG totale (PA={PA}, NA={NA})')
plt.xlabel('Tempo (s)')
plt.ylabel('Ampiezza (a.u.)')
plt.xlim(0, durata)
plt.grid(True)

# Prepara il testo con i rapporti principali
ratios_text = (
    f"Theta/Beta: {theta_beta:.2f}\n"
    f"Alpha/Beta: {alpha_beta:.2f}\n"
    f"Theta/Alpha: {theta_alpha:.2f}\n"
    f"Delta/Alpha: {delta_alpha:.2f}"
)

# Box con i ratio in alto a destra
plt.gca().text(
    0.98, 0.98, ratios_text,
    transform=plt.gca().transAxes,
    fontsize=12, fontfamily='monospace',
    verticalalignment='top', horizontalalignment='right',
    bbox=dict(boxstyle='round', facecolor='white', alpha=0.85, edgecolor='gray')
)

# Box con la valutazione sotto i ratios
plt.gca().text(
    0.98, 0.68, valutazione_testo,
    transform=plt.gca().transAxes,
    fontsize=12, fontfamily='sans-serif',
    verticalalignment='top', horizontalalignment='right',
    bbox=dict(boxstyle='round', facecolor='#eef8fc', alpha=0.92, edgecolor='gray')
)

plt.tight_layout()
plt.savefig("tracciato_eeg_totale_con_valutazione.svg", format="svg")
plt.close()

print("\nGrafico salvato in 'tracciato_eeg_totale_con_valutazione.svg'")
print("Valutazione sintetica:", valutazione_testo)
