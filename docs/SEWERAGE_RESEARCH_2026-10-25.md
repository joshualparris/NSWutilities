# Sewerage and toilet plumbing: evidence-led Repository Town design
PUBLIC research/specification, 25 October 2026. System **RT-SYS-003**. Existing parents **RTU-022–024** remain open; child task IDs **RTSW-001–028** are in SEWERAGE_TASKS.json.
**Research and proposed architecture, not a completed or deployed sewer simulation.** Electricity research is assigned to ChatGPT's dedicated electricity session; drinking-water research to Manus. This session owns the sewerage research documents only.

## Decision and next implementation
Use **Narromine as the provisional operational/network reference**, with a labelled synthetic sewer layout fitted to Repository Town. Use Uralla/Bundarra as gravity/pressure-system comparisons and Bermagui for treatment-plant visual context. This is the strongest reference in the small candidate set inspected, not a claim to have ranked every NSW town.
**Next implementation: RTSW-003**, inventory every fixture and property connection. Then reconcile the proposed water/power contract (RTSW-004) before coding a one-toilet-to-treatment vertical slice. Do not start by merely adding decorative underground pipes.

## 1. Candidate selection and evidence limits
Scores 0–3: 0 not found in this review; 1 limited; 2 useful; 3 substantial. A zero is not proof a document does not exist. Scores reflect accessibility and suitability in this investigation, not engineering approval.

| Candidate | Process description | Recent quantified operation | Network/catchment depiction | Failure/renewal evidence | Measured street inverts/pipe inventory | Total /15 |
|---|---:|---:|---:|---:|---:|---:|
| Narromine | 3 | 3 | 2 | 3 | 0 | 11 |
| Uralla | 3 | 1 | 2 | 2 | 0 | 8 |
| Bundarra (separate pressure scheme) | 2 | 1 | 2 | 1 | 0 | 6 |
| Bermagui | 2 | 1 | 1 | 1 | 0 | 5 |

Narromine's public council documents provide plant/process descriptions, reported flows and incident/catchment material [SW-S01/02]. Uralla's 2023 AMP describes six lift stations and extended-aeration treatment; Bundarra separately has 175 property pressure pods and passive ponds [SW-S03]. Those are historical descriptions, not verified 2026 asset counts. Bermagui publishes annotated process/monitoring images [SW-S04].
No candidate supplied a verified complete property-to-main invert/diameter survey in this investigation. Never turn a schematic line into an asserted real pipe route.

### Reference facts that constrain the scenario
The Narromine incident plan describes oxidation-pond treatment with a 4,000 EP planning basis, 160 ML effluent storage, irrigation hardware serving 45 ha and 11 collection pump stations [SW-S01, printed p5]. These are source-described assets, not game sizing instructions.
The 2025 report records 199.24 ML influent, daily mean 545.85 kL and maximum 1,694 kL; its reuse scheme is reported inactive since 2017 [SW-S02, pp9–10]. The same report records ten chokes/blockages without reported network overflows that year [p24]. Consequently a blockage need not cause an overflow, and visible irrigation hardware must not imply active reuse.
Use source-reported mean and annual total separately: rounded figures need not reconcile to the last litre. A zero daily minimum requires data-quality investigation before being interpreted as an actual zero sewage day. No high-frequency inflow series has been imported/calibrated here.

## 2. Existing Repo Town gap
Runtime baseline inspected: JoshMemory main b59ea0b, whose runtime source remains the RTU-001 baseline 19a13fe.
- household.js WATER.toilet is 0.03 abstract units, charged per awake-at-home hour rather than a real flush event.
- life.js utilitiesHour adds floor(0.8 * town water delivered) to one wastewater stock; a powered treatment plant removes up to 22 units hourly. Water used on gardens and water held in cisterns are not individually routed.
- Global pollution changes when the one stock passes a threshold. There is no property lateral, pipe elevation/capacity, manhole/wet-well storage, treatment residence time, pollutant mass or surface-spill volume.
- The general house builder adds a toilet prop without a dedicated flush action; the Farmhouse toilet is geometry. householdPanel lacks a dedicated toilet state/control.
- The existing sewage works is an educational treatment gallery, not a functioning hydraulic plant. Its generic biological/clarifier exhibits must not be relabelled as a real Narromine pond plant.
- Preserve the tested visitor route, separate water/sewage sites, save semantics, utility repair workflow and existing electrical dependencies.
See RTU-001 for all 234 property/site locations. This research does not claim every toilet has already been enumerated.

