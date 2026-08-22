import json
import os

# Chemins des fichiers
csv_input_path = "C:\\Users\\l.baduet\\Downloads\\metadata.csv" # Remplacez par le nom de votre fichier CSV
jsonl_output_path = "my_data_train.jsonl"      # Le fichier de sortie demandé

# Dossier de base à ajouter devant le chemin audio si nécessaire (laisser vide si non requis)
base_audio_dir = "data/audio/" # Ajustez selon votre configuration

with open(csv_input_path, "r", encoding="utf-8") as f_in, \
     open(jsonl_output_path, "w", encoding="utf-8") as f_out:
    
    for index, line in enumerate(f_in, start=1):
        line = line.strip()
        if not line:
            continue
            
        # Découpage de la ligne par le séparateur '|'
        parts = line.split("|")
        if len(parts) >= 3:
            audio_rel_path = parts[0].strip().split("/")[1]
            text_val = parts[1].strip()
            # ref_text_val = parts[2].strip() # Si vous en avez besoin plus tard
            
            # Construction de l'ID unique (ex: sample_001)
            sample_id = f"sample_{index:03d}"
            
            # Construction du chemin complet de l'audio
            audio_full_path = os.path.join(base_audio_dir, audio_rel_path)
            
            # Création du dictionnaire pour la ligne JSON
            data = {
                "id": sample_id,
                "audio_path": audio_full_path,
                "text": text_val,
                "language_id": "bas"
            }
            
            # Écriture de la ligne au format JSONL dans le fichier de sortie
            f_out.write(json.dumps(data, ensure_ascii=False) + "\n")

print(f"Conversion terminée ! Fichier enregistré sous : {jsonl_output_path}")