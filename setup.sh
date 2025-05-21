#!/bin/bash

echo "[+] LFI Scanner Setup Script"
echo "[+] Checking Python version..."
python3 --version || { echo "[!] Python3 n'est pas installé."; exit 1; }

echo "[+] Création de l'environnement virtuel..."
python3 -m venv venv
source venv/bin/activate

echo "[+] Installation des dépendances..."
pip install -r requirements.txt

echo "[+] Environnement prêt !"
echo "Pour l'utiliser :"
echo "  source venv/bin/activate"
echo "  python3 scanner.py <URL> <param>"

echo "[+] Fin de l'installation."
