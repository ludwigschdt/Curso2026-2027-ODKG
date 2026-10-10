import os
from pathlib import Path

import morph_kgc

group_dir = Path(__file__).resolve().parent.parent
rdf_dir = group_dir / "rdf"

# Les chemins du config.ini sont relatifs à Group07
os.chdir(group_dir)

graph = morph_kgc.materialize("transformation/config.ini")

rdf_dir.mkdir(exist_ok=True)

graph.serialize(
    destination=str(rdf_dir / "knowledge-graph.nt"),
    format="nt",
)

graph.serialize(
    destination=str(rdf_dir / "knowledge-graph.ttl"),
    format="turtle",
)

print(f"Generated {len(graph)} triples")