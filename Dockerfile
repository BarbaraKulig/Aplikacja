# Użyj obrazu bazowego Pythona
FROM python:3.8-slim

# Ustaw katalog roboczy w kontenerze
WORKDIR /app

# Skopiuj zawartość katalogu aktualnego do kontenera w katalogu /app
COPY . /app

# Zainstaluj Personal Assistant oraz zależności
RUN pip install personal_assistant

ENTRYPOINT ["python", "aplikacja.py"]

# Określ, co ma być wykonywane po uruchomieniu kontenera
CMD ["bash"]