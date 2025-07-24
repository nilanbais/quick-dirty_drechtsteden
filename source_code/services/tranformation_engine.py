"""
File met het object verantwoordelijk voor het 'aan elkaar knopen' van de stappen in de automatisering.

stappen die doorlopen worden:
1. inlezen van de input data vóó de aggregatie.
2. aggregeren van de data over een periode van 1 dag (elke dag is 1 record).
3. toevoegen van de nieuwe records aan de output (dashboard dataset).
"""

class TransformationEngine:

    def run_transformations() -> None:
        print("Lege functie => Fictief uitvoeren van transformatie.")