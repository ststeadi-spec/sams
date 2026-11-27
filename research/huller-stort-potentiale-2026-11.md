# Uløste huller med stort potentiale (research, 27. nov. 2026)

> Researchjob, ingen app-kode. Formål: at finde software-huller i hele verden med et reelt og voksende behov, ingen god løsning endnu og potentiale til at blive en stor virksomhed. Én person skal kunne starte med AI-kodning.
> Jeg har bevidst ignoreret film/TV, Skandinavien og tidligere idéer.

## Sådan skal du læse rapporten

- **[V] = verificeret** med kilde (link i afsnittet "Kilder"). Mange kilder er advokatfirmaer og leverandører, så deres tal kan være farvede. Det er markeret der, hvor det betyder noget.
- **[G] = gæt/estimat** ud fra egen viden og ræsonnement. Det gælder bl.a. de fleste TAM-tal og vurderinger af konkurrenter. Det har ikke været muligt at tjekke alle konkurrenter én for én. Søgningen var en halv dags desk research, ikke interviews.
- Score 1-5 på fem akser: **Ægthed** (er behovet reelt og betalt), **Størrelse**, **Tidsvindue** (5 = vinduet er åbent nu og varer et par år), **Startbarhed** for én person, **Forsvar** (moat). Max 25.
- **Skepsis-regel:** For hver kandidat står der, *hvorfor* hullet findes. Ellers ingen kandidat. "Ingen konkurrenter" tæller som et advarselstegn, ikke et plus.

## Metode

Fem linser blev brugt: (a) nye skift 2025-2028 (regler, AI-agenter, betalinger, aldring, klima), (b) folk der efterspørger et værktøj, (c) brancher på papir, Excel og WhatsApp, (d) lande/sprog uden de store spillere, (e) nye kundegrupper. Det stærkeste mønster er **(a) ny regel + (e) ny kundegruppe**. Når en lov får en deadline, opstår der på én dag tusindvis af virksomheder med et problem, de ikke havde i går. De store leverandører går efter enterprise-kunderne, så mellemstore og små kunder står tilbage med Excel og konsulenter. AI gør det muligt at automatisere den slags dokumentations- og fortolkningsarbejde, som før krævede konsulenttimer.

**Overordnet fund:** Regelstrømmen fra EU 2026-2028 rammer især **små producenter af forbundne/digitale produkter** og **små grænseoverskridende e-handlere**. Her er der flest ægte og datofæstede huller. I USA har én ny lov, Medicaid-arbejdskravet, skabt et pludseligt behov hos millioner af mennesker og tusindvis af sundhedsaktører. AI-agent-infrastruktur er overvejende ved at lukke (der kommer mange VC-finansierede startups).

---

## Del 1: 32 kandidat-huller

Hvert hul står med: **Behov · Hvem · Bevis · Hvorfor uløst · Hvem kan lukke det · TAM · Første 10 kunder · Vejen til stor**.

### A. Ny lovgivning (datofæstede behov)

**1. CRA-compliance-drift for små producenter af produkter med digitale elementer (EU Cyber Resilience Act)**
- Behov: Siden **11. sep. 2026** skal producenter indberette aktivt udnyttede sårbarheder og alvorlige hændelser til ENISA's platform inden for få timer/dage. Fra **dec. 2027** gælder de fulde krav: SBOM, sårbarhedshåndtering, supportperiode, CE-dokumentation. [V]
- Hvem: Alle der sælger hardware/software med digitale elementer i EU: IoT-firmaer, maskinbyggere med firmware, små softwarehuse, importører.
- Bevis: ENISA-survey (feb.-mar. 2026): kendskabet er højt, men den praktiske parathed halter, og **hver femte var usikker på, om CRA overhovedet gælder dem**. Reglerne omfatter også ældre produkter, som stadig har support. [V] Big4/BSI/UL/advokater sælger rådgivning (der er altså betalingsvilje), men de sælger timer, ikke drift. [V]
- Hvorfor uløst: Ny regel. Enterprise-værktøjer (fx SBOM-/firmware-scanning til bilindustri og medico) er prissat til store kunder [G]. Små firmaer har ingen PSIRT-funktion.
- Hvem kan lukke: SBOM-/AppSec-leverandører (Snyk, Anchore, ONEKEY, Cybellum, Finite State) kan rykke nedad [G]. Certificeringshuse kan bundle software. **Delvist åbent. Vinduet er ca. 2026-2028.**
- TAM [G]: Titusindvis af EU-producenter. 50-100k firmaer × €3-10k/år ≈ **€150M-1B/år**, plus ikke-EU-producenter der sælger til EU.
- Første 10: Find små IoT-/hardwarefirmaer på Kickstarter/CE-lister og i hardware-acceleratorer. Tilbyd "CRA-scan + rapporteringsberedskab" til fast pris. Brug LinkedIn-tråde og ENISA-diskussioner.
- Vejen til stor: Udvid fra rapportering til et fuldt "compliance-OS" for forbundne produkter (CRA + Data Act + RED + GPSR + digitalt produktpas + AI Act for indlejrede systemer fra 2028). Én kunde, mange regler.

**2. EU Data Act: dataadgangsportal for mellemstore producenter af forbundne produkter**
- Behov: Siden 12. sep. 2025 har brugere ret til data fra forbundne produkter. Produkter sat på markedet **efter 12. sep. 2026** skal have "access by design". Bøderne kan nå GDPR-niveau. [V]
- Hvem: Mellemstore producenter (mikro- og små virksomheder er delvist undtaget [V]) af maskiner, landbrugsudstyr, hvidevarer, wearables og bil-tilbehør.
- Bevis: Hver eneste store advokatfirma har lavet Data Act-guides, og der er klar efterspørgsel efter rådgivning [V]. Søgningen fandt **intet navngivet softwareværktøj** [V: ingen fund], hvilket kan betyde et hul eller et lille marked.
- Hvorfor uløst: Ny regel. Kræver både jura (forretningshemmeligheder, FRAND-vilkår) og integration med IoT-backend. IoT-platforme (AWS IoT, Azure) leverer rør, ikke compliance-flow.
- Hvem kan lukke: IoT-platforme, PIM-/kundeportal-leverandører, consent-leverandører (OneTrust). [G]
- TAM [G]: 10-30k mellemstore EU-producenter × €10-30k/år ≈ **€100-900M/år**.
- Første 10: Tyske/italienske Mittelstand-maskinbyggere via VDMA-/branchemesser. Tilbyd "Data Act-portal på 30 dage" (white-label portal + datakatalog + anmodningsflow).
- Vejen til stor: Den samme portal bliver grundlaget for datamarkedspladsen (producenten kan sælge/dele data med tredjeparter mod kompensation, som loven tillader).

