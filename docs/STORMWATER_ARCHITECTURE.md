# RT-SYS-004 — Stormwater and flood drainage simulation architecture

**Status:** Target architecture; no current Repository Town stormwater solver is verified. **Scope:** one fictional NSW-style small town, preserving 234 existing building/site candidate IDs. Real Dubbo counts are a comparison, not a fake pipe map.

## Fidelity tiers

**Tier 0:** existing landscape, weather and decorative drain grates; no verified routed network or measured hydraulics.
**Tier 1 (playable):** finite synthetic catchment volumes; explicit roofs, streets, inlets, pipes, swales, outfalls, detention and overland routing, isolated faults, affected buildings and maintenance; deterministic game time, balance ledgers.
**Tier 2 (validated reference):** EPA SWMM hydrology, pipe/node surcharge and LID on a *synthetic documented* benchmark; compare errors/time series, store pinned solver versions.
**Tier 3 (optional):** 2D topographic shallow-water/flood solver, dynamic river tailwater, sediment pollutant load and risk scenarios with field-calibrated parameter evidence. No safety, statutory or design certification.

## Separation of networks

Layer STORM: building roof/lot -> pit and street inlets -> conveyance -> outfall or detention. Layer SURFACE: overland water and ponding in road/landscape -> downstream water body. Layer SANITARY (RT-SYS-003): toilets, wastewater laterals and sewage pumps only, with explicit wet-weather I&I defect transaction. Layer POTABLE (RT-SYS-002): water supply and legally distinct rain tank/harvested stormwater supply. Riverine flood layer is separate exogenous receiving-water/tailwater/hazard boundary. Never imply a real pressure main or sanitary sewer is a storm drain.

## Canonical TypeScript design sketch

- Provenance: {evidence: documented | inferred | synthetic, sourceId?, asOfDate?, licence?, accuracy?, assumptions?}.
- Subcatchment: {id, areaM2, imperviousFraction, depressionStorageL, infiltrationModel, slopeFraction, surfaceRouteId, landcover, worldPolygon, evidence}.
- RoofOutlet: {id, buildingId, catchmentId, gutterId?, downpipeId?, rainTankId?, serviceMode: connected | onSite | unknown | notRequired}.
- StormNode: {id, kind: inlet | pit | junction | manhole | detention | GPT | wetland | culvert | outfall, worldX, worldZ, groundElevationM?, invertElevationM?, storedL, maxStoredL?, evidence}.
- StormEdge: {id, fromId, toId, kind: pipe | openDrain | swale | overflow | culvert | pumped, lengthM?, invertUpM?, invertDownM?, hydraulicCapLph?, available: boolean, obstructionFraction, evidence}.
- SurfaceCell: {id, areaM2, terrainElevationM, pondedL, spillRouteIds, permeabilityClass, buildingFloodThresholdM?, evidence}.
- RainSample: {scenarioId, utcTime, depthMm, durationH, evidence, sourceId?}; scenario label observed | design | synthetic.
- Snapshot: {tick, version, rainL, infiltrationL, evapL, harvestedL, outfallL, overflowToSurfaceL, surfaceExitL, storedL, pollutantMassKg?, serviceInterruptions, auditImbalanceL}.

## Units and conservation

Rain depth: mm; area: m²; 1 mm × 1 m² = 1 litre. Flows: L/hour for game, m³/s for SWMM/engineering comparisons (multiply L/h by 1/3.6e6); pipe diameter: mm, length and elevations: metres. Rain intensity mm/hour is NOT rainfall depth until multiplied by timestep hours. If a roof tank captures 10 L, remove the same 10 L from downstream runoff, not an additional 10.

Whole-domain liquid balance per tick (L):
  StorageBefore + Rain + ExternalUpstream + ApprovedImports
    = Infiltration + Evaporation + HarvestedConsumption + Outfalls +
      SurfaceExit + StorageAfter + ExplicitlyAccountedLeaks.
Transfers between catchments, pipes, tanks and surface cells **cancel** in the townwide ledger. Internal pit overflow is a transfer to SURFACE, not an extra terminal loss; distinguish report fields for internal transfers vs external sinks. Pollutant mass is a distinct ledger, with treatment captured solids and final destination, no invented disappearance.

Simple pipe **capacity estimates** may use Manning's Q=(1/n) A R^(2/3) sqrt(S), with area A, hydraulic radius R and energy slope S in consistent SI for appropriate open-channel/free-surface conditions. Capacity alone cannot predict surcharging, dynamically backwater-affected pipe pressures, surface depths or flow reversal. A full hydraulic solver is required to make such claims.

