"""Lit un pom.xml (XML) et génère un workflow GitHub Actions (YAML).
Usage : python scripts/pom_to_workflow.py [pom.xml] [sortie.yml]
Utilise uniquement la bibliothèque standard (xml.etree)."""
import sys
import xml.etree.ElementTree as ET

NS = {"m": "http://maven.apache.org/POM/4.0.0"}

def texte(noeud, chemin):
    el = noeud.find(chemin, NS)
    return el.text.strip() if el is not None and el.text else None

def lire_pom(chemin):
    racine = ET.parse(chemin).getroot()
    deps = [{"groupId": texte(d, "m:groupId"),
             "artifactId": texte(d, "m:artifactId"),
             "version": texte(d, "m:version"),
             "scope": texte(d, "m:scope") or "compile"}
            for d in racine.findall("m:dependencies/m:dependency", NS)]
    return {"artifactId": texte(racine, "m:artifactId"),
            "version": texte(racine, "m:version"),
            "java": texte(racine, "m:properties/m:maven.compiler.release") or "17",
            "deps": deps}

def generer_yaml(pom):
    lignes = [
        f"# Généré automatiquement depuis pom.xml ({pom['artifactId']} {pom['version']})",
        "# Dépendances détectées :",
    ]
    lignes += [f"#   - {d['groupId']}:{d['artifactId']}:{d['version']} ({d['scope']})"
               for d in pom["deps"]] or ["#   (aucune)"]
    lignes += [
        f"name: CI {pom['artifactId']}",
        "on:",
        "  push:",
        "    branches: [main]",
        "  pull_request:",
        "jobs:",
        "  build:",
        "    runs-on: ubuntu-latest",
        "    steps:",
        "      - uses: actions/checkout@v4",
        "      - uses: actions/setup-java@v4",
        "        with:",
        "          distribution: temurin",
        f"          java-version: '{pom['java']}'",
        "          cache: maven",
        "      - name: Build et tests",
        "        run: mvn -B verify",
    ]
    return "\n".join(lignes) + "\n"

if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "pom.xml"
    dst = sys.argv[2] if len(sys.argv) > 2 else ".github/workflows/ci.yml"
    contenu = generer_yaml(lire_pom(src))
    with open(dst, "w", encoding="utf-8") as f:
        f.write(contenu)
    print(f"Workflow généré : {dst}\n")
    print(contenu)