**3. Medicaid-arbejdskrav: "behold-dækning"-værktøj for sundhedsaktører (USA)**
- Behov: Fra **1. jan. 2027** skal stater kræve, at voksne i Medicaid-udvidelsen dokumenterer 80 timers arbejde, uddannelse eller frivilligt arbejde om måneden, eller at de er fritaget. Nebraska og Iowa starter tidligere, og i Nebraska mister folk allerede dækning. [V]
- Hvem: Millioner af modtagere. Men den betalende kunde er **FQHC'er (sundhedscentre), hospitaler, managed care-selskaber (MCO'er) og NGO'er**, som mister indtægt eller medlemmer, når patienter falder ud. [G for betalingsvilje]
- Bevis: CBPP vurderer, at der "ikke findes teknologi, der kan implementere kravet gnidningsfrit". Pilotforsøg i Louisiana og Arizona havde lav deltagelse og begrænset funktionalitet. Føderale midler er øremærket ($200M til systemer) [V]. Staterne bruger eksisterende leverandører (Deloitte m.fl.) til *statens* side [V]. Modtager-/aktørsiden er tynd.
- Hvorfor uløst: Ny regel med 18 måneders tidsfrist. Staternes indkøb er langsomme [V], og de store leverandører bygger statens system, ikke hjælpen til modtagerne.
- Hvem kan lukke: MCO'ernes egne teams, Unite Us/Findhelp (henvisning), Propel (SNAP-app), Benefits Data Trust-lignende NGO'er. [G] **Vinduet er åbent nu, men politisk risiko: reglen kan ændres ved magtskifte.**
- TAM [G]: ~1.400 FQHC-organisationer + ~6.000 hospitaler + ~80 Medicaid-MCO'er. Pr. bevaret medlem er et MCO ~$400-600/md. værd [G]. Realistisk **$300M-1B/år**.
- Første 10: FQHC'er i Nebraska, Iowa og Georgia (Georgia har allerede "Pathways"). Tilbyd SMS/WhatsApp-flow på engelsk/spansk til at dokumentere timer og fritagelser og sende til statens portal. Betal pr. bevaret patient.
- Vejen til stor: Platform for "hold folk berettigede" på tværs af programmer (SNAP-arbejdskrav, Medicaid-fornyelse, ACA). Resultatbaseret prisætning.

**4. CBAM-data for leverandører uden for EU (eksportørsiden)**
- Behov: CBAM's definitive fase startede 1. jan. 2026. Importører over 50 ton skal være autoriserede deklaranter, og certifikatkøb starter feb. 2027 for 2026-import [V]. Uden verificerede emissionsdata bruges **standardværdier, der gør varen dyrere** [V]. Det er en konkurrenceulempe for eksportøren.
- Hvem: Små og mellemstore stål-, aluminium-, cement-, gødnings- og skruefabrikker i Tyrkiet, Indien, Ukraine, Vietnam, Egypten, Kina.
- Bevis: Reglen og prismekanismen er [V]. Der findes mange CBAM-værktøjer til *EU-importører* [G]. Eksportør-værktøjer på tyrkisk, hindi og vietnamesisk er sjældne [G, ikke verificeret].
- Hvorfor uløst: Det er et sprog- og land-hul, og eksportørerne er "for små" for europæiske SaaS-firmaer.
- Hvem kan lukke: Verifikatorer (TÜV, SGS, Bureau Veritas) med egne portaler, lokale ESG-konsulenter. [G]
- TAM [G]: 10-20k anlæg × $2-10k/år ≈ **$50-200M/år**. Mere hvis CBAM udvides til flere varer (det er planlagt [G]).
- Første 10: Tyrkiske stål-/skrueproducenter via eksportforeninger (İMMİB). Bed EU-importører om at pege på deres leverandører, så importøren bliver kanalen.
- Vejen til stor: "Produkt-CO₂-pas" for eksportører til alle markeder med grænsetold (UK-CBAM 2027, evt. andre).

**5. Grænseoverskridende EU-compliance for små webshops (PPWR/EPR + €3-told + GPSR)**
- Behov: PPWR gælder fra 12. aug. 2026. **Der er ingen generel undtagelse for små producenter**, og man skal registrere/rapportere/betale i hvert land og evt. have en repræsentant der. €3-told pr. vare under €150 gælder fra 1. jul. 2026 [V].
- Bevis: Branchemedier kalder PPWR en "papirfælde", og nogle sælgere holder op med at sende til EU [V]. Amazon-finansieret research peger på samme byrde [V, med interesse].
- Hvorfor uløst: Behovet er fragmenteret på 27 portaler/sprog. Eksisterende aktører (Lizenzero, Taxually, ERP Recycling, Ecosistant) dækker dele af det [V/G]. **Hullet er ved at lukke.**
- TAM [G]: Mio. sælgere. €20-100/md. ≈ €500M+.
- Første 10: Shopify-app-butikken. Etsy-/Shopify-forums.
- Vejen til stor: Bliv "Stripe Tax for EU-produktregler".

