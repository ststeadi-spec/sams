
## Selvforbedring 12.11.2026 (cloud)
- `sams_telegram.py` CLOUD_NOTE påstod "Gmail works here directly", men cloud-serveren har ingen Gmail-connector (ingen MCP-servere). Rettet: mail-opslag går via `sams-mac`; er Mac'en offline, siges det kort og der hjælpes med det nettet kan svare (fx færgeplan). Anledning: færge-spørgsmål 11.11 kl. 23:05.
- Backup: `backups/orb-bak-archive/sams_telegram.py.<stamp>`. Træder i kraft ved næste genstart af broen (proces kører uden supervisor på cloud; ikke genstartet mens en `claude -p` kørte).

## Selvforbedring 13.11.2026 (cloud)
- Billede uden tekst 12.11 kl. 21:42 blev besvaret af Haiku, som ikke genkendte en Steadicam-rig og spurgte "hvad skal jeg bruge det til". `pick_model` sender nu beskeder der starter med `[Samuel sendte` (billeder/filer) til mindst Sonnet, og billeder uden tekst får en hint om at tolke det ud fra hans arbejde/udstyr og gætte kvalificeret før der spørges.
- Backup: `backups/orb-bak-archive/sams_telegram.py.<stamp>`. Ingen tests på cloud; verificeret med py_compile + pick_model-kald. Træder i kraft ved næste genstart af broen (ikke genstartet: en `claude -p` kørte).
