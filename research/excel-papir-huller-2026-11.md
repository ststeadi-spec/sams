# Markedshuller: arbejde der stadig kører på Excel, papir, WhatsApp og e-mail

*Research udført 27.11.2026 (automatisk baggrundsjob, ingen app-kode). Globalt fokus, ikke film/TV og ikke Skandinavien. Idéer der kun opstår pga. nye lovkrav er udeladt.*

## TL;DR

35 kandidater er undersøgt. **Ingen af dem er et helt rent hul.** Næsten alle "oplagte" niches (fragt-tilbud, catering, turneringer, bogholderi, lab-lager, tutoring, hestestalde) har allerede 3-10 betalte værktøjer. De reelle huller ligger hvor **to eller flere firmaer skal koordinere med hinanden** (ikke internt i ét firma), og hvor de eksisterende værktøjer er tunge ERP-moduler, som den ene part ikke vil købe.

**Top 5:**

| # | Hul | Løses i dag med | Hvorfor der ikke findes et godt værktøj |
|---|---|---|---|
| 1 | Produktionsstatus mellem brands og deres kontraktproducenter/fabrikker | Ugentlige e-mails, PDF-statusrapporter, WhatsApp/WeChat, Excel "time-and-action"-ark | Kundeportaler findes kun som moduler i producentens ERP (BatchMaster, Nulogy). Anvyl blev købt af Sage i 2024 og rykket op i ERP-kanalen. Ingen let, neutral "fælles tråd" der virker uden integration |
| 2 | Drifts-lag for små influencer-/creatorbureauer (2-20 ansatte) | Google Sheets, Etsy-skabeloner, Notion, e-mail med creators | De store værktøjer (Grin, CreatorIQ, Upfluence) sælger opdagelsesdatabaser til brands. Bureauets egen drift (aftaler, leverancer, kundegodkendelse, udbetaling, margin) er en eftertanke |
| 3 | Let handels-back-office for små råvareimportører (kaffe, kakao, nødder, krydderier, skaldyr) | Master-regneark med kontrakter, lots, positioner og prøver | CTRM-systemer (Agiblocks, Hermes, DycoTrade) er enterprise/ERP-tunge. Hver vertikal er for lille alene, så ingen har lavet ét let værktøj på tværs |
| 4 | Brugtbils- og maskineksportører (Japan/UAE/USA → Afrika, Mellemøsten, Asien) | WhatsApp-grupper, Excel-lagerlister og håndlavede fakturaer | Kun CarDeal365 (1 anmeldelse) og skræddersyede ERP'er. Branchen er uformel og for "beskidt" for SaaS-firmaer i Vesten |
| 5 | Gruppe-rejser (Umrah/Hajj, skole, kirke, retreats) i lande uden for USA/EU's betalingssystemer | WhatsApp-grupper, Excel, bankoverførsler, kontanter | WeTravel og SquadTrip er bygget til amerikanske kort og Stripe. Kunderne klager over kortdækning uden for USA/UK/EU |

**Anbefaling:** Nr. 1 er stærkest (ægte hul, netværkseffekt, salg kan foregå 100 % online over for brands). Nr. 2 er nemmest at starte solo, men har den svageste forsvarbarhed. Nr. 3 har det bedste "voldgravs"-potentiale, men kræver domæneviden.

---

## Metode og begrænsninger (læs dette først)

- Research udført med web-søgning, opslag på Capterra/G2/Product Hunt/YC-kataloget, branchefora (ProZ, Practical Machinist, NMPro) og Etsy. Samlet ca. 100 søgninger og opslag.
- **Reddit var ikke tilgængelig** (søgeværktøjet viste næsten ingen Reddit-tråde, og direkte opslag blev blokeret). Capterra.com og kometsales.com kunne ikke hentes direkte. Det betyder, at meget af "smerte-beviset" kommer fra **leverandørers egne blogs og cases**, som har interesse i at beskrive et Excel-problem. Det er markeret.
- **VERIFICERET** = en konkret kilde siger det (link angivet). Det betyder ikke, at kilden er neutral.
- **GÆT** = mit eget estimat eller min ræsonnering.
- Markedsstørrelser er næsten alle GÆT. Der findes ikke pålidelige tal for "antal små importører af X".
- Næste skridt før der bygges noget: manuel gennemgang af Reddit og samtaler med 10+ rigtige brugere (se 30-dages planer).

### Scoring

Hver kandidat er scoret 1-5 på:

- **Æ** = hullets ægthed (5 = intet brugbart værktøj; 1 = løst af mange)
- **P** = potentiale på sigt (kan det blive en stor virksomhed?)
- **O** = online-distribution / stedsuafhængighed (5 = kunder findes, køber, onboardes og supporteres 100 % online). **Vægtes dobbelt**, som ønsket
- **S** = startbarhed solo med AI-kodning
- **F** = forsvarbarhed (netværkseffekt, data, skiftomkostning)

**Total = Æ + P + 2×O + S + F (maks 30).** Regel: kandidater med **Æ ≤ 2 kan ikke komme i top 5** uanset total. Ellers kommer mættede men online-venlige markeder (fx musik-advancing) for højt op.

---

## Alle 35 kandidater

### A. Handel, logistik og produktion