## 3. Required physical chain
For each connected property:
water supply -> isolating/inlet fitting -> cistern storage -> flush valve -> trapped toilet pan -> sanitary branch/stack -> property drain/inspection point -> property connection -> gravity main/manholes -> lift station if required -> pressure rising main -> further gravity/trunk sewer -> treatment -> effluent storage/approved reuse or discharge.
Ventilation is an air path with a gas/pressure role, not a second sewage outfall. S/P pan outlet geometry is an equipment choice, not a rule that all toilets require an extra trap downstream.
Maintain distinct nodes for basins, showers, baths, kitchen sinks, dishwashers and laundry. Blackwater and greywater may enter the same sanitary system; greywater reuse requires an explicit separate treatment/diversion scenario.
Off-sewer farms can use septic/onsite treatment only after a deliberately assigned service mode; onsite systems are not holes that delete sewage [SW-S17].

### Toilet behaviour
Use a finite cistern volume and distinct reduced/full flush command. Caroma 844710W is a documented example: 4.5/3 L, S-trap, bottom inlet, 410 mm pan height and 670 mm projection; its manufacturer label gives 3.5 L average and says it is not an accessible/ambulant fixture [SW-S06]. Do not install it as the only public accessible option. Generic WELS behavioural averaging is a rating convention [SW-S05], not a substitute for actual flush-event accounting.
States: ready, flushing, refilling, empty/insufficient-water, inlet-isolated, outlet-blocked, leaking, unavailable-for-maintenance. Use clear feedback and discrete events; sanitary detail remains discreet rather than graphic.
- A full stored cistern can supply a gravity flush after mains water loss. Refill then depends on actual delivered water and pressure.
- Ordinary gravity pans/cisterns need no electricity. Macerators, pressure pods and booster-dependent supplies are separately modelled equipment.
- A leaking inlet/flush valve can waste water continuously; metering occurs on actual supply withdrawal, not on pressing a button.
- Inadequate storage must not produce a normal flush or spawn water. Do not assume a partially filled cistern gives the same flush performance.
- Traps hold a seal; model dry/siphoned seal and poor venting as diagnosed failure states. Do not attempt compressible air/bowl CFD in the first playable version.
- Cistern residual volume, refill flow and flush duration require exact product testing or explicit synthetic parameters; the 4.5 L event volume is not proof of tank geometry or refill rate.

### Property plumbing and surcharge
Store branch/stack/downstream junction IDs, cover/invert levels, route geometry, connection ownership, inspection access, vent/trap state and service mode. Use roof-vent and inspection-point assets at plausible positions; no plumbing through doors or floating above floors.
Overflow relief gullies provide an external escape path under surcharge; they do not sanitise sewage or guarantee no indoor damage [SW-S10]. The NSW 2026 advisory discusses a 150 mm relationship to the lowest connected fixture [SW-S09]. Full standard compliance depends on more than one number; exact elevations and all applicable rules remain a design-verification task.
A reflux/backwater valve is distinct from a relief gully. A closed valve prevents selected backflow but also limits the property's ability to discharge; do not allow infinite internal storage. A stuck/obstructed ORG can change where a spill appears.
Use licensed-worker NPCs and inspection-based repairs; player tasks can report faults or organise repairs without presenting the simulation as plumbing installation instructions [SW-S08].

## 4. Collection hydraulics and pumps
Represent a directed hydraulic graph of real game-space routes, not just nearby-radius service. Nodes: fixture outlet, inspection junction, manhole, wet well, storage, treatment inlet, outfall. Edges: gravity lateral/main, pumped rising main, valve and explicit fault leak/inflow.
Every endpoint has stable ID, x/z and elevation datum. Manhole cover level is not pipe invert level. Gravity sewers fall between compatible invert levels; a flat game landscape still needs a declared synthetic underground elevation model and finite burial depths. Add a lift station where a gravity-only route is impossible. Never invent measured Narromine inverts.
Use actual internal diameter and material/roughness assumptions; DN is a nominal size. Vinidex's PVC-U DWV datasheet is a suitable non-pressure family reference, not the material specification for a pressure main [SW-S07]. Do not infer installed council brands.

