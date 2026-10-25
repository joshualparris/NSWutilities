# Pub simulation release — 26 October 2026

Runtime source: `4718823f47c70a0f20407005009471f66af6430a`.
Content fingerprint: `def06d2a86accb99f164d77306e11115a500f02b8fe9a5025e5a3f43539184d2`.
Canonical change: https://github.com/joshualparris/JoshMemory/pull/219.
Playtest: https://parris-tech-services.github.io/Repository-town-playtest/qa-tests/pub-compliance.html?v=4718823.
Direct game: https://parris-tech-services.github.io/Repository-town-playtest/qa/pub-compliance-20261025/.

The final candidate has 39 registered seats, revised sampled door sweeps, a clear rear exit, a wall-aligned TV, collision-blocking lowered bar, powered/coasting fans, pub uniforms and physical drink/plate/tray service. Material accounting covers beer, bottles, glasses, plates, washing and finite supplier deliveries. Pool has playable fixed-step ball physics and simplified two-player house rules; Keno is a free scheduled educational draw without money or prizes. Onsite simulated RSA/RCG records gate service. Twelve schematic utility layers distinguish independent service paths.

Local final source passed pub venue/physics/layout/stock/negative-timestamp regression, formal source-audit validity, preserved 1.2 m design-route checks, 45-interior and seating tests. Desktop and phone emulation passed pool shots, scheduled Keno draws, real menu alcohol purchase and physical service progression with zero page errors. Privacy scanned 798 files against 1116 private markers and the manifest verified 1163 files. The final source's full release gate also passed in GitHub Integration, including all five 28-day simulation seeds.

Formal building/fire/access/structural/food/electrical/gas/licensing compliance is **not certified**. The conservative 24-patron gameplay limit remains separate from the 39 furniture places. No extra storey or cellar was needed for this seating pass; no structurally/accessibly designed new storey is claimed. Utilities remain engineering approximations, with calibrated pressure/power-flow/RF and concurrent articulated staff tasks open under PUB-SIM-011–013. The source evidence registry and detailed acceptance tasks are in PUB_SIMULATION_2026-10-26.md. An automated simulated inspection issues no real approval.

This is isolated QA publication, not a claim that the separate Vercel production alias was promoted. The retired root handover and approved production backup are preserved.

## Completed acceptance evidence

Merged as `e69ca6f02197ed9290dfe942f12d6d1b08f5bcfb`. All seven PR workflows passed at the runtime source: [Integration and five seeds](https://github.com/joshualparris/JoshMemory/actions/runs/40237440744), [recorded WebGL](https://github.com/joshualparris/JoshMemory/actions/runs/40237440734), [pub physical walkthrough](https://github.com/joshualparris/JoshMemory/actions/runs/40237440738), [envelope](https://github.com/joshualparris/JoshMemory/actions/runs/40237440716), [mobile driving](https://github.com/joshualparris/JoshMemory/actions/runs/40237440722), [heritage](https://github.com/joshualparris/JoshMemory/actions/runs/40237440717), [audit validity](https://github.com/joshualparris/JoshMemory/actions/runs/40237440770).

[Publisher attempt 2](https://github.com/Parris-Tech-Services/Repository-town-playtest/actions/runs/40237466640/attempts/2) and [actual hosted acceptance](https://github.com/Parris-Tech-Services/Repository-town-playtest/actions/runs/40238413993) both passed. The first publisher attempt missed the eight-second rear-exit deadline; independent source walkthrough and repeated desktop/phone navigation passed. No teleport or bypass replaced the keyboard exit assertion.

Additional local checks against the real public URL verified the exact source/fingerprint, pool, scheduled Keno, menu purchase, visible pouring/carrying and meal service, zero page errors, then header-free automatic pub entry with an iframe at y=0 filling the viewport on desktop and phone emulation. After using the desktop HUD, the test explicitly clicks the game before keyboard interaction, as the documented controls require. Physical Android handset and human listening review are not claimed.

[Hosted phone pouring screenshot](https://github.com/joshualparris/JoshMemory/blob/main/repository-town/audit/pub/venue/hosted-phone-pour.png) and [hosted phone dish service](https://github.com/joshualparris/JoshMemory/blob/main/repository-town/audit/pub/venue/hosted-phone-dish.png) preserve the final visual evidence. PUB-SIM-001–010 have pilot-level acceptance evidence; the engineering and concurrent-service limits remain explicit under PUB-SIM-011–013. No formal PUB-CODE/RTPUB approval item has been ticked off by this release.