| # | Kandidat | Bevis for Excel/papir/WhatsApp | Konkurrenter | Vurdering | Æ | P | O | S | F | Total |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Spot-tilbud hos små speditører** (fragtrater fra rederier i Excel) | WebCargo/Freightos-undersøgelse af 40 speditører: 61 % håndterer rater i Excel, 45 % via telefon/mail (VERIFICERET, leverandør: [webcargo.co](https://www.webcargo.co/blog/choosing-a-freight-rate-management-system-rms/)) | Freightify, CargoSphere, WebCargo, cargo.one, Magaya, GoFreight, Descartes Spot, Quotiss ($99-1.999/md), og mange nye AI-ratesheet-startups ([The Loadstar](https://theloadstar.com/ship-angel-oceanrate-ocean-rate-sheet-ai/)) | Løst og bliver mere overfyldt | 1 | 3 | 5 | 3 | 1 | 18 |
| 2 | **DTC-brands der følger PO'er/produktion hos fabrikker i Asien** | Airtable sælger en "time-and-action"-skabelon til DTC-tøj (VERIFICERET: [airtable.com](https://www.airtable.com/use-cases/product-milestone-time-and-action-dtc-apparel)). Uphance skriver om "regnearks-tærsklen" | Anvyl → købt af Sage okt. 2024 ([CPA Practice Advisor](https://www.cpapracticeadvisor.com/2024/10/01/sage-acquires-supply-chain-technology-platform-anvyl/111246/)), TrackIT, Uphance, Backbone PLM, SourceDay | Delvist hul. **Slået sammen med #31 til top 1** | 3 | 4 | 4 | 4 | 3 | 22 |
| 3 | **B2B-grossistordrer via WhatsApp** (Indien, LatAm, Afrika, MENA) | Stærkt: Source.One håndterer 25.000 RFQ'er/dag på WhatsApp ([WhatsApp Business](https://business.whatsapp.com/resources/success-stories/sourceone)) | Bizom, FieldAssist, Sukhiba ([TechCrunch](https://techcrunch.com/2023/10/25/sukhiba-eyes-africa-growth)), BeatRoute, Mercately, nFuse, Seals AI (YC S24), Take App | Løst og overfyldt, og lokal tilstedeværelse hjælper meget | 1 | 4 | 2 | 3 | 2 | 14 |
| 4 | **Planteskolers ugentlige tilgængelighedslister** (Excel/PDF pr. mail) | Stærkt: Saunders Brothers, New Moon Nursery, Hillcrest m.fl. sender ugentlige Excel-lister (VERIFICERET: [saundersbrothers.com](https://saundersbrothers.com/page/Wholesale-Availability), [NMPro](https://www.nurserymag.com/article/playing-matchmaker)) | Plantbid (gratis for avlere), LandscapeHub, SBI Quick Avail, Nursery Designs | Delvist hul, men lav betalingsvilje og ældre, sæsonbetonet målgruppe | 3 | 2 | 3 | 4 | 2 | 17 |
| 5 | **Snitblomsthandel** (farme i Ecuador/Colombia/Kenya → importører) | Ikke fundet direkte (GÆT) | Komet Sales (konsoliderer markedet, 4.000+ virksomheder: [koronet.com](https://koronet.com/komet-sales)), Floriday, Unosof, FreshPortal | Løst på importørniveau | 2 | 2 | 2 | 3 | 2 | 13 |
| 6 | **Små råvareimportører** (kaffe, kakao, nødder, krydderier, skaldyr): kontrakter, lots, positioner | Cropster og RoasterTools kalder master-regnearket "en byrde" (leverandør). Agiboo: små handlere "stykker systemer sammen af regneark" ([agiboo.com](https://www.agiboo.com/ctrm-software-for-smes-affordable-solutions-for-small-and-medium-businesses/)). Sea Delight brugte "GP og Excel" ([inecta](https://inecta.com/blog/in-conversation-with-seafood-trader-sea-delight)) | Agiblocks, Hermes, OpenCTRM, opsPhlo (Acumatica), DycoTrade (Dynamics), CropConex ([Sprudge](https://sprudge.com/cropconex-unveils-new-suite-of-tools-for-coffee-traders-224294.html)), inecta Seafood | Delvist hul. **Top 3** | 3 | 3 | 4 | 3 | 4 | 21 |
| 7 | **Brugtbils- og maskineksportører** (Japan/UAE/USA → Afrika m.fl.) | WhatsApp er hovedkanalen; numre står på hver annonce, og eksportører kører WhatsApp-kanaler (VERIFICERET overfladisk, omfang GÆT) | CarDeal365 (1 Capterra-anmeldelse: [capterra.ca](https://www.capterra.ca/software/1106697/CarDeal365)), Rlogical (skræddersyet), Emirates Auto Dealer, AutoTrade24; markedspladser SBT, BE FORWARD, JapaneseCarTrade | Delvist/reelt hul. **Top 4** | 4 | 4 | 3 | 3 | 3 | 20 |
| 8 | **Uafhængige salgsagenturer** (multi-line reps): ordrer og provision | Ikke stærkt dokumenteret | Repfabric (4,8/5, 44 anm.), Rep Order Management ($50/bruger), eRep, RepBud | Løst. Evt. smal niche: automatisk provisionsafstemning ud fra producenternes PDF/Excel-opgørelser (GÆT) | 2 | 2 | 4 | 4 | 2 | 18 |
| 9 | **Små job-shops/værksteder**: planlægning på whiteboard/Excel | Stærkt: Practical Machinist-tråde om whiteboard → Excel, og "$500/md software du vil smide ud af vinduet" (VERIFICERET: [practicalmachinist.com](https://www.practicalmachinist.com/forum/threads/developer-looking-for-help-understanding-how-small-shops-track-work.447345/)) | ProShop, JobBOSS, E2, MRPeasy, Fulcrum, Katana, Steelhead, Paperless Parts | Løst. Dem der bliver på whiteboard gør det frivilligt | 1 | 3 | 4 | 3 | 2 | 17 |
| 10 | **Skibsmæglere** (positionslister og lastordrer via mail) | Branchen kører på mail | Shipfix (Veson, 400k mails/dag), Kpler Inbox, Signal Ocean, SpotShip | Løst af stærke spillere der ejer data | 1 | 3 | 3 | 2 | 1 | 13 |
| 11 | **Vin- og spiritusimportører**: allokering til restauranter/butikker | Ikke fundet direkte (GÆT) | 365WineTrade (Dynamics), Wine Hub UK (fra £1.285/md), Provi/SevenFifty (USA), Ekos, Vintegrate | Delvist hul uden for USA (EU/UK/Asien) til €100-300/md | 3 | 2 | 4 | 4 | 3 | 20 |
| 12 | **Skrot- og genbrugsmetalhandlere** (priser og handler i WhatsApp-grupper, især Indien/MENA) | IndiaMART fuld af handlere med WhatsApp-knapper og kg-priser (VERIFICERET overfladisk) | MyScrap, MetalMandi, ScrapC, Recykal (WhatsApp-bot til indkøbsgrupper) | Delvist, men stærkt lokalt og relationsbaseret | 3 | 3 | 2 | 3 | 2 | 15 |

### B. Service, rejser og events

| # | Kandidat | Bevis | Konkurrenter | Vurdering | Æ | P | O | S | F | Total |
|---|---|---|---|---|---|---|---|---|---|---|
| 13 | **Incoming-touroperatører/DMC'er**: tilbud og leverandørbooking | Tourwriter-case: Huellas brugte "Excel til hvert tilbud, kopieret linje for linje fra hotellernes rateark" (VERIFICERET, leverandør: [tourwriter.com](https://www.tourwriter.com/huellas-e-travel-2/)) | Tourplan (dyr, 6-12 mdr. implementering), Tourwriter (~$99/bruger), Kaptio, Lemax, Wetu, Safari Portal, TourConnect AI | Løst i toppen; delvist hul for 1-3-mands DMC'er i nye markeder (GÆT) | 2 | 3 | 3 | 3 | 3 | 17 |
| 14 | **Rooming lists / hotelblokke** til grupper | Mews, Clock og Crewfare ("Spreadsheet Purgatory") bekræfter Excel (VERIFICERET, leverandører) | Crewfare, Engine, EventPipe, Groups360 (gratis for arrangører), Cvent Passkey, OPERA-import | Mest løst; finansieres af hotelprovision, så arrangører forventer gratis | 2 | 1 | 5 | 4 | 1 | 18 |
| 15 | **Gruppe-rejsearrangører uden for USA/EU** (Umrah, skole, kirke, retreats): betaling og deltagerinfo | Mange Etsy-skabeloner til "group trip cost splitter" (VERIFICERET: [etsy.com](https://www.etsy.com/listing/4316252620)). WeTravel-klager over kortdækning uden for US/UK/EU ([Trustpilot](https://www.trustpilot.com/review/wetravel.com?page=2)) | WeTravel, SquadTrip, GroupCollect, Umrah360, UmrahOps | Delvist hul pga. betalingsskinner. **Top 5** | 3 | 3 | 4 | 3 | 3 | 20 |
| 16 | **Medicinske turisme-facilitatorer** | Indirekte: flere WhatsApp-CRM'er målretter nichen | Planports (dedikeret CRM med WhatsApp-indbakke), PlacidTracks, Kommo, Bitrix24 | Delvist; høj ansvars- og datarisiko | 2 | 3 | 4 | 2 | 2 | 17 |
| 17 | **Oversættelsesbureauer/freelancere** | ProZ: "et simpelt Excel-ark fungerer fint"; Plunet kaldes "overpriced" (VERIFICERET: [ProZ](https://guj.proz.com/forum/translation_project_vendor_management/363967-best_pm_solution_for_micro_business.html)) | Protemos (gratis for freelancere), XTRF, Plunet, LSP.expert | Løst, og AI skrumper segmentet (små bureauer -3,7 %: [Nimdzi](https://multilingual.com/nimdzi-100-top-5/)) | 1 | 1 | 5 | 4 | 1 | 17 |
| 18 | **Tolkebureauer**: booking af tolke | Ikke fundet | Boostlingo, Interpreter IO ($199/bruger), Interpreterly, Interpreter Intelligence | Muligt hul i lavenden (5-50 tolke, uden for USA) (GÆT). AI-eksponeret | 3 | 2 | 4 | 4 | 2 | 19 |
| 19 | **Musik: advancing/turnéstyring** for indie-artister og agenter | Google Drive-ark (VERIFICERET: [raespoon.com](https://raespoon.com/archive/independent-musician-touring-and-booking-guide/)) | Master Tour, Daysheets (gratis ≤5), Gigwell, Prism.fm, Stagent | Løst; indie-segmentet har ingen penge | 1 | 2 | 5 | 4 | 1 | 18 |
| 20 | **Akademiske konferencer** | EasyChair "reelt ikke gratis siden 2022" ([blog](https://data-mining.philippe-fournier-viger.com/easychair-is-it-still-good/)) | Microsoft CMT (gratis), ConfTool, Oxford Abstracts, Fourwaves, Dryfta, Whova | Løst; gratis incumbents sætter prisgulvet | 1 | 2 | 5 | 3 | 2 | 18 |
| 21 | **Ungdoms-/amatørturneringer** | Kun leverandørpåstande | SportsEngine Tourney, Exposure ($2/hold), LeagueApps, Tournify, LeagueLobster | Løst og prispresset | 1 | 2 | 5 | 4 | 2 | 19 |
| 22 | **Destination wedding-planlæggere** | Room blocks og gæstebetalinger håndteres på tværs af værktøjer | Aisle Planner, HoneyBook, Planning Pod, Zola, rsvpBOOK | Mest løst; tyndt hul i kombineret gæsterejse og leverandører | 2 | 2 | 5 | 4 | 2 | 20 |
| 23 | **Cateringfirmaer** (ordrer/BEO'er) | "Regneark til kalkulation, delt kalender, noter til allergier, gruppe-SMS til chauffører" (VERIFICERET, leverandørblog: [guideflow.com](https://www.guideflow.com/blog/catering-software)) | Caterease (klodset), Total Party Planner (4,8), Tripleseat (4,7), Better Cater | Løst af velanmeldte værktøjer | 1 | 2 | 3 | 3 | 2 | 14 |
| 24 | **Umrah/Hajj-agenturer** (MENA, Sydasien, britisk diaspora): manifester, værelser, busser, visa | Leverandørguide: betalinger ofte manuelle via WhatsApp ([go4whatsup](https://www.go4whatsup.com/gcc/whatsapp-for-umrah-hajj-agencies/)) | Umrah360, UmrahOps, PHPTravels (ingen priser/anmeldelser fundet) | Delvist hul; kræver arabisk/urdu og rammes af saudisk licensering. Indgår i top 5 (#15) | 3 | 3 | 3 | 3 | 3 | 18 |
| 25 | **Messeudstillere**: standlogistik, fragt, personale | Leverandører positionerer sig mod regneark | Boothlyo, ExhibitForce, generiske PM-værktøjer | Mest løst; lille betalingsvilje | 2 | 2 | 5 | 4 | 1 | 19 |

### C. Professionelle ydelser, lab, ejendom og andet

| # | Kandidat | Bevis | Konkurrenter | Vurdering | Æ | P | O | S | F | Total |
|---|---|---|---|---|---|---|---|---|---|---|
| 26 | **Små labs**: prøver i fryserbokse og reagenslager | LabKey: små labs bruger regneark fordi det er billigt (leverandør) | Quartzy ($159-299/md, ingen gratis plan længere), Benchling, eLabInventory, Labguru, Freezerworks, Genemod, Dr Freezr | Løst; lav betalingsvilje (forskningsmidler) | 2 | 1 | 5 | 4 | 2 | 19 |
| 27 | **Uafhængige kliniske forsøgssteder** (drift, ikke compliance) | Ikke verificeret (GÆT) | RealTime-CTMS (fra ~$500/md, 4,9), CRIO (fra ~$200/md), Clinical Conductor, Florence | Løst i USA; måske hul uden for USA; demo-tungt salg | 2 | 3 | 2 | 2 | 3 | 14 |
| 28 | **Influencer-/creatorbureauer** (2-20 ansatte): aftaler, leverancer, godkendelser, udbetaling, margin | Mange Etsy-trackers ($2-10) og gratis bureau-skabeloner fra Modash/Collabstr (VERIFICERET: [collabstr.com](https://collabstr.com/blog/influencer-marketing-spreadsheet)) | Influencity, Influencer Hero (klient-workspaces), PartnrUP (white label), Upfluence, Lumanu (udbetaling) | Delvist hul; markedet bevæger sig derhen. **Top 2** | 3 | 3 | 5 | 4 | 2 | 22 |
| 29 | **Hestestalde/opdræt** | OnlineBarnManagement: erstatter "papir, whiteboards og regneark" (leverandør) | BarnManager, BarnOps, HayNet, Stable Secretary, Equine Genie | Løst og fragmenteret | 1 | 1 | 5 | 4 | 1 | 17 |
| 30 | **Off-plan ejendomssalg**: udviklere deler enhedslister via WhatsApp-PDF'er med mæglere | Stærkt antydet af antallet af værktøjer (GÆT) | Dubai: Reelly (30.000+ agenter), Alnair, PropSpace, Property Finder. Indien: Sell.do, Propacity, PropertyPistol Radiate | Løst i Dubai og Indien; måske Tyrkiet/Egypten/KSA (ikke verificeret) | 1 | 3 | 2 | 2 | 3 | 13 |
| 31 | **Kontraktproducenter (kosmetik, kosttilskud, fødevarer) → kundernes ordre-/batchstatus** | Nulogy/ASCM 2025: 50 % af brands har begrænset/ingen indsigt i partnernes data, 80 % kalder det en stor udfordring; status kommer som "ugentlige opkald, PDF-rapporter og mailtråde" (VERIFICERET: [nulogy.com](https://nulogy.com/what-does-supply-chain-visibility-look-like-for-co-manufacturers/)) | Kun portaler inde i ERP'er: BatchMaster, Datacor, Amtech EnCore, Wherefour, Deacom, Nulogy (enterprise). Intet let selvstændigt værktøj fundet; intet på YC | **Reelt hul (middel sikkerhed). Top 1** (sammen med #2) | 4 | 4 | 4 | 4 | 4 | 24 |
| 32 | **Privat undervisning/tuition-centre** (Asien, Mellemøsten, Afrika) | Sandsynligt (GÆT) | Teachmint (~$5/bruger/år), Classplus, Tuition Plus, Cledgr ($11/md), TutorBird, Teachworks | Løst med varepriser | 1 | 1 | 3 | 4 | 1 | 13 |
| 33 | **Bygge-tilbudsudjævning (bid leveling) uden for USA** | Etsy-skabeloner til $9-27 ([etsy.com](https://www.etsy.com/listing/4583147009)); Archdesk: Excel har været hovedværktøjet (VERIFICERET) | Procore Tender Mgmt, BidWork (UK), Bidhive, SmartBid, ConWize, cosuno (DACH), mange AI-startups | Delvist hul (AI der læser PDF-tilbud), men kategorien fyldes hurtigt og salget er demo-tungt | 3 | 4 | 3 | 3 | 2 | 18 |
| 34 | **Bogholderifirmaer**: jagt på kunders bilag | Kendt problem | Karbon, TaxDome, Content Snare, Financial Cents, Soraban, Canopy, Liscio | Løst (bekræftet), meget overfyldt | 1 | 2 | 5 | 4 | 1 | 18 |
| 35 | **Rengøringsfirmaer med underleverandørnetværk** (koordinering via WhatsApp) | "WhatsApp-fototråde til kvalitet, papir-pluklister, regneark til vagtplan" (leverandørpåstand) | Swept, Jobber, ProTeams, Joblogic, Team Engine, Connecteam | Mest løst i US/UK; muligt hul for WhatsApp-native værktøj i MENA/LatAm | 2 | 2 | 3 | 3 | 2 | 15 |
| 36 | **Små udlejere i nye markeder** (husleje via WhatsApp/kontant) | Dwellrs (Nigeria) positioneres mod WhatsApp ([Product Hunt](https://www.producthunt.com/products/dwellrs)) | Nyumbani, Hauzisha (gratis), M-Pesa Bill Manager, RentBeta, RentOk | Løst og lav betalingsvilje | 1 | 1 | 2 | 3 | 1 | 10 |

*(36 rækker; #2 og #31 er to sider af samme hul og regnes som ét i top 5.)*

### Rangering (Æ ≥ 3)

1. **#31 + #2 Producent↔brand-status**: 24
2. **#28 Influencer-bureau-drift**: 22
3. **#6 Råvareimportør-back-office**: 21
4. **#7 Bil-/maskineksportører**: 20
5. **#15 Gruppe-rejser uden for US/EU-betalinger** (+ #24 Umrah): 20
6. #11 Vinimportører uden for USA: 20 (taber på potentiale)
7. #18 Tolkebureauer i lavenden: 19
8. #33 Bid leveling uden for USA: 18
9. #4 Planteskolelister: 17
10. #12 Skrothandel: 15

**Mønster:** De stærkeste huller er **mellem-firma-koordinering** (brand↔producent, importør↔leverandør↔køber, eksportør↔køber↔speditør). Hvert firma har sit eget system, men tråden *mellem* dem lever i mail og WhatsApp. Ingen ERP-leverandør ejer den tråd, fordi den ene part aldrig vil købe den anden parts ERP.

---

## Top 5 i detaljer, med hård kritik

### 1. Fælles produktionsstatus mellem brands og deres producenter

**Hvem har problemet:** Brands med fysiske produkter og omsætning på ca. $0,5-50 mio. (kosmetik, kosttilskud, fødevarer/drikke, tøj, gadgets), der får produceret hos kontraktproducenter (co-mans, co-packers) eller fabrikker i Asien/Tyrkiet/Portugal/Mexico. Og omvendt de små og mellemstore producenter, der hver uge får 20 mails med "hvor er min ordre?".

**Hvordan det løses i dag (bevis):**
- Status kommer som "ugentlige opkald, PDF-statusrapporter og mailtråde" (VERIFICERET, Nulogy: [link](https://nulogy.com/what-does-supply-chain-visibility-look-like-for-co-manufacturers/)).
- 50 % af brands har begrænset eller ingen indsigt i partnernes data; 80 % kalder det en stor udfordring (VERIFICERET, Nulogy/ASCM-undersøgelse 2025: [link](https://nulogy.com/?p=2972)).
- Airtable og ClickUp sælger/udgiver "time-and-action"-skabeloner til DTC-tøj (VERIFICERET: [airtable.com](https://www.airtable.com/use-cases/product-milestone-time-and-action-dtc-apparel)).
- Shopify-forum: brands der spørger hvordan de koordinerer ordrer mellem to producenter ([community.shopify.com](https://community.shopify.com/t/how-to-coordinate-orders-between-two-manufacturers/221326)).

**Hvorfor der ikke findes et godt værktøj:**
- Kundeportaler findes kun **inde i producentens ERP** (BatchMaster, Datacor, Amtech EnCore, Nulogy). Små producenter kører på QuickBooks, Excel eller gamle ERP'er og har ingen portal (GÆT, høj sikkerhed).
- Anvyl (den bedste brand-side-løsning) blev købt af Sage i 2024 og flyttet mod ERP-kanalen (VERIFICERET).
- Før AI var det umuligt at lave status uden integration. Nu kan en AI læse producentens mails, PDF'er og Excel-ark og opdatere en fælles tidslinje uden at nogen ændrer vaner. **Det er "for svært før AI"-argumentet.**

**Betalingsvilje:** Anvyl rejste VC-penge og blev opkøbt. Uphance, Backbone og SourceDay har betalende kunder. Om producenterne selv vil betale er ikke verificeret. **Brands betaler** (de har smerten og budgettet).

**Konkurrenter:** Sage Supply Chain Intelligence (ex-Anvyl), TrackIT, Uphance, Backbone PLM, SourceDay, Airtable/ClickUp-skabeloner; på producentsiden BatchMaster, Nulogy, Katana. Ingen af dem er en neutral, gratis-for-producenten tråd.

**Markedsstørrelse (GÆT):** Millioner af små brands med fysiske produkter (Shopify alene har flere millioner forhandlere). Hvis 100.000 brands verden over har 1+ eksterne producenter og betaler $100-300/md, er det et marked på $120-360 mio./år, før producent-siden og tillægsprodukter (inspektion, finansiering, fragt).

**Første 10-100 kunder online:**
- Brand-founders samles online: r/ecommerce, r/shopify, r/FulfillmentByAmazon, r/smallbusiness, Facebook-grupper for kosmetik- og kosttilskudsbrands, LinkedIn.
- Indhold: "co-man status-skabelon" (gratis Google Sheet), der fører over i værktøjet.
- **Viral mekanik:** brandet inviterer sin producent gratis. Producenten ser 1 kunde i værktøjet, og når 3 af hans kunder bruger det, vil han selv invitere de næste.

**Hvordan det kan blive stort:** Netværk af brands og producenter → producent-katalog/markedsplads ("find en co-man med ledig kapacitet"), produktionsfinansiering på PO'er, kvalitetsinspektion, fragtbooking. Tænk "Faire/Flexport for produktion".

**Kan drives hvor som helst fra:** **Ja** for brand-siden: selvbetjening, Stripe, e-mail-support. **Delvist** for producent-siden: de skal adoptere det, men produktet kan bygges så de ikke behøver at gøre noget (AI læser deres mails/PDF'er).

**Hård kritik:**
- "Visibility"-værktøjer er en kirkegård. Mange har prøvet (Anvyl, Sourcemap, Inspectorio på enterprise-niveau). Brands siger de vil have indsigt, men betaler sjældent for et dashboard alene.
- Producenterne kan modarbejde gennemsigtighed: forsinkelser er nemmere at skjule i mails.
- Integration er hele spillet. Uden at producenten taster noget ind er data kun så gode som mailene, og AI-udtræk kan fejle på kritiske datoer.
- Kunderne i hver vertikal (kosmetik vs. tøj vs. fødevarer) har forskellige milepæle. Man skal vælge én vertikal først, ellers bliver det generisk og taber til Airtable.
- Kinesiske fabrikker kører på WeChat, ikke WhatsApp, og WeChat-integration er svær.

### 2. Drifts-lag for små influencer-/creatorbureauer

**Hvem:** Bureauer med 2-20 ansatte, der kører creator-kampagner for brands. Ca. 7.000 influencer-marketing-firmaer i verden i 2025 (VERIFICERET: [Statista](https://statista.com/statistics/1553738/number-influencer-marketing-companies-worldwide)), plus mange tusinde "almindelige" bureauer, der laver creator-arbejde ved siden af.

**I dag:** Google Sheets pr. kampagne, gratis skabeloner fra Modash/Collabstr, Etsy-trackers til $2-10 (VERIFICERET), Notion, mail- og DM-tråde med creators, manuel udbetaling via PayPal/Wise.

**Hvorfor intet godt værktøj:** De store (Grin, CreatorIQ, Upfluence) sælger opdagelsesdatabaser og brand-siden. Bureauets kerne (aftale → brief → udkast → kundegodkendelse → postet → betalt → margin) er en eftertanke. AI gør det nu muligt automatisk at læse DM'er og mails og opdatere status.

**Betalingsvilje:** Udbetalingsplatforme tager 2-5 % af udbetalinger; Izea fra $250/md (VERIFICERET). Bureauer fakturerer kunder og har derfor budget.

**Konkurrenter:** Influencity, Influencer Hero (klient-workspaces), PartnrUP (white label), HypeAuditor, Archive, Lumanu. **Markedet bevæger sig mod dette.** Det er den største risiko.

**Markedsstørrelse (GÆT):** 20.000 bureauer × $150-500/md = $36-120 mio./år ARR-loft på software, plus en mulig betalingsandel (take rate) af creator-udbetalinger (influencer-marketing er en industri på $30+ mia.).

**Første kunder online:** LinkedIn (bureau-ejere poster offentligt), r/InfluencerMarketing, Slack-/Discord-fællesskaber for creator-økonomien, Product Hunt, gratis "kampagne-margin-beregner".

**Vækst:** Udbetalinger og fakturering (betalingsandel), white label til klienter, benchmark-data om priser pr. creator-type.

**Hvor som helst fra:** **Ja, fuldt ud.** Alle kunder er online-indfødte.

**Hård kritik:**
- **Svag forsvarbarhed.** Lavt teknisk vandløb, og fem velfinansierede spillere kan bygge det i næste kvartal.
- Bureauer i denne størrelse churner meget og er prisfølsomme; mange lukker eller fusionerer.
- Det er reelt "ClickUp med creator-felter". Mange bureauer vil sige "vi har Notion".
- Ikke specielt "WhatsApp/papir"-præget. Det er et regneark-problem i et digitalt-indfødt marked, så smerten er mindre.
- Top 2 skyldes primært den høje online-score, ikke et stort hul.

### 3. Let handels-back-office for små råvareimportører

**Hvem:** Importører og handlere med 2-30 ansatte af grøn kaffe, kakao, nødder, tørret frugt, krydderier, te og frossen fisk/skaldyr. De køber fra producenter i Afrika, Asien og Latinamerika og sælger til ristere, chokolademagere, fødevareproducenter og grossister.

**I dag:** Master-regneark med kontrakter (fast pris / PTBF mod futures), lots, lagerpositioner, prøver sendt/godkendt, forskud og afskibninger. Cropster og RoasterTools kalder regnearket "en byrde" (leverandør); Agiboo skriver at små handlere "stykker systemer sammen af regneark" (VERIFICERET); Sea Delight kørte på "GP og Excel" (VERIFICERET).

**Hvorfor intet godt værktøj:** CTRM-markedet er enterprise (Agiblocks, ION, Hermes) eller ERP-tilføjelser (DycoTrade til Dynamics, opsPhlo til Acumatica, inecta til Dynamics). De koster implementering og konsulenter. **Hver vertikal er for lille alene**, så ingen har lavet ét let, selvbetjent værktøj på tværs af "bløde" råvarer.

**Betalingsvilje:** CropConex har betalingsmodeller med niveauer (VERIFICERET). Enterprise-CTRM koster typisk fem- til seks-cifret pr. år (GÆT, ikke prissat offentligt). Handlerne flytter millioner pr. container, så $200-800/md er småpenge **hvis** det forhindrer én fejl.

**Konkurrenter:** Agiblocks (har SMB-version), Hermes, OpenCTRM, CropConex (kaffe), Cropster Green (kaffe-lots), inecta Seafood, BlueTrace, Wisefish. Tjek dybere: CropConex er den nærmeste trussel i kaffe.

**Markedsstørrelse (GÆT):** Specialkaffe alene: ca. 300-600 importører i USA/EU (lille). På tværs af kaffe, kakao, nødder, krydderier, te og skaldyr globalt: 10.000-30.000 små handlere × $300-800/md = $36-290 mio./år.

**Første kunder online:** LinkedIn (handlere er synlige), Specialty Coffee Association-fora, Sprudge- og Perfect Daily Grind-læsere, nichenyhedsbreve (fx Undercurrent for skaldyr), gratis "kontrakt- og positions-skabelon" der er bedre end deres egen.

**Vækst:** Start i én råvare, udvid horisontalt. Bagefter: handelsfinansiering, prøve-/kvalitetsdata, sporbarhed, markedsplads mellem producenter og købere. Data om faktiske handelspriser er værdifulde.

**Hvor som helst fra:** **Ja.** Branchen er international og kører allerede på mail og videoopkald.

**Hård kritik:**
- **Domæneviden er en reel barriere.** PTBF, differentials, hedging, kvalitetsscore og incoterms skal være rigtige, ellers mister du tilliden på dag 1. Samuel har ingen baggrund her.
- Små handlere er ofte konservative familievirksomheder. "Det virker jo i Excel" er stærkt.
- Lille marked pr. vertikal. "På tværs af råvarer" lyder godt, men hver har egne regler og vil føle at produktet ikke er lavet til dem.
- Salget kan blive demo-tungt (videomøder er OK online, men det skalerer langsomt).
- CropConex, Cropster og Agiboo kan lave en "lite"-version.

### 4. Værktøj til brugtbils- og maskineksportører

**Hvem:** Tusindvis af små eksportører i Japan (mange drevet af pakistanske, srilankanske og bangladeshiske iværksættere), UAE (Sharjah/Dubai), USA, UK og Korea, der sælger brugte biler, lastbiler og entreprenørmaskiner til købere i Afrika, Mellemøsten, Caribien og Centralasien. JapaneseCarTrade alene viser 9.182 eksportører (VERIFICERET, agentrapport). Japan eksporterer over 1 mio. brugte biler om året (GÆT, ikke åbnet kilde).

**I dag:** Lager i Excel, billeder og priser i WhatsApp-grupper og -kanaler, proformafakturaer i Word, betalingsopfølgning via bankkvitteringer på WhatsApp, fragt- og papirstatus pr. telefon (VERIFICERET overfladisk: WhatsApp-numre på alle annoncer; omfanget er GÆT).

**Hvorfor intet godt værktøj:** Branchen er uformel og "beskidt" for vestlige SaaS-firmaer; forhandlerkunderne sidder spredt over mange lande; og de få værktøjer er japanske ERP'er eller skræddersyede løsninger (CarDeal365 med 1 anmeldelse, Rlogical). **Intet WhatsApp-native værktøj fundet.**

**Betalingsvilje:** Uklar (GÆT: middel). Marginerne er tynde pr. bil, men der er mange biler, og én tabt betaling eller forkert dokument koster mere end et års abonnement.

**Konkurrenter:** CarDeal365, Rlogical, Emirates Auto Dealer, AutoTrade24, markedspladser (SBT, BE FORWARD) der hellere vil have handlen på deres platform.

**Markedsstørrelse (GÆT):** 20.000-50.000 eksportører globalt × $50-200/md = $12-120 mio./år, plus tillæg: betalingssikring/escrow, fragtbooking og finansiering (meget større).

**Første kunder online:** Eksportørerne er selv hyper-online (Facebook-grupper, YouTube, WhatsApp-kanaler, markedspladsprofiler med offentlige kontaktoplysninger). Gratis "WhatsApp-katalog-generator" fra deres Excel-lager er en naturlig indgang.

**Vækst:** Fra lager-/fakturaværktøj → betalingssikring mellem køber og eksportør (det største problem i branchen er tillid) → fragt- og toldformidling → finansiering. Kan blive "Shopify + Escrow for grænseoverskridende brugtvarehandel" og udvides til maskiner, dæk og reservedele.

**Hvor som helst fra:** **Delvist.** Software, salg og support kan foregå online på engelsk. Men en betalings-/escrow-del kræver licens og lokale partnere, og kunderne forventer support via WhatsApp på tidspunkter i deres tidszone.

**Hård kritik:**
- Uformelle brancher hader gennemsigtighed og abonnementer; mange vil hellere fortsætte i WhatsApp gratis.
- Svindel, sanktioner (fx eksport af biler til visse lande) og hvidvaskrisiko gør betalingsdelen, som er hvor pengene er, juridisk farlig.
- Markedspladserne (BE FORWARD, SBT) kan presse eller kopiere.
- WhatsApp Business API koster pr. samtale og kan ændre regler; afhængighed af Meta er en platformrisiko.
- Behovet er **ikke** verificeret med rigtige eksportører. Det er den mest gætte-baserede af top 5.

### 5. Gruppe-rejser uden for USA/EU's betalingssystemer (Umrah, skole, kirke, retreats)

**Hvem:** Små rejsearrangører og frivillige gruppeledere i Indien, Pakistan, Indonesien, Malaysia, Nigeria, Mellemøsten, LatAm og diaspora-miljøer, der arrangerer pilgrimsrejser (Umrah/Hajj), skolerejser, kirkerejser, retreats og bryllupsrejser for grupper.

**I dag:** WhatsApp-grupper til info, Excel til deltagerlister og værelser, betaling via bankoverførsel, mobile penge eller kontanter med skærmbilleder som kvittering. Etsy sælger mange "group trip payment tracker"-skabeloner (VERIFICERET). Umrah-guide: betalinger håndteres ofte manuelt (VERIFICERET, leverandør).

**Hvorfor intet godt værktøj:** WeTravel og SquadTrip er bygget til amerikanske kort/Stripe; kunder klager over kortdækning uden for US/UK/EU og over at pengene holdes tilbage til efter rejsen (VERIFICERET: [Trustpilot](https://www.trustpilot.com/review/wetravel.com?page=2), [Software Advice](https://www.softwareadvice.com/travel-management/wetravel-profile/reviews/)). Lokale betalingsskinner (UPI, mobile money, Pix, FPX) og afbetalinger er ikke understøttet.

**Betalingsvilje:** Bevist via transaktionsgebyrer (WeTravel, SquadTrip 3 % + Stripe).

**Konkurrenter:** WeTravel, SquadTrip, GroupCollect, Umrah360, UmrahOps, PHPTravels; plus generiske betalingslinks (Razorpay, Paystack).

**Markedsstørrelse (GÆT):** Saudi-Arabien sigter efter titusinder af millioner Umrah-pilgrimme om året; selv en lille andel af gruppebetalinger giver et stort transaktionsvolumen. Skole- og kirkerejser i nye markeder kommer oveni. En betalingsandel på 1-3 % af et par hundrede millioner dollars i volumen → $3-10 mio. i omsætning er realistisk, mere med lån og forsikring.

**Første kunder online:** Facebook- og WhatsApp-fællesskaber for gruppeledere, YouTube-rejsevloggere, Instagram-annoncer målrettet "Umrah group leader".

**Vækst:** Betalinger → afbetaling/"rejs nu, betal senere" → forsikring → hotel- og flyindkøb for grupper.

**Hvor som helst fra:** **Delvist.** Software og support kan drives online, men betalinger i hvert land kræver lokale betalingsudbydere (Stripe virker ikke overalt), og Umrah kræver saudisk licens hos den der sælger selve pakken (værktøjet kan stå udenfor, hvis det kun er til betaling og administration).

**Hård kritik:**
- Betalinger i 10 lande er ikke et soloprojekt; hvert land er en ny integration og nye regler. Start med ét land og én betalingsskinne.
- Religiøse rejser kræver kulturel tillid; en dansk solo-founder uden netværk i miljøet har en ulempe.
- Transaktionsgebyrer presses af lokale betalingslinks (Razorpay/Paystack er næsten gratis).
- Sæsonbetonet og skrøbeligt (Hajj-kvoter, visumregler, pandemier).
- WeTravel kan udvide til lokale betalinger.

---

## 30-dages planer (uden kode) for top 3

Fælles princip: **ingen kode før 10 samtaler og mindst 3 der siger "jeg betaler hvis du bygger X".** Alt foregår online.

### Plan 1: Producent↔brand-status

| Uge | Hvad | Mål |
|---|---|---|
| 1 | Vælg **én** vertikal (anbefaling: kosmetik/hudpleje eller kosttilskud, fordi de bruger co-mans meget og har høje marginer). Læs 50 tråde på r/ecommerce, r/shopify, r/SkincareAddiction-brandfora, Facebook-grupper for "beauty brand founders". Notér nøjagtige citater om "my manufacturer", "PO status", "delayed". Lav en liste over 100 brands med 1-20 ansatte (LinkedIn, Shopify-butikker der nævner "made in USA/EU by our lab partner") | 50 citater, 100 navne |
| 2 | Send 100 personlige LinkedIn-/mailbeskeder: "Jeg undersøger hvordan små brands følger med i produktionen hos deres producent. 15 minutters videoopkald?" Book 10-15 samtaler. Spørg: hvordan ser din sidste forsinkelse ud; hvem opdagede den; hvad kostede den; hvad bruger du i dag; hvad har du prøvet og opgivet | 10+ samtaler |
| 3 | Lav samme øvelse på producent-siden: find 30 små co-mans (Google "private label skincare manufacturer", Thomasnet, Alibaba) og tal med 5. Lav en klikbar mockup (Figma eller bare slides) af "fælles ordretråd hvor AI læser producentens mails" | 5 producentsamtaler, 1 mockup |
| 4 | Landingside med pris ($99/$249/md) og "Book pilot". Vis mockup til de 10 brands. Bed om forudbetaling eller skriftlig pilot-aftale. Beslut: fortsæt / skift vertikal / drop | ≥3 forudbetalte eller underskrevne piloter = byg. Ellers stop |

### Plan 2: Influencer-bureau-drift

| Uge | Hvad | Mål |
|---|---|---|
| 1 | Find 150 bureauer med 2-20 ansatte (LinkedIn-søgning "influencer marketing agency" + Clutch.co + Instagram-bios). Læs anmeldelser af Grin, Upfluence, Influencer Hero på G2/Capterra og notér hvad bureauer klager over | Liste + top 10 klager |
| 2 | Bed 50 bureauer om at sende deres (anonymiserede) kampagneark. Byd på en gratis "margin-analyse" af deres sidste kampagne i bytte for 20 minutter | 10 samtaler, 5 regneark |
| 3 | Kortlæg de 5 arks fælles struktur. Lav en Google Sheets-skabelon, der er bedre end alle 5, og del den gratis (Product Hunt, LinkedIn, r/InfluencerMarketing) med tilmelding til venteliste | 200 downloads / 50 på venteliste |
| 4 | Spørg de mest aktive skabelonbrugere: "Hvad ville få dig til at betale $149/md for at få det her som værktøj?" Tag forudbetaling. **Tjek særligt om Influencer Hero/PartnrUP allerede løser det for dem**, og hvis ja: drop | ≥5 forudbetalinger = byg |

### Plan 3: Råvareimportør-back-office

| Uge | Hvad | Mål |
|---|---|---|
| 1 | Lær domænet: læs om PTBF-kontrakter, differentials, kontraktformularer fra Green Coffee Association/ECF, lot-sporing. Se YouTube-foredrag fra SCA-konferencer. Vælg startråvare (anbefaling: specialkaffe, fordi den er mest online og har mange små importører, eller krydderier/nødder hvis CropConex viser sig stærk i kaffe) | 2-siders domæne-note |
| 2 | List 100 små importører (SCA-medlemsliste, Sprudge, Perfect Daily Grind, LinkedIn). Skriv til 60: "Hvordan holder I styr på kontrakter og positioner? Må jeg se jeres ark (anonymiseret)?" | 8-10 samtaler |
| 3 | Test grundigt CropConex, Cropster Green og Agiblocks SMB (demoer/prøveperioder). Notér præcist hvad de mangler for 2-10-personers firmaer og hvad de koster | Konkurrent-matrix |
| 4 | Mockup + pris ($299-599/md). Vis den til de 10. Kræv pilot-aftale. Afprøv samme pitch over for 10 nødde-/krydderi-importører for at teste "på tværs af råvarer" | ≥3 piloter i én råvare og ≥1 interesse i en anden = byg |

---

## Hvad Samuel bør tjekke/beslutte

1. **Vil du gå efter et B2B-koordinationsproblem** (top 1 og 3, større og mere forsvarbare, men længere salgscyklus) eller et **hurtigere online-indfødt marked** (top 2, nemmere at starte, svagere voldgrav)?
2. Lav selv et 30-minutters Reddit-tjek for top 1 (r/ecommerce, r/shopify "manufacturer delay") før du bruger tid på samtaler. Det var ikke muligt herfra.
3. Top 4 og 5 er de mest gætte-baserede. De kræver betalingslicenser eller lokal tillid og skal kun vælges hvis du har en personlig forbindelse til branchen.

## Kilder (udvalg)

- Nulogy om co-man-synlighed: https://nulogy.com/what-does-supply-chain-visibility-look-like-for-co-manufacturers/ og https://nulogy.com/?p=2972
- Sage køber Anvyl: https://www.cpapracticeadvisor.com/2024/10/01/sage-acquires-supply-chain-technology-platform-anvyl/111246/
- Airtable DTC time-and-action: https://www.airtable.com/use-cases/product-milestone-time-and-action-dtc-apparel
- Agiboo om CTRM for SMV'er: https://www.agiboo.com/ctrm-software-for-smes-affordable-solutions-for-small-and-medium-businesses/
- CropConex: https://sprudge.com/cropconex-unveils-new-suite-of-tools-for-coffee-traders-224294.html
- inecta / Sea Delight: https://inecta.com/blog/in-conversation-with-seafood-trader-sea-delight
- CarDeal365: https://www.capterra.ca/software/1106697/CarDeal365
- Statista, antal influencer-marketing-firmaer: https://statista.com/statistics/1553738/number-influencer-marketing-companies-worldwide
- Collabstr skabeloner: https://collabstr.com/blog/influencer-marketing-spreadsheet
- WeTravel-anmeldelser: https://www.trustpilot.com/review/wetravel.com?page=2
- WebCargo rate-undersøgelse: https://www.webcargo.co/blog/choosing-a-freight-rate-management-system-rms/
- Practical Machinist: https://www.practicalmachinist.com/forum/threads/developer-looking-for-help-understanding-how-small-shops-track-work.447345/
- NMPro om planteskoler: https://www.nurserymag.com/article/playing-matchmaker
- Tourwriter-case: https://www.tourwriter.com/huellas-e-travel-2/
- ProZ om oversætter-PM: https://guj.proz.com/forum/translation_project_vendor_management/363967-best_pm_solution_for_micro_business.html
- Nimdzi 100: https://multilingual.com/nimdzi-100-top-5/
- Source.One WhatsApp: https://business.whatsapp.com/resources/success-stories/sourceone
- Archdesk om bid leveling: https://archdesk.com/blog/guide-to-subcontractor-bid-leveling
- Dwellrs: https://www.producthunt.com/products/dwellrs
- Flere links står i tabellerne ovenfor.
