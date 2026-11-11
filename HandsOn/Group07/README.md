Course 2026-2027-ODKG Group 6
=============================
Group members:
- Numidia Nimhaoulin (numidia17)
- Camille Rouzaud (Marcelo Uliaduz)
- Edgar Barrios (Eddregon)
- Ludwig Schmidt (ludwigschdt)

Our dataset (./csv/DBtrainrides.csv) is too large to upload it on GitHub (772 MB), so we only took the first 1000 lines of it.
The original is available at https://www.kaggle.com/datasets/nokkyu/deutsche-bahn-db-delays.
It is licensed under the MIT-License.

Application setup
-----------------
The application uses GraphDB to host the knowledge graph. GraphDB runs in Docker.

1. Start GraphDB from the `app/` folder:
   ```bash
   cd app
   docker compose up -d
   ```
   The Workbench is then available at http://localhost:7200.

2. Create the repository (only needed once per machine):
   - In the Workbench go to *Setup → Repositories → Create new repository → GraphDB Repository*.
   - Set the **Repository ID** to `db-delays` and keep all other settings at their defaults.

3. Import the data into `db-delays`:
   - Select the repository, go to *Import → Upload RDF files* and upload
     - `ontology/db-delays.ttl`
     - `rdf/knowledge-graph-with-links.ttl`
   - Start the import with the default settings.

The SPARQL endpoint used by the app is http://localhost:7200/repositories/db-delays.
