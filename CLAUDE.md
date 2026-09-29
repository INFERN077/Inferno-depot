# Consignes permanentes

## Génération de scripts YouTube

Ces consignes s'appliquent à chaque script demandé, qu'il soit écrit avec le prompt de scénariste (PDF fourni ou `prompts/prompt-script-youtube-sans-visage.md`) ou sans. Elles priment sur le format de sortie de ce prompt.

**Ce qui est livré : uniquement le script final.** Le texte de la voix off, prêt à être doublé tel quel par une voix IA. Il n'y a aucun retouchage après.

- Recherche, plan, accroches, révision : faits en interne, jamais livrés. Pas de fiche de préparation, de banque de faits, de rapport de révision, d'auto-audit ni de liste de sources.
- Dans la réponse : le script complet, puis au plus une ligne pour dire où il est enregistré. Pas de résumé ni de briefing.
- Enregistrer le script dans `scripts/<titre-en-minuscules-avec-tirets>.txt`, puis committer et pousser.

**Format du texte (lu directement par une voix IA) :**

- Uniquement la narration : pas de titre, de timecodes, d'indications visuelles, sonores ou de ton, de crochets, de notes ni de markdown.
- Nombres, dates et pourcentages écrits en toutes lettres (« trois virgule quatre pour cent », « deux mille vingt-six »). Aucun symbole (%, €, /, &).
- Sigles : garder ceux qui s'épellent (ETF, PEA, LVMH). Écrire comme un mot ceux qui se prononcent comme un mot (« Cac quarante »). Éviter ceux qu'une voix IA lit mal (KO…) et les noms étrangers difficiles à prononcer quand on peut s'en passer.
- Pauses : uniquement avec la ponctuation (points, points de suspension).
- Aucune référence à l'image (« à l'écran », « comme tu peux le voir ») : la narration se suffit à elle-même.
- Pas de pont vers une autre vidéo, sauf si elle est fournie.

**Fiabilité (pas de relecture humaine) :**

- Aucun marqueur [À VÉRIFIER] ou [INFO MANQUANTE] dans le texte livré. Chaque fait est vérifié dans une source fiable pendant la recherche. Un fait incertain est retiré, ou formulé prudemment (« environ », « on raconte »).
- Un calcul maison est présenté comme tel (« on a fait une simulation »), avec ses hypothèses principales dites dans la narration.