### Proposed model tiers
1. **Playable conservative graph:** finite node/pipe storage, routed transfers bounded by source volume, destination acceptance, edge capacity and travel delay. Diagnosed obstructions reduce capacity; no negative volumes or disappearance.
2. **Free-surface approximation:** partially full circular section and Manning capacity for suitable gravity flow. In SI, Q=(1/n) A R^(2/3) sqrt(S); Q in m³/s, A m², R m. Convert to L/s once. S is a defined energy/grade approximation, not a magic map gradient.
   For diameter D and water depth y: theta=2 acos(1-2y/D), A=D²(theta-sin(theta))/8, wetted perimeter=D theta/2, R=A/perimeter. Handle dry and nearly full limits explicitly.
3. **Surcharge/backwater:** the simple grade-capacity approximation is insufficient. Use an explicitly labelled storage/backpressure surrogate until validated against dynamic-wave fixtures, or integrate a validated solver. Reverse flow requires hydraulic heads and constraints, not reversing every arrow randomly.
These formulas describe the proposed game approximation; parameter values and tolerances are not sourced Narromine calibration.

Pumping: wet-well volume/level, duty/standby availability, hysteresis (start above stop), maximum starts, pump curve/system-head intersection, nonreturn/isolating valve state, electrical consumption, faults and maintenance. Choose an actual manufacturer curve before assigning a model; Grundfos is currently a mechanism reference, not an installed pump identification [SW-S14].
Pump electrical load should use P=rho*g*Q*H/efficiency (W with Q m³/s); efficiency is not assumed 100%. Power loss stops the affected pump, not upstream gravity flow. Storage fills, alarms arise and only then does surcharge/spill occur if capacity is exhausted.
Emergency generators require finite fuel, startup/connection delay and compatible capacity. Telemetry/alarms can have their own backup state. Returning power does not instantaneously empty a flooded catchment.

## 5. Treatment and environmental consequences
Choose a declared process scenario:
- **Narromine-inspired baseline:** pond treatment and effluent storage with residence-time/quality abstractions; reuse equipment can be installed but inactive.
- **Existing generic visitor gallery:** retain as educational comparison or adapt labels with evidence; do not pretend its clarifier represents every pond system.
- **Optional Uralla activated sludge or Bundarra pressure/pond branch:** separate scenario, never combine their equipment into an asserted Narromine configuration.
Track water volume, suspended solids/organic load (initially one explicit tracer if needed), solids/sludge exported, effluent held and any released mass. Biological removal/conversion, settling and evaporation require stated equations/coefficients; untreated sewage must not simply vanish as “22 units processed.”
Effluent safety is not a boolean clean-water flag. Use quality gates for proposed reuse/discharge and log failures. Onsite systems require finite tanks, site constraints, desludging and explicit disposal destinations.
Cafés/pubs and food processing require waste-stream-specific trade-waste pretreatment; workshops/industry cannot dump arbitrary chemicals into domestic drains [SW-S15]. Model grease accumulation, maintenance and authorised disposal rather than automatically routing all liquids to sewer.
Blockage mechanisms can include unsuitable solids, grease and roots [SW-S16]. Rainfall-derived infiltration/inflow enters through explicitly faulty connections/joints/manholes, while ordinary stormwater remains RT-SYS-004. Do not model every rainy day as a combined sewer.
Pond water balance can include rainfall/evaporation as separate inputs/losses; those are not household wastewater.