**6. India DPDP-consent og -drift for SMV'er**
- Behov: DPDP-reglerne blev offentliggjort 13. nov. 2025. Consent managers kom med fra nov. 2026, og hovedpligterne gælder **maj 2027** [V].
- Hvem: Millioner af indiske virksomheder med kundedata (klinikker, skoler, fintech, D2C).
- Hvorfor uløst: Ny regel. Globale leverandører er for dyre.
- Hvem kan lukke: Indiske startups og legaltech, fx Leegality, Arrka, Tsaaro [G]. Consent managers skal være indiske selskaber [V], så en udenlandsk solo-founder står svagt. **Det lukker hurtigt.**
- TAM [G]: Stort antal, lav pris: $100-300M/år.

**7. EU Pay Transparency for virksomheder med 100-250 ansatte**
- Behov: Fristen var 7. jun. 2026. De fleste lande er forsinkede, og første rapporter kommer i 2027-2028 [V].
- Hvorfor uløst: Reglerne varierer fra land til land. HR-systemerne er langsomme.
- Hvem kan lukke: Personio, HiBob, Workday, Syndio, Figures [G]. **Lukker, når lovene falder på plads.** TAM [G] €200-500M.

**8. EUDR-sporbarhed for små kooperativer**
- Behov: Gælder fra 30. dec. 2026 for store og mellemstore, og fra 30. jun. 2027 for mikro og små [V]. Der kræves polygon-kortlægning af parceller [V].
- Hvorfor uløst: Arbejdet ligger i marken, og regelændringerne har skabt usikkerhed.
- Hvem kan lukke: Koltiva, Farmforce, Meridia, Satelligence m.fl. [G] **Overfyldt.** TAM [G] $200M.

**9. IEEPA-toldrefusion og drawback for små importører (USA)**
- Behov: Højesteret underkendte IEEPA-tolden 20. feb. 2026. ~$166-170 mia. skal refunderes til 300k+ importører via CBP's CAPE-portal (siden apr. 2026). Der er høje afvisningsrater og et stramt 80-dages vindue [V]. Drawback: $3-6 mia./år hentes ikke hjem [V, leverandørtal].
- Hvorfor uløst: Det kræver ACE-adgang, og toldmæglere prioriterer store kunder [V].
- Hvem kan lukke: **Flexport, Passport, Tarifflo (YC S26) er allerede i gang** [V]. Det er en engangsbølge. **Lukker.**

**10. AI Act Art. 50 (gennemsigtighed) / AI-mærkning for små udgivere og apps**
- Behov: Gennemsigtighedskrav fra aug. 2026. Højrisiko-delen er udskudt til dec. 2027/aug. 2028 [V].
- Hvem kan lukke: C2PA-værktøjer, og Adobe/Google bundler funktionen. Den forventede "AI Act-bølge" blev mindre af udskydelsen [V]. TAM moderat.

**11. Aldersverifikation for små platforme (UK OSA, Australiens under-16-regel, amerikanske delstater)**
- Behov: Australiens regel gjaldt fra 10. dec. 2025 for de store platforme [V]. UK OSA rammer også små fora [G, ikke verificeret i denne søgning].
- Hvem kan lukke: Yoti, k-ID, Persona [G]. Hullet for de små platforme er at få det billigt og privatlivsvenligt. TAM begrænset, fordi mange små platforme hellere lukker eller geoblokerer.

### B. AI-agenter og deres infrastruktur

