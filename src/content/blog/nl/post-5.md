---
title: "Hoe u een website bouwt met moderne technologie"
meta_title: ""
description: "dit is metabeschrijving"
date: 2025-12-24T10:00:00Z
image: "/images/avatar-astro-dark.png"
categories: ["Web", "Development"]
author: "Steven Reiz"
tags: ["Astro", "VS Code", "WSL"]
draft: false
---

Bij het maken van deze nieuwste versie van de website wilde ik wegblijven van het beproefde (maar vermoeide) gebruik van WordPress. Ik was vooral op zoek naar iets wat meer IDE-vriendelijk was, met inhoud opgeslagen als Markdown- en afbeeldingsbestanden in plaats van in een database. Dit zou de workflow meer developer- en AI-vriendelijk maken. Liefst nog steeds met ondersteuning voor theming en Python-gebaseerde aanpassingen. WYSIWYG-bewerking was geen vereiste, en zou altijd later nog toegevoegd kunnen worden met een van de vele Markdown-gebaseerde CMS-systemen indien nodig.

Na het beoordelen van een groot aantal opties, inclusief enkele low-code / AI-gebaseerde tools, heb ik gekozen voor [Astro](https://astro.build/). Het is wat low-level, maar het is volledig open source en heeft een aantal geweldige startpagina's en thema's beschikbaar. Het integreert goed met een aantal andere front-end technologieën, en het genereert ook nog eens moderne statische websites die erg snel laden en te gebruiken zijn. Het belangrijkste nadeel is dat aanpassingen in Typescript en niet in Python worden gedaan, maar dat is niet onverwacht voor een front-end framework en voor eenvoudige sites niet heel relevant (even afgezien van internationalisatie, dat was nog behoorlijk ingewikkeld om in te bouwen). Tot nu toe is de ervaring met Astro geweldig geweest met snelle ontwikkeling en bewerking door de logische structuur en live preview-functie. Het heeft ook geweldige communityondersteuning.

## Creatief ontwerp

Voor de structuur van de website heb ik een eenvoudig modern ontwerp geselecteerd, goed geschikt voor startups en kleine bedrijven, gericht op één pagina met een header, hero-sectie en voettekst. Enkele kleinere pagina's zijn toegevoegd als ondersteuning, en een blog ten behoeve van uitbreidbaarheid en SEO-mogelijkheden. De [Astroplate](https://astro.build/themes/details/astroplate/) startpagina / thema die ik hiervoor heb gebruikt, is net als Astro zelf open source.

## Genereren van de inhoud

Ik verwachtte aanvankelijk het grootste deel van de site, zowel tekst als afbeeldingen, in één keer met AI in agentmode te genereren. Dit is zeker mogelijk (inclusief Vibe-codering van een Astro-site eromheen), maar toen ik aan de site begon te werken bleek het instellen van de Astro-site gemakkelijk genoeg om niet veel hulp nodig te hebben. Ik wilde ook WSL gebruiken voor het uitvoeren van de Astro npm/yarn tooling om in ieder geval nog een bepaalde mate van security te behouden, wat volledig door AI gestuurde ontwikkeling zou hebben bemoeilijkt.

Vervolgens, toen ik daadwerkelijk de inhoud aan het maken was, bleek opnieuw dat het gemakkelijker was om de tekst met de hand te schrijven in plaats van een AI dit te laten doen. Dit liet het genereren van afbeeldingen voor logo's, illustraties enz. over. VS Code is geweldig voor het beheren van een project als dit (bijvoorbeeld de remote/WSL-ondersteuning ervan is feilloos), maar in de gratis versie van Github Copilot ondersteunen verrassenderwijs geen van de meegeleverde modellen het genereren van afbeelding. Er zijn verschillende manieren om dit op te lossen, en ik heb een MCP-server voor dit doel gemaakt om ComfyUI netjes in de Copilot-agentsmodus te integreren, maar bleek in de praktijk wat onhandig. In plaats daarvan heb ik ervoor gekozen ComfyUI rechtstreeks met de webgebruikersinterface en enkele aangepaste bedrijfsgerichte workflows te gebruiken, en vervolgens de resultaten in VS Code te kopiëren.

Al met al verliep het project soepel, het was een goed moment om wat nieuwe technologie te leren en het was meer bevredigend om deze tooling te gebruiken dan WordPress. Ik laat u het oordeel over de resulterende website zelf vellen!