## 6. Water/electricity integration proposal (coordinate with owners)
Use simulation time and SI units at boundaries. Do not edit Manus's water model without reconciliation.
- Water request: requestId, fixtureId, propertyId, desiredLitres, purpose, timestamp. Reply: actualDeliveredLitres, pressureKPa, quality/source tag, committed meter transaction ID.
- Fixture event: eventId, fixtureId, timestamp, actualOutletLitres, pollutantMassG and downstreamNodeId. Repeated IDs do not debit/emit twice.
- A toilet refill debits water and increases cistern storage; its later flush transfers stored volume into sewer. Water supply and wastewater discharge can occur in different intervals.
- Return every withdrawal to one of: stored fixture water, sewer discharge, garden/consumptive use, evaporation/leak or other explicit destination. Remove the old global 80% sewer contribution for consumers migrated to events; never run both.
- Power query: assetId/serviceId, availableKw, energised and simulation timestamp. A temporary legacy adapter can map pump assets to the existing sewage customer, labelled aggregate approximation.
- Outage events: asset state transition, cause, detection time, affected hydraulic catchment and finite repair order. Stable property keys H:/B: remain unchanged.
- Save/replay: snapshot cisterns, wet wells, pipes in transit, treatment/storage/sludge, closures/blockages, event-deduplication state and random seed. Advance deterministic substeps during sleep/time acceleration; no skipping stored wastewater.
- Proposed timestep: fixture events in seconds; hydraulic substeps initially 1–10 simulated seconds with stability testing; treatment summary about 5 simulated minutes. These are starting design choices, not measured real solver performance.

## 7. Data contract
Proposed fields, not a completed JSON Schema:
- asset: id, type, systemId=RT-SYS-003, propertyId, sourceIds[], provenance(documented/inferred/synthetic), confidence, asOf, x/z/elevationM, modelVersion.
- fixture: productId or generic class, accessibleSuitability, supplyNodeId, cisternCapacityL, storedL, full/reducedFlushL, inletState, refillModel, trapSealState, wasteNodeId.
- node: invertM, coverM, storageCurve, volumeL, headM, surfacePondingL, pollutantMassG.
- edge: from/to, route[], lengthM, internalDiameterM, roughness, pressureClass/material, capacityModel, transitVolumeL, blockageFraction, valveState, ownership.
- pump: wetWellId, duty/standby group, verified curve reference, start/stop levels, efficiency curve, powerAssetId, actualKw, availability.
- treatment: processScenario, stage volumes, residence-time/quality state, solids store, effluent store, reuse permission and outlet state.
Reject NaN, duplicate IDs, unknown connections, inconsistent units, inverted elevations for claimed gravity edges, negative volumes, impossible fill, undocumented real coordinates and pressure-main material mismatches.

## 8. Conservation and update algorithm
At every substep:
1. Consume committed water-delivery transactions into fixture stores.
2. Apply unique fixture actions; transfer only available water to downstream node.
3. Assemble gravity/pump transfer proposals from previous-state levels; limit concurrent transfers so no node is overdrawn.
4. Transfer water and pollutant mass together. Apply leakage, spill and infiltration to named ledgers, not clamped-away negatives.
5. Advance treatment/pond/storage and record effluent/solids/evaporation destinations.
6. Evaluate levels, blocked service, alarms, repair consequences and UI.
7. Check conservation, publish immutable readings, save event log.
Water balance: initial storage + delivered fixture inflow + infiltration + pond rain = final storage + legal effluent exports + tankered exports + surface spills + evaporation + explicitly modelled seepage. Transfers between nodes are internal and cancel.
Pollutant balance separately accounts for reaction/transformation and sludge removal; water conservation does not prove biological quality.
Tankering transfers wastewater into finite vehicle capacity and a receiving disposal account; it is not deletion.

## 9. Actual solver code audit and reuse
EPA SWMM is an engineering hydraulic reference, not a town game. Inspected commit **07c371f8a0d477da1d9d4e7c0d75719664f62fec** [SW-S13]:
| File | Functions inspected | Relevance |
|---|---|---|
| src/solver/dynwave.c | dynwave_init, dynwave_getRoutingStep, dynwave_execute | Picard-based continuity/momentum routing, timestep control |
| src/solver/dwflow.c | dwflow_findConduitFlow | Individual conduit momentum and surcharge handling |
| src/solver/flowrout.c | flowrout_init/getRoutingStep/execute | Routing-model selection |
| src/solver/node.c | node_getDepth/getVolume/getMaxOutflow/getSystemOutflow | Storage, depth and outflow limits |
| src/solver/massbal.c | massbal_open/report/addInflowFlow | Explicit water/quality accounting |
The official README states the C solver is public domain. Check extern dependencies and wrappers separately; the EPA name/logo does not imply endorsement. No source code copied in this deliverable.
**Recommendation:** begin with a conservative browser graph plus offline SWMM benchmark fixtures. A browser/WASM port is an evaluation task, not assumed necessary or already working. SWMM can model sanitary routing and surcharge [SW-S11]; it is not the whole biological treatment/fixture engine. Reference/manual versions and exact input files must be pinned in the benchmark implementation [SW-S12].

