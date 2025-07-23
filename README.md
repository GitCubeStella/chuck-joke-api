# 🐳 Chuck Norris Joke API
![CI Status](https://github.com/gitcubestella/chuck-joke-api/actions/workflows/docker-build.yml/badge.svg)

Ein Docker-basiertes Python-Flask-Projekt, das zufällige Chuck-Norris-Witze von einer öffentlichen API zurückliefert – automatisch gebaut & deployed via GitHub Actions.

---

## 📦 Image aus der GitHub Container Registry (GHCR) ziehen

```bash
docker pull ghcr.io/gitcubestella/chuck-joke-api:latest

🚀 Container starten

docker run -p 5000:5000 ghcr.io/gitcubestella/chuck-joke-api:latest

➡️ Danach im Browser öffnen:
http://localhost:5000/joke

Beispielausgabe:
{
  "joke": "Chuck Norris can divide by zero."
}

🛠 Entwickeln & lokal testen
# Installiere Abhängigkeiten
pip install -r requirements.txt

# Starte die App
python app.py

🔄 GitHub Actions CI/CD
Diese App wird automatisch gebaut und als Container-Image veröffentlicht mit jedem Commit auf main.

📦 Registry-Link:
https://github.com/users/gitcubestella/packages

🧠 Tech Stack:
- Python 3.11
- Flask
- GitHub Actions
- Docker
- GHCR (GitHub Container Registry)

📬 Kontakt
Entwickelt mit ☕ und 💥 von @GitCubeStella

🛡 Lizenz
MIT License – feel free to fork & have fun.


---

## ✅ Als Nächstes:

1. Erstelle die Datei `README.md` in deinem Projektordner
2. Inhalt einfügen
3. Commit & push:

```bash
git add README.md
git commit -m "Add README with usage instructions"
git push origin main