## Deterministic timestep and graph solver (Tier 1)

1. Input explicit rainfall *depth this timestep* (observed historical or labelled synthetic), upstream boundary and tailwater scenario; validate station/time provenance.
2. For each catchment, partition 100% of rainfall into on-site storage, infiltration, evapotranspiration, harvesting, and runoff. Surface depression storage and already-full tanks are stateful.
3. Route runoff to connected pits/open drains by actual directional graph and bottleneck remaining volume capacities. All uncollected excess becomes surface ponded volume with a visible location.
4. Release detention at configured outlet limit while conserving storage and respecting receiving-water high-level (modelled/observed tailwater must be declared).
5. Route overland along deterministic synthetic terrain gradient/waypoints; clamp finite water, avoid infinite round-robin graph circulation; if slope ambiguous retain pending ponded water with an unresolved-route flag.
6. Apply faults to pits/pipes/GPTs/pumps with timestamps; power is read from an immutable electricity snapshot; don't silently make all gravity pipes fail on blackout.
7. Send only explicitly scoped infiltration/inflow fault volumes to RT-SYS-003 sanitary solver. Rainwater tank extraction is a separate RT-SYS-002 transaction.
8. Publish immutable result to 3D scene, weather panel and maintenance workflow; assert ledger conservation and state bounds, persist seed/graph version/tick.

## Realism/quality hierarchy

- **Actual:** only published authorised and dated asset data; never claim individual Dubbo pipe locations or invert levels without source.
- **Inferred:** estimated catchment/runoff parameter with evidence and uncertainty.
- **Synthetic:** fictional streets, pit connections, drain directions and capacities built to fit Repository Town's own world.
- **Unknown:** missing service or GIS licence; fail explicit graph validation rather than invent a connection.
- **Design scenario:** ARR/BoM probabilities must not be presented as measured live weather. AEP is annual exceedance probability, not a forecast probability of street flooding.

## Interfaces and ownership

Stormwater parent system **RT-SYS-004**, child IDs **RTSM-001–030**; **RTU-022** preserves sanitary/stormwater separation and RTU-029/030 cross-fault/performance acceptance, not a competing RTSW implementation. RTSW sewerage owns toilets, sanitary mains and treatment. NSW-WAT owns lawful rainwater/harvesting intake to treatment/water use. NSW-ELEC owns power service of stormwater pumps/telemetry. RLT/roads and town geometry owners keep existing lighting/streets. Do not rewrite world files without COORDINATION claim.

## Required synthetic acceptance tests (all remain unverified until implemented)

1. 1 mm on a 100 m² catchment produces exactly 100 L prior to losses.
2. Half impervious/pervious catchments partition runoff, infiltration, storage without double subtraction.
3. 30-minute rainfall in mm/hour converts to correct mm and litres; no double multiplication.
4. Rain tank capture fills only remaining tank capacity, excess enters drainage, consumption debits once.
5. One blocked side-entry inlet causes surface ponding; nearby healthy inlet remains operative.
6. Single pipe closure only affects connected upstream catchments; directed bypass can restore.
7. Multiple branches sharing a pipe never exceed its throughput; excess remains stored/ponded.
8. Culvert/outfall tailwater restriction creates a correct backlog and not an invisible loss.
9. GPT litter capture affects pollutant ledger; doesn't magically drain or purify all water.
10. Retarding basin reaches storage capacity and sends excess to safe overland route.
11. Rain gardens/infiltration reduce total external outflow, but saturated soil limits new intake.
12. Unknown invert or catchment direction never silently assigned a factual grade.
13. All 234 site candidates have explicit stormwater service decision or unknown flag.
14. An electrical blackout affects a powered pump, not gravity-only swales/pipes.
15. Illegal direct potable/sanitary cross-connection is rejected; sewer I&I only via explicit defect.
16. Stormwater reuse demand is bounded by stored treated volume and a fictional permit.
17. Road crossing/flooded shop warnings follow synthetic threshold and reset on recession.
18. Day/night, dry spell, drought and intense rainfall have deterministic save/reload.
19. One month volume ledger has tolerance, zero NaN/negative stored litres and stable sorting.
20. Pin SWMM and compare event hydrographs, pipe surcharge timing and storage with documented tolerances.
21. Large 1,000+ synthetic catchment stress fixture respects target mobile FPS and CPU budget.
22. Actual deployed Repository Town desktop/Android gameplay demonstrates overlays, faults, repairs and 3D effect; verify exact deployed source SHA and screenshots.

No test passing is asserted by this document.