## 10. In-world presentation and play
Sewer overlay: dim terrain/buildings; reveal sanitary routes, slope/invert profile, manholes, wet wells, pumping arrows, rising mains, treatment/effluent/sludge paths and affected catchment. Never show storm drains as sewer connections unless the inspected scenario explicitly identifies a faulty cross-connection.
Toilet cutaway: supply pipe -> finite cistern -> pan trap -> branch -> property connection; Show/Hide, reduced/full flush, refill indication and a short non-graphic flow trace. Make repeat-click and unavailable-water feedback clear.
Street clues: slow drains, a service alarm, a discreet external spill, closed public toilet, a crew vehicle and restored service. A reported blockage is diagnosed before pipes are excavated; routine maintenance can prevent failure.
Gameplay: report a blocked toilet, inspect a surface access point safely, book a plumber, fund a repair, arrange a finite-capacity tanker, restore a pump, verify downstream recovery. No player entry into wet wells/manholes or instruction to handle sewage.
Keep settings/inspection controls usable on touch screens; never make the player manage hundreds of individual flushes to keep NPCs alive. NPC daily routines generate household events while the player can inspect and intervene.

## 11. Acceptance suite required before feature completion
- One real 4.5/3 L event fixture: each click produces exactly the chosen declared volume once; no negative cistern storage.
- Mains off with filled cistern: remaining supported flush works; refill cannot occur without actual delivery.
- Electrical blackout: gravity flow continues; only powered assets stop. Wet-well reserve delays failure.
- Property blockage versus trunk blockage produces different affected areas; low relief path versus obstructed relief gives different spill locations.
- Duty pump failure switches to available standby with finite capacity; high-level alarm and telemetry outage are distinct.
- Rain/infiltration increases sewer load only through declared mechanisms; roof runoff stays separate.
- Deliberate overflow, leakage and tanker removal conserve water and pollutant mass.
- Treatment cannot export fresh drinking water; inactive reuse stays inactive until a scenario explicitly enables it.
- All 234 existing registered locations have connected/onsite/no-fixture/unresolved status; no silent “connected” default. Fixtures, not property counts, determine discharge.
- Duplicate events, save mid-flush, refill, sewage in transit, wet-well high level and repair/reload match uninterrupted simulation.
- Closed/toilet-out-of-service cues, sounds, overlay routes and visible fixture dimensions are tested in desktop and Android-size gameplay.
- Proposed numerical acceptance: bounded non-negative stores, explicit balance residuals, analytic simple-pipe fixtures and comparison of delay/peak/storage/surcharge to pinned SWMM reference cases. Numeric tolerances must be chosen and justified before accepting the surrogate.
- Performance target to measure: about 234 service locations, 1,000 hydraulic elements, 1-day accelerated run with deterministic output; no continuous synchronous hydraulic solve blocking a mobile frame. Runtime budget is a target, not benchmark evidence.

## 12. Uncertainty, standards and public evidence
Not established: real street inverts/diameters/pump curves; high-resolution Narromine inflow; current reuse status after the 2025 reporting year; complete updated 2026 Uralla/Bundarra assets; per-house fixtures and NPC usage distribution; contaminant kinetics; exact product refill data; actual runtime accuracy/performance.
The regulator advisory explicitly discusses a 2026 standard edition, while other public pages contain older references. Pin the actual project-adopted PCA/AS/NZS versions before asserting normative compliance. This document does not reproduce/paywall-bypass standards or provide a certified installation design.
Use publicly disclosed diagrams for evidence only. Keep unavailable routes/sizes synthetic. Do not republish third-party map imagery, CAD files, private access/contact details or operational control data.
Brand references are illustrative source-backed assets, not statements that councils installed those products. Obtain reuse permission or create original geometry before shipping manufacturer models.
Sources and precise locators are in SEWERAGE_SOURCES.json; any source labelled “identified” still requires the detailed review stated there. This is a substantial scoped investigation, not an exhaustive national asset survey or a calibrated town twin.