**12. "Agent-klar" booking og tilbud for lange-hale-servicefirmaer** (VVS'er, klinikker, frisører, håndværkere)
- Behov: AI-assistenter (ChatGPT, Gemini) skal kunne booke og indhente tilbud. ACP (OpenAI/Stripe) og UCP (Shopify/Google) dækker *produkter* [V]. **Søgningen fandt intet om services/booking** [V: ingen fund].
- Bevis: PayPal-survey: små firmaer halter efter, og 74% siger, at de skal have betydelig ekstern hjælp [V, leverandørdata].
- Hvorfor uløst: Det er nyt, servicedata er ustrukturerede (priser varierer, kapacitet), og protokollerne er bygget til webshops.
- Hvem kan lukke: **Square, Booksy, Fresha, Jobber, ServiceTitan, Google Reserve** kan tænde det for deres kunder. Det er den største trussel. [G]
- TAM [G]: >10 mio. servicefirmaer globalt × $20-50/md.
- Første 10: Firmaer uden bookingsystem (telefon/WhatsApp), fx håndværkere. En AI-telefon/WhatsApp-agent med et MCP-endpoint.
- Vejen til stor: Bliv "Stripe for agent-til-service-transaktioner" på tværs af bookingsystemer.

**13. Know-Your-Agent / agent-identitet for handlende**: Baselayer ($35M A, sep. 2026), Beltic, Vouched ($17M), Keycard ($38M) er i gang [V]. NIST-standard er på vej. **Lukker.**

**14. Agent-betalinger og -mandater**: Visa, Mastercard, Stripe, Coinbase og mange startups er i gang [G]. **Lukket for en solo-founder.**

**15. MCP/agent-adapter for gamle vertikale systemer** (tandlæge-PMS, ERP'er til grossister uden API)
- Hvorfor hul: De gamle leverandører vil ikke åbne op. Det er for småt for Zapier.
- Risiko: Leverandørerne kan lukke adgangen. Juridisk gråzone ved screen-scraping.
- TAM [G]: Fragmenteret, $100M+ pr. vertikal. Startbarhed: høj. Forsvar: lavt.

**16. Revision og logning af AI-agenters handlinger for regulerede SMV'er** (revisorer, advokater, mæglere): Observability-markedet er overfyldt for udviklere (Langfuse m.fl.). Hullet er en "compliance-læsbar" log for ikke-teknikere. Moderat. [G]

**17. AI-agent-ansvarsforsikring/-garanti**: AIUC m.fl. er i gang [G]. Kræver kapital og licens. Ikke startbar solo.

**18. Licensering af AI-crawling for små udgivere**: Cloudflare pay-per-crawl og TollBit [G]. **Lukket.**

### C. Brancher på papir, Excel, WhatsApp og telefon

**19. Speditører og toldmæglere: e-mail-til-ordre-automatisering**: Mange YC-firmaer 2025-26 er i gang (Alchemize, MarkIt, flere "AI-teammates for forwarders") [V]. **Lukker** i USA. **Mindre lukket i Tyrkiet, Mellemøsten, Afrika, LatAm** (sprog- og landehul) [G].

**20. Grossister og distributører, B2B-ordrer via WhatsApp i emerging markets**: Choco, Pepper og lokale aktører [G]. Delvist løst.

**21. Japanske kaigo-operatører (ældrepleje) med papirarbejde**: Stor mangel på personale (~90% har afvist opgaver pga. bemanding) [V]. Branchen foreslår SaaS til små operatører på landet [V]. **Sproghul og relationssalg. Ikke startbart for en ikke-japansktalende solo-founder.** TAM stort.

**22. Skrothandlere og genvindingspladser (compliance mod metaltyveri, kontantløse betalinger, ID-krav)**: Nicheværktøjer findes [G]. Lille TAM.

**23. Kommunale vandværker: blyrørsinventar (US EPA LCRI)**: 120Water m.fl. [G]. Lukket.

**24. Tolkebureauer: booking og fakturering (domstole, sundhed)**: Gamle systemer, telefon og Excel [G]. Lille, men tilgængeligt marked. TAM ~$100M.

### D. Demografi og aldring

**25. GUIDE-modellen (CMS-demens): software til care navigators**
- Behov: 8-årig model (2024-2032). ~235 unikke organisationer. Op til $2.625 pr. patient/år i PY2026 [V]. Ansøgningsvinduet er lukket [V].
- Hvorfor hul: Ny betalingsmodel, og EPJ-leverandører bygger ikke til omsorgsgivere.
- Risiko: Lille, fastlåst kundebase. Remo Health m.fl. er leverandører [V]. **TAM lille (~$20-50M).** Godt kilecase, dårlig virksomhed.

**26. Familiens "økonomi-omsorger"-værktøj (forældres regninger, svindelvagt, fuldmagt)**: Carefull, EverSafe [G]. Lav betalingsvilje blandt forbrugere (de fleste apps har fejlet). Hullet er B2B2C via banker.

**27. Dødsbo-administration uden for USA/UK** (Tyskland, Brasilien, Indien): I USA/UK findes Empathy og Atticus [G]. Andre lande har landespecifikke regler, og der er et klart sproghul. TAM pr. land $50-200M. Langsomt salg via begravelsesforretninger og banker.

### E. Klima og energi

**28. Bevis for klimasikring af boliger over for forsikring** (Californiens "Safer from Wildfires", IBHS-certificering, vind i Florida)
- Behov: Forsikringsselskaberne *skal* give rabat for tiltag, men de kræver fotos, kvitteringer og inspektioner [V]. AAA giver op til 12,5% [V].
- Hvorfor hul: Ny regel, intet standardiseret bevisflow mellem husejer, håndværker og forsikringsselskab.
- Hvem kan lukke: Forsikringsselskabernes apps, IBHS, inspektionsfirmaer. [G]
- TAM [G]: Millioner af boliger i risikozoner. B2B til forsikringsselskaber/mæglere $100-300M.

**29. Hedestress-compliance for arbejdsgivere** (delstatsregler i CA, WA, OR, MD, NV; Golfen; Indien): Wearables (Kenzen) [G]. Det føderale OSHA-krav er usikkert. Moderat.

**30. Fællesopladning til lejligheder og ejerforeninger i emerging markets**: Mange aktører i Vesten [G]. LatAm/Indien er åbent, men infrastrukturen kommer først. Tidligt.

### F. Nye betalingssystemer og nye kundegrupper

**31. Pix Automático-abonnementsdrift for brasilianske SMV'er**
- Behov: Lanceret jun. 2025. Antallet af virksomheder der modtager betalinger gik fra 275 til ~14.000 (aug. 2025 → aug. 2026). Påbudt for interbank-autodebitering fra jan. 2026 [V].
- Hvorfor hul: Det er nyt, og kortbaseret abonnementssoftware (Stripe Billing) passer dårligt [G].
- Hvem kan lukke: PagBrasil, EBANX, Asaas, Iugu, Vindi [V/G]. **Lokale spillere bevæger sig hurtigt. Lukker.**

**32. Kreatører og uafhængige "AI-solo-virksomheder" som ny kundegruppe** (bogføring, kontrakter, IP-licenser til AI-træning): Behovet er reelt, men det er et diffust segment, og Stripe/Gumroad/Lemon Squeezy dækker det meste [G]. Lav ægthed som "hul".

---

## Del 2: Scoretabel

| # | Hul | Ægthed | Størrelse | Vindue | Solo-start | Forsvar | Sum |
|---|-----|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | CRA-compliance for små producenter | 5 | 4 | 5 | 4 | 3 | **21** |
| 2 | EU Data Act-portal | 4 | 4 | 5 | 3 | 4 | **20** |
| 3 | Medicaid "behold-dækning" for aktører | 5 | 4 | 4 | 3 | 3 | **19** |
| 4 | CBAM eksportørsiden | 4 | 3 | 5 | 4 | 3 | **19** |
| 12 | Agent-klar booking for servicefirmaer | 3 | 5 | 4 | 4 | 2 | **18** |
| 5 | EU-webshop-compliance (PPWR/€3) | 5 | 4 | 3 | 4 | 2 | 18 |
| 28 | Klimasikringsbevis til forsikring | 4 | 3 | 4 | 3 | 3 | 17 |
| 15 | MCP-adaptere til gamle systemer | 3 | 3 | 4 | 5 | 2 | 17 |
| 19 | Speditører (ikke-engelsksprogede markeder) | 4 | 4 | 3 | 3 | 2 | 16 |
| 27 | Dødsbo uden for US/UK | 4 | 3 | 3 | 3 | 3 | 16 |
| 7 | Pay Transparency | 4 | 3 | 3 | 3 | 2 | 15 |
| 6 | India DPDP | 4 | 3 | 3 | 2 | 2 | 14 |
| 31 | Pix Automático | 4 | 3 | 2 | 3 | 2 | 14 |
| 16 | Agent-revisionslog for ikke-teknikere | 3 | 3 | 3 | 4 | 1 | 14 |
| 25 | GUIDE-demens | 4 | 1 | 3 | 3 | 3 | 14 |
| 21 | Japansk kaigo | 5 | 4 | 4 | 1 | 4 | 18* |
| 24 | Tolkebureauer | 3 | 2 | 3 | 4 | 2 | 14 |
| 29 | Hedestress | 3 | 3 | 2 | 3 | 2 | 13 |
| 9 | Toldrefusion/drawback | 5 | 3 | 1 | 3 | 1 | 13 |
| 8 | EUDR kooperativer | 4 | 3 | 2 | 2 | 2 | 13 |
| 26 | Økonomi-omsorg | 3 | 3 | 3 | 3 | 1 | 13 |
| 11 | Aldersverifikation (små platforme) | 3 | 2 | 3 | 3 | 1 | 12 |
| 20 | B2B-WhatsApp-ordrer | 4 | 3 | 1 | 3 | 1 | 12 |
| 10 | AI Act Art. 50 | 3 | 2 | 3 | 3 | 1 | 12 |
| 22 | Skrothandlere | 3 | 1 | 3 | 4 | 2 | 13 |
| 30 | EV-opladning EM | 2 | 3 | 2 | 2 | 2 | 11 |
| 13 | KYA-agentidentitet | 4 | 5 | 1 | 1 | 1 | 12 |
| 23 | Blyrør | 4 | 2 | 1 | 3 | 1 | 11 |
| 14 | Agentbetalinger | 4 | 5 | 1 | 1 | 1 | 12 |
| 17 | Agentforsikring | 3 | 4 | 2 | 1 | 2 | 12 |
| 18 | Crawl-licenser | 3 | 3 | 1 | 2 | 1 | 10 |
| 32 | AI-solo-kreatører | 2 | 3 | 3 | 4 | 1 | 13 |

\* Kaigo scorer højt på marked, men får startbarhed 1. Det er udelukket fra top 5, fordi kravet om "én person med AI, hvor som helst fra" ikke holder (japansk sprog og relationssalg).

**Ved at lukke:** #9, #13, #14, #18, #19 (USA), #20, #23, #31. Dem ville jeg ikke starte i.

---

## Del 3: Top 5 med hård kritik

### 1. CRA-compliance-drift for små producenter (score 21)
**Hullet:** Titusindvis af små EU- og ikke-EU-producenter har siden sep. 2026 haft en lovpligtig 24-timers indberetningspligt og står over for fulde krav i dec. 2027. Ingen software er prissat og bygget til dem.
**Hård kritik:**
- *Compliance-købere køber minimum.* Mange vil vente til første håndhævelse (som ved EAA, hvor håndhævelsen indtil videre er korrigerende, ikke bødeudstedende [V]). Salget kan derfor gå trægt før dec. 2027.
- *Fortolkningsrisiko:* Harmoniserede standarder er ikke færdige [G]. Produktet skal kunne ændres hurtigt.
- *SBOM-giganterne* kan lave en "SMB-tier" på et kvartal. Forsvaret skal derfor ligge i workflow + dokumentationsbibliotek + juridisk kortlægning af produktkategorier, ikke i scanning.
- *Ansvarsrisiko:* Hvis kunden misser en 24-timers frist pga. dit værktøj, så får du skylden. Det kræver en ansvarsfraskrivelse og senere en forsikring.
- *Fordel:* Det er et B2B-produkt med en hård dato og en køber, der får flere regler (Data Act, digitalt produktpas, AI Act 2028). Det giver mulighed for land-and-expand.

### 2. EU Data Act-dataadgangsportal (score 20)
**Hullet:** Mellemstore producenter af forbundne produkter skal kunne udlevere brugsdata på anmodning og i nye produkter bygge adgang ind fra start. De har kun advokatnotater, ingen værktøjer.
**Hård kritik:**
- *Er efterspørgslen fra brugerne reel?* Hvis få slutbrugere anmoder om data, vil producenterne nøjes med en manuel e-mail-proces. **Det er den største risiko.** Behovet kan være 90% teoretisk, indtil konkurrenter (fx uafhængige reparatører) begynder at bruge retten.
- Søgningen fandt *ingen* værktøjer. Det kan betyde, at markedet ikke er opstået endnu.
- Kræver integration med mange forskellige IoT-backends, så det kan blive en konsulentforretning i forklædning.
- *Fordel:* Den rigtige køber er dem, der *vil have data* (eftermarked, forsikring, reparation). Kan vendes til en datamarkedsplads, og den har netværkseffekt. Synergi med #1, samme køber.

### 3. Medicaid "behold-dækning" for sundhedsaktører (score 19)
**Hullet:** Millioner af amerikanere skal fra jan. 2027 dokumentere arbejde hver måned eller miste dækning. Staternes systemer er sene og dårlige, og aktørerne, der mister penge, har intet værktøj.
**Hård kritik:**
- *Politisk risiko:* Reglen kan blive ændret eller udsat (CBPP og andre presser på for mere tid [V]). Et skifte i Kongressen efter 2026-valget kan ændre den.
- *Etisk og omdømmemæssig:* Du tjener penge på en regel, der fjerner sundhedsdækning. Formuler det som "hjælp folk med at beholde den".
- *Salgscyklus:* Hospitaler og FQHC'er har lange indkøbsforløb. HIPAA, BAA og sikkerhedsreviews er tunge for én person.
- *Staternes portaler er forskellige* (50 integrationer). AI kan hjælpe, men det er stadig tungt.
- *Fordel:* Ekstremt ægte og målbar ROI (en bevaret patient = penge), og vinduet åbner nu. Hullet er bekræftet af CBPP og KFF [V].

### 4. CBAM for eksportører uden for EU (score 19)
**Hullet:** Små tyrkiske, indiske og vietnamesiske stål- og aluminiumsproducenter skal levere verificerede emissionsdata til EU-kunder, ellers bliver varen dyrere pga. standardværdier. Værktøjerne er bygget til EU-importører, på engelsk.
**Hård kritik:**
- Verifikation kræver akkrediterede verifikatorer. Softwaren er kun en del af løsningen.
- EU har gentagne gange forenklet og udskudt (omnibus, 50-ton-tærskel) [V]. Omfanget kan skrumpe igen.
- Prisfølsomme kunder i lavtlønslande, så betalingsvilje pr. kunde er lav.
- Solo-founder uden lokalsprog: AI-oversættelse hjælper, men tillid sælges lokalt. Kræver lokal partner.

### 5. Agent-klar booking/tilbud for servicefirmaer (score 18)
**Hullet:** AI-assistenter kan nu købe produkter (ACP/UCP), men ikke booke en VVS'er eller hente et tilbud. Millioner af servicefirmaer har ingen maskinlæsbar kapacitet eller pris.
**Hård kritik:**
- *Det mest sandsynlige udfald er, at platformene lukker hullet* (Square, Booksy, Jobber, Google). Det er det svageste forsvar i top 5.
- Efterspørgslen fra forbrugerne via agenter er stadig lille og bygger på leverandørtal [V, PayPal/Shopify].
- *Men:* Det har det største potentiale, hvis det lykkes ("Stripe for agent-til-service"). Det er en asymmetrisk satsning: billig at teste, enorm hvis den rammer. Mest realistisk via firmaer *uden* bookingsystem (telefon/WhatsApp), som platformene ikke når.

---

## Del 4: 30-dages planer (top 3) for at bevise behovet uden at kode

### Plan for #1 CRA-compliance
- **Dag 1-5:** Byg en liste med 200 små producenter: hardware på Kickstarter/Indiegogo med EU-levering, medlemmer af IoT- og Embedded World-udstillerlister, små firmware-teams. Find CTO/produktansvarlig.
- **Dag 3-7:** Lav en landingsside (no-code) med "CRA-tjek på 15 min: gælder CRA for dig, og er du klar til 24-timers indberetning?" og en pris (fx €290 for scan + plan, €99/md. for beredskab). Tilmelding = intention.
- **Dag 5-20:** 30 samtaler (LinkedIn + kold e-mail). Spørgsmål: Hvem håndterer sårbarheder i dag? Har I et SBOM? Hvad har I betalt rådgivere? Hvad sker der, hvis I får en sårbarhed i morgen?
- **Dag 10-25:** Concierge-MVP: Lav manuelt (med Claude som hjælp) 5 betalte CRA-tjek-rapporter for €290. Mål, om de vil betale for løbende drift.
- **Dag 25-30:** Beslutning. **Grønt lys** hvis ≥5 betalte rapporter, ≥3 vil have løbende abonnement og ≥30% af samtalerne beskriver en konkret smerte. **Rødt** hvis svaret overvejende er "vi venter til 2027".

### Plan for #2 EU Data Act
- **Dag 1-7:** Vend det om: find først *efterspørgselssiden*. Tal med 10 uafhængige reparatører og eftermarkedsfirmaer (landbrugsmaskiner, hvidevarer, bil) og spørg, om de har anmodet om data efter Data Act, og hvad der skete. Hvis ingen har anmodet, bliver hypotesen svag.
- **Dag 5-15:** 20 samtaler med compliance-/produktchefer hos mellemstore tyske/italienske/nordiske maskin- og apparatproducenter (sproget er ligegyldigt, AI oversætter). Spørgsmål: Har I fået anmodninger? Hvordan svarer I? Hvem ejer problemet? Budget?
- **Dag 10-20:** Lav en figma/no-code-mock af en portal + "Data Act-beredskabsscore". Vis den i samtalerne og bed om en betalt pilot (€2-5k) eller et intentionsbrev (LOI).
- **Dag 15-30:** Tal med 3 advokatfirmaer, der har skrevet Data Act-guides. Spørg, om de vil henvise klienter til et værktøj (kanaltest).
- **Beslutning:** Grønt lys ved ≥2 LOI/betalte pilot + bevis for reelle dataanmodninger. Ellers parkér og fold idéen ind i #1 som modul.

### Plan for #3 Medicaid "behold-dækning"
- **Dag 1-5:** Kortlæg Nebraska, Iowa, Montana og Georgia: hvordan indberetter man, hvilke fritagelser er der, hvor går folk tabt? Læs CBPP's leverandøranalyse og KFF-rapporterne.
- **Dag 3-15:** 25 samtaler med FQHC-direktører, hospitalernes ansvarlige for patientøkonomi ("revenue cycle") og "enrollment assisters" (navigatorer) i de stater. Spørgsmål: Hvor mange patienter mister I? Hvad koster det? Hvad gør I nu (telefon, papir)?
- **Dag 10-20:** Mål det reelle problem: Bed om (anonymiserede) tal for frafald fra Nebraska siden starten. Skriv en 1-sides ROI-beregning (frafald × gns. indtægt pr. patient).
- **Dag 15-30:** Tilbyd en manuel pilot til 1-2 FQHC'er: SMS-påmindelser + hjælpelinje drevet manuelt eller med no-code (Twilio Studio), betalt pr. patient. Tal også med 2 Medicaid-MCO'er om medlemsfastholdelse.
- **Beslutning:** Grønt lys ved én betalt pilot eller ét LOI fra et MCO + dokumenteret frafald. **Rødt** ved tegn på, at reglen udsættes, eller at staterne selv løser det med ex parte-data (automatisk verifikation, CMS anbefaler det [V]).

---

## Samlet anbefaling

Start med **#1 CRA** som kile. Det har den hårdeste dato, en klar B2B-køber og er mest startbart solo. Planlæg fra dag ét **#2 Data Act** som modul nummer to til samme køber ("compliance-OS for små producenter af forbundne produkter"). **#3 Medicaid** er det mest ægte behov, men har politisk og salgsmæssig risiko. Det kræver amerikanske samtaler i de næste 30 dage, ellers er vinduet væk.

**Hvad Samuel skal tjekke/beslutte:**
1. Vil du gå efter **B2B-compliance** (kedeligt, sikkert, hård dato) eller **asymmetrisk agent-satsning** (#5)?
2. Kan du tage 25-30 kundesamtaler i en måned? Alle planer forudsætter det.
3. Tjek selv konkurrenterne for #1 og #2 igen (søg "CRA compliance software SME" og "Data Act portal"). Det er de vigtigste ikke-verificerede antagelser.

---

## Kilder

**CRA:**
- [EU-Kommissionen: CRA reporting](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting)
- [CSA research note: CRA-indberetning fra 11. sep. 2026](https://labs.cloudsecurityalliance.org/research/csa-research-note-eu-cra-reporting-deadline-20260903-csa-sty/)
- [NCSC Irland: CRA](https://ncsc.gov.ie/cra/)
- [DLA Piper: CRA-forberedelse](https://privacymatters.dlapiper.com/2026/08/eu-preparing-for-the-cyber-resilience-acts-september-2026-reporting-obligations/)
- [BSI: september 2026-deadline](https://www.bsigroup.com/en-GB/insights-and-media/insights/blogs/the-september-2026-cyber-resilience-act-deadline/)
- [UL: CRA-parathed](https://www.ul.com/news/cyber-resilience-act-readiness-what-manufacturers-need-know-about-new-reporting-requirements)
- [Skadden: FAQ og tjekliste](https://www.skadden.com/insights/publications/2026/09/get-ready-reporting-faqs-and-checklist)

**Data Act:**
- [Orrick](https://www.orrick.com/en/Insights/2025/09/The-EU-Data-Act-is-in-Force-What-Should-Businesses-Do)
- [Alston & Bird](https://www.alston.com/en/insights/publications/2025/09/eu-data-act-connected-products)
- [ACT | The App Association: SMV'er](https://actonline.org/2025/08/27/the-eu-data-act-why-smes-and-startups-should-take-notice/)
- [Travers Smith](https://www.traverssmith.com/knowledge/knowledge-container/the-eu-data-act-compliance-countdown-for-connected-products/)

**Medicaid:**
- [CBPP: leverandørlandskabet](https://www.cbpp.org/research/health/assessing-the-medicaid-work-requirement-vendor-landscape)
- [CBPP: staterne har brug for mere tid](https://www.cbpp.org/research/health/states-need-more-time-to-prepare-for-medicaid-work-requirement)
- [KFF: staternes beslutninger](https://www.kff.org/medicaid/an-early-look-at-policy-decisions-as-states-get-ready-to-implement-work-requirements/)
- [KFF Health News: lidt bevis for, at teknologien virker](https://kffhealthnews.org/health-care-costs/medicaid-eligibility-tool-pilot-test-work-requirements-ai-louisiana-arizona-georgia/)
- [Axios aug. 2026](https://www.axios.com/2026/08/03/medicaid-work-eligibility-requirement-rules-patients?stream=top)
- [Georgetown CCF tracker](https://ccf.georgetown.edu/feature/tracking-implementation-of-h-r-1-medicaid-work-reporting-requirements/)
- [Bloomberg Law: teknologi- og finansfirmaer](https://news.bloomberglaw.com/health-law-and-business/tech-financial-firms-sign-on-to-build-medicaid-work-requirement)

**CBAM:**
- [EU-Kommissionen: CBAM definitive regime](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-definitive-regime_en)
- [EY: CBAM-omnibus](https://www.ey.com/en_gl/technical/tax-alerts/eu-adopts-cbam-omnibus-regulation)
- [Irish EPA](https://www.epa.ie/our-services/licensing/climate-change/eu-carbon-border-adjustment-mechanism/)
- [BSI 2026/2027](https://www.bsigroup.com/en-GB/insights-and-media/insights/blogs/preparing-for-eu-cbam-the-20262027-transition-explained)

**PPWR / €3-told:**
- [Packaging Gateway](https://www.packaging-gateway.com/features/eu-packaging-rules-increase-compliance-burden-for-cross-border-sellers/)
- [e-Residency: PPWR for små virksomheder](https://www.e-resident.gov.ee/blog/posts/ppwr-regulation-small-businesses/)
- [ioplus: papirfælde](https://ioplus.nl/en/posts/why-the-new-eu-packaging-law-is-a-paperwork-trap)
- [ChannelEngine](https://www.channelengine.com/en/blog/packaging-and-packaging-waste-regulation-ppwr)
- [EU-Kommissionen: €3-told](https://commission.europa.eu/news-and-media/news/ensuring-fairness-and-safety-eur3-customs-duty-low-value-parcels-2026-06-29_en)
- [EU Access2Markets](https://trade.ec.europa.eu/access-to-markets/en/news/eu-applies-eu3-customs-duty-item-low-value-e-commerce-consignments)

**DPDP:**
- [PIB-dokument](https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251117695301.pdf)
- [YourStory: 18 måneder](https://yourstory.com/2025/11/digital-personal-data-protection-dpdp-rules-2025-rollout-over-18-months)
- [Hogan Lovells](https://ca.hoganlovells.com/en/publications/indias-digital-personal-data-protection-act-2023-brought-into-force-)
- [Entrepreneur India: SMV'er](https://india.entrepreneur.com/news-and-trends/india-pushes-for-digital-privacy-with-dpdp-rules-2025-key/499704)

**AI Act-omnibus:**
- [Gibson Dunn](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement)
- [Hogan Lovells](https://www.hoganlovells.com/en/publications/eu-legislators-agree-to-delay-for-highrisk-ai-rules)
- [The Register](https://www.theregister.com/ai-and-ml/2026/05/07/eu-hits-snooze-on-ai-act-rules-after-industry-backlash/5234530)

**Pay Transparency:**
- [Baker McKenzie](https://www.bakermckenzie.com/en/insight/publications/2026/06/european-union-pay-transparency-directive-beyond-the-deadline)
- [Littler](https://www.littler.com/news-analysis/asap/did-member-states-meet-deadline-status-implementation-eu-pay-transparency)
- [Morgan Lewis](https://www.morganlewis.com/pubs/2026/06/eu-pay-transparency-directive-the-deadline-for-transposition-has-passed-what-now)

**EUDR:**
- [EU Access2Markets: udsættelse til dec. 2026](https://trade.ec.europa.eu/access-to-markets/en/news/delay-until-december-2026-and-other-developments-implementation-eudr-regulation)
- [EY](https://taxnews.ey.com/news/2026-0237-eu-deforestation-regulation-application-postponed-to-30-december-2026)
- [Baker McKenzie](https://www.bakermckenzie.com/en/insight/publications/alerts/2025/12/european-union-provisional-agreement-on-eudr-one-year-postponement)

**Told (USA):**
- [NPR: refusioner](https://npr.org/2026/02/21/g-s1-110987/supreme-court-tariffs-refunds)
- [Bloomberg Law: $170 mia.](https://news.bloomberglaw.com/us-law-week/tariff-ruling-kicks-off-messy-fight-over-170-billion-in-refunds)
- [Holland & Knight: CAPE](https://www.hklaw.com/en/insights/publications/2026/04/cape-has-arrived-navigating-the-next-phase-of-ieepa-duty-refunds)
- [FoodNavigator: afvisningsrater](https://www.foodnavigator-usa.com/Article/2026/05/14/tariff-refunds-what-brands-need-to-know/)
- [Cato](https://www.cato.org/blog/ieepa-tariff-refunds-are-far-ideal-could-get-farther)
- [FreightWaves: drawback](https://www.freightwaves.com/news/settling-into-tftea-drawback)
- [Flexport: drawback](https://www.flexport.com/blog/how-importers-and-exporters-can-claim-millions-in-duty-drawback/)

**AI-agenter / KYA:**
- [SiliconANGLE: Baselayer $35M](https://siliconangle.com/2026/09/22/with-35m-in-series-a-funding-baselayer-is-building-the-trust-layer-for-the-agentic-economy/)
- [Businesswire: Vouched $17M](https://www.businesswire.com/news/home/20250904708838/en/Vouched-Announces-$17-Million-Series-A-to-Accelerate-Expansion-Building-on-Know-Your-Agent-KYA-Suite-Success)
- [SecurityWeek: Keycard](https://www.securityweek.com/keycard-emerges-from-stealth-mode-with-38-million-in-funding/amp/)

**Agentisk handel:**
- [PayPal: handlendes holdning](https://www.paypal.com/us/brc/article/agentic-commerce-pulse-report-findings)
- [Shopify: agentic commerce](https://www.shopify.com/blog/agentic-commerce)

**YC-logistik:**
- [YC Logistics-liste](https://ycombinator.com/companies/industry/Logistics)
- [YC Alchemize](https://ycombinator.com/companies/alchemize)

**GUIDE:**
- [CMS GUIDE](https://www.cms.gov/priorities/innovation/innovation-models/guide)
- [CMS MLN-faktaark jul. 2026](https://www.cms.gov/sites/default/files/2026-07/mln7172818-guiding-improved-dementia-experience-model.pdf)
- [AARP](https://www.aarp.org/health/brain-health/medicare-guide-program-for-dementia-caregivers/)
- [UMN-studie](https://experts.umn.edu/en/publications/the-characteristics-of-sites-delivering-the-guiding-an-improved-d/)

**Japan kaigo:**
- [MHLW-PDF](https://www.mhlw.go.jp/content/12300000/001747214.pdf)
- [Japan Times: mangel på hjemmepleje](https://www.japantimes.co.jp/news/2025/05/05/japan/home-care-services-worker-shortage)
- [nippon.com](https://www.nippon.com/en/japan-topics/c15004/japan%E2%80%99s-failing-nursing-care-insurance-system.html)

**Wildfire:**
- [CDI Safer from Wildfires](https://www.insurance.ca.gov/01-consumers/200-wrr/safer-from-wildfires.cfm)
- [CDI FAQ](https://www.insurance.ca.gov/01-consumers/105-type/95-guides/03-res/upload/faq-safer-from-wildfire-regulation.pdf)
- [AAA/CSAA-rabat](https://csaa-insurance.aaa.com/wildfire_discount)

**Pix Automático:**
- [Safra](https://oespecialista.safra.com.br/pix-automatico-pagamento-contas-recorrentes/)
- [Adyen](https://www.adyen.com/pt_BR/centro-de-conhecimento/pix-automatico-jornada-adyen-proximos-passos)
- [PagBrasil](https://www.pagbrasil.com/blog/recurring-payments/automatic-pix-2026/)
- [EBANX via FF News](https://ffnews.com/news/more-than-60-of-pix-automatico-users-are-brand-new-subscribers-to-digital-platforms-ebanx-data-shows)

**EAA-håndhævelse:**
- [Deque](https://www.deque.com/blog/early-signs-of-eaa-enforcement-across-europe/)
- [Taylor Wessing](https://www.taylorwessing.com/en/insights-and-events/insights/2026/03/the-eaa-takes-shape)

**Australien, minimumsalder:**
- [eSafety](https://www.esafety.gov.au/about-us/industry-regulation/social-media-age-restrictions)

**Begrænsninger:** Ingen interviews. Konkurrentlisterne er ikke udtømmende. Flere kilder er dateret efter søgeindeksets friskhed, og nogle tal kommer fra leverandører med egeninteresse (markeret). TAM-tal er grove bottom-up-gæt og skal valideres.
