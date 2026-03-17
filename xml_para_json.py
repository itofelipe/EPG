import xml.etree.ElementTree as ET
import json
from collections import defaultdict

# Caminho do XML de entrada
xml_file = 'guide.xml'

# Parse do XML
tree = ET.parse(xml_file)
root = tree.getroot()

# Dicionário de canais
output = defaultdict(list)

# Percorre todos os elementos "programme"
for programme in root.findall("programme"):
    channel = programme.attrib.get("channel")
    start = programme.attrib.get("start")
    stop = programme.attrib.get("stop")

    title_el = programme.find("title")
    desc_el = programme.find("desc")
    image_el = programme.find("image")

    # Monta o JSON do programa
    entry = {
        "start": start,
        "stop": stop,
        "title": title_el.text if title_el is not None else "",
        "desc": desc_el.text if desc_el is not None else "",
        "image": image_el.text if image_el is not None else ""
    }

    output[channel].append(entry)

# Salva o resultado em JSON
with open('guide.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("✅ Conversão concluída. Arquivo 'saida.json' criado com sucesso.")


""" 
npm run grab --- --channels=meus_canais.channels.xml --output=guide.xml --days=7 --maxConnections=5
datefudge "yesterday" npm run grab --- --channels=meus_canais.channels.xml --output=guide.xml --days=7 --maxConnections=12
python3 xml_para_json.py 
"""