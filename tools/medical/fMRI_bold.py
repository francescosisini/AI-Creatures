import numpy as np
import matplotlib.pyplot as plt

# ---- INPUT PARAMETRI ----
PA = 2    # Positive Affect (0-10)
NA = 7    # Negative Affect (0-10)

stim_visivo    = True   # Stimolo visivo ON/OFF
stim_motorio   = False  # Stimolo motorio ON/OFF
stim_memoria   = False   # Stimolo mnemonico ON/OFF
stim_emozioni  = False  # Stimolo emozionale ON/OFF

stim_start = 8
stim_end = 13

# ---- TIME ----
t = np.linspace(0, 30, 300)
stim_on = (t >= stim_start) & (t <= stim_end)

# ---- RISPOSTA BOLD GENERICA (gaussiana) ----
def response(t, amp, center, width):
    return amp * np.exp(-0.5 * ((t - center) / width) ** 2)

# ---- LOGICA REGIONI ----
bold_amigdala = 0.2 + 0.2 * (NA / 10)
if stim_emozioni:
    bold_amigdala += response(t, 0.7 * (NA / 10 + 0.3), stim_start + 2, 2.4)
bold_amigdala += 0.07 * np.random.randn(len(t))

bold_prefront = 0.21 + 0.21 * (PA / 10)
if stim_emozioni:
    bold_prefront += response(t, 0.6 * (PA / 10 + 0.2), stim_start + 2, 3.2)
if stim_memoria:
    bold_prefront += response(t, 0.25, stim_start + 2.5, 3.7)
bold_prefront += 0.07 * np.random.randn(len(t))

bold_motoria = 0.19
if stim_motorio:
    bold_motoria += response(t, 0.55, stim_start + 2, 2.2)
bold_motoria += 0.05 * np.random.randn(len(t))

bold_ippocampo = 0.18 + 0.1 * ((PA + NA) / 20)
if stim_memoria:
    bold_ippocampo += response(t, 0.6 * ((PA + NA) / 20 + 0.2), stim_start + 2, 3.0)
bold_ippocampo += 0.06 * np.random.randn(len(t))

bold_visiva = 0.16
if stim_visivo:
    bold_visiva += response(t, 0.44, stim_start + 2, 1.8)
bold_visiva += 0.045 * np.random.randn(len(t))

# ---- PLOT ----
plt.figure(figsize=(11, 5))
plt.axvspan(stim_start, stim_end, color='yellow', alpha=0.15, label='Stimolo')
plt.plot(t, bold_amigdala,   color='firebrick', label='Amigdala (emozioni/NA)')
plt.plot(t, bold_prefront,   color='navy', label='Prefrontale (regolazione/PA, memoria)')
plt.plot(t, bold_motoria,    color='green', label='Motoria')
plt.plot(t, bold_ippocampo,  color='slateblue', label='Ippocampo (memoria/emozioni)')
plt.plot(t, bold_visiva,     color='orange', label='Visiva (stimolo)')

plt.title(
    f"Simulazione fMRI - Risposta BOLD multi-regione\n"
    f"(PA={PA}, NA={NA}, "
    f"Visivo={'ON' if stim_visivo else 'OFF'}, "
    f"Motorio={'ON' if stim_motorio else 'OFF'}, "
    f"Memoria={'ON' if stim_memoria else 'OFF'}, "
    f"Emozioni={'ON' if stim_emozioni else 'OFF'})"
)
plt.xlabel("Tempo (s)")
plt.ylabel("Segnale BOLD (a.u.)")
plt.legend(loc='upper right', framealpha=0.93)
plt.tight_layout()
plt.savefig("fmri_bold_multiregione_parametrico.svg", format="svg")
plt.show()
