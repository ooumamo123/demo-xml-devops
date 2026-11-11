# Démo : XML dans le build (Ant -> Maven -> CI/CD)

## Prérequis : JDK 21, Ant, Maven, Git, Python 3

## Étape 1 : Ant
    .\telecharger-junit.ps1
    ant test
    ant jar
    java -jar build-ant/calculatrice.jar

## Étape 2 : Maven
    mvn test
    mvn package
    java -jar target/calculatrice-1.0.0.jar

## Étape 3 : pom.xml -> workflow GitHub Actions
    python scripts/pom_to_workflow.py
    git add . ; git commit -m "demo" ; git push
(le workflow se lance sur l'onglet Actions de GitHub)
