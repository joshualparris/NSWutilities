# Cellar and upstairs pub release — 26 October 2026

PUBLIC fictional game implementation and verification record.

Runtime source: `46a3439e5204d856768e61842fa439a0d9b2c200`.
Content fingerprint: `6be3babae426edb93c44438833bd66bff6a3c7803e57d55435f0c26eae0e3dc0`.
[Core expansion PR #221](https://github.com/joshualparris/JoshMemory/pull/221), merged as `ff1a53115d2a4ee2e6546e746c100b334ea7bf2d`, preserves the concurrent pub ID controls from PR #220. [Window-clearance follow-up PR #222](https://github.com/joshualparris/JoshMemory/pull/222) corrects a side-window overlap found in actual gameplay screenshots; merged as `aaf4533d976ca12f3f73e80e5d54164ed5dee34b`.

[Play the expanded pub](https://parris-tech-services.github.io/Repository-town-playtest/qa-tests/pub-compliance.html?v=46a3439). The launcher has no introductory header and enters the pub automatically at lunchtime. Use E on desktop or Use on phone at the marked stair/lift landing. The compact floor control opens the passenger-lift panel. Existing saved utility faults remain meaningful: lift travel needs power; cellar entry needs extraction, monitoring and a cleared atmosphere alarm.

## Implemented

| Level | Playable contents |
|---|---|
| Ground | 19 registered seats, bar/bistro, kitchen, sanitary facilities, pool and original services |
| Upstairs, +4.8 m | 32 registered seats, dining, office, lift landing, main stair, refuge/staff assistance and separate rear escape stair |
| Cellar, −3.2 m | Kegs/chiller, finite visible wine racks, extraction, low-level gas monitor, alarm, hand basin and powered sanitary holding-tank pump |

The exterior has two actual above-ground storeys and aligned upper windows. Real floor/ceiling shaft openings, stair treads, stringers and rails replace an inaccessible decorative upper floor. The rear paved discharge route goes around the escape-stair annex. Ground seating was reduced from the earlier 39-seat layout to free circulation; 51 places across both occupied floors do not increase the existing whole-venue 24-patron gameplay cap or establish approved occupancy.

The timed passenger lift checks isolation, power and emergency state, cancels pending trips when its panel closes, and meters completed-trip energy. Stairs and exits remain available during blackout. Cellar hazards refuse entry while allowing occupants to leave. Finite wine transfers conserve stock and change actual rack contents; beverage-gas leakage/dispensing/exchanges conserve mass. The hand basin fills a finite holding tank, whose pump needs its own electrical and sanitary connections. LPG and beverage-gas cylinders stay outside.

## Verification

All seven source workflows passed at the exact runtime source: [integration/five 28-day seeds](https://github.com/joshualparris/JoshMemory/actions/runs/40261033453), [recorded 3D gameplay](https://github.com/joshualparris/JoshMemory/actions/runs/40261033483), [physical walkthrough](https://github.com/joshualparris/JoshMemory/actions/runs/40261033429), [building envelope](https://github.com/joshualparris/JoshMemory/actions/runs/40261033515), [mobile driving](https://github.com/joshualparris/JoshMemory/actions/runs/40261033526), [heritage](https://github.com/joshualparris/JoshMemory/actions/runs/40261033565), [audit validity](https://github.com/joshualparris/JoshMemory/actions/runs/40261033446). The physical workflow's first attempt timed out waiting for a WC button; its unchanged rerun passed. The independent publisher also passed that same walkthrough.

[Publisher 40261155778](https://github.com/Parris-Tech-Services/Repository-town-playtest/actions/runs/40261155778) passed full release, privacy, manifest integrity and desktop/phone compliance, venue, expansion and ID suites, then generated host commit `fa8304638cdc466d0906f2ae47f50021df9fbd62`. [Actual hosted verification 40261957076](https://github.com/Parris-Tech-Services/Repository-town-playtest/actions/runs/40261957076) passed all five browser suites against the public URL, including the header-free full-viewport launcher. Its log records the exact source and fingerprint above; both desktop and phone runs passed with zero page errors. Screenshots are retained in the publisher's pub gameplay artifact and the hosted run's completion artifact.

Local final desktop and phone-emulation expansion playthroughs passed: actual E/Use stair transitions, upstairs seating, office/lift isolation refusal, cancelled lift, successful timed cellar trip, finite wine transfer, hand washing, gas leak/alarm, exit and refused unsafe re-entry, purge/reset, blackout lift refusal, staff assistance and separate upper/cellar escapes. Walking after escape is asserted, guarding a real frame-lifecycle bug found and fixed during playtesting. Zero page errors were observed in those runs.

The final phone stair screenshot was visually inspected: the menu board no longer crosses the window. A Three.js bounding-box regression checks the menu, television and upstairs pictures against the side-window span. Actual colliders are sampled for all hotspots and 1.2 m design routes to vertical circulation and the separate exit.

Reproduce from the exact source:
```sh
npm ci
npm run build:release
node tools/check_privacy.mjs
node tests/pub-expansion.mjs
# Serve dist/public at localhost:8091, install Playwright Chromium, then:
node tests/pub-compliance-browser.mjs
node tests/pub-venue-browser.mjs
node tests/pub-expansion-browser.mjs
TOWN_URL=http://localhost:8091/ node tests/pub-id-browser.mjs
node tests/pub-launcher-browser.mjs
```

The publisher and hosted workflows record their exact commands, release identity and screenshot artifacts. Browser phone emulation is not a physical-handset sign-off. The supplementary local cancelled-trip/second-cellar-exit checks extend the committed baseline browser suite.

## Limits and remaining work

Stairs change between the engine's flat collision scenes at physical camera elevations; continuous 3D foot-by-foot stair climbing is not implemented. No full multi-floor waiter scheduler, office-reservations system, measured crowd-capacity assessment or calibrated pressure/airflow/phase-power solver is claimed. Utility diagrams remain schematic; per-floor alignment and calibration remain under PUB-SIM-011. PUB-SIM-011–013 stay open.

The synthetic lift, CO2 model, alarm thresholds, equipment sizes and refuge transfer are gameplay assumptions, not real engineering or safe-entry advice. Structural/excavation/waterproofing, fire compartmentation, accessible evacuation, ventilation, gas/electrical commissioning and business/licensing approvals require independent assessment. No formal PUB-CODE/RTPUB compliance item is certified by this release. The game has been published to the existing isolated QA path; the separate Vercel production alias has not been promoted.

Detailed primary sources, dimensions, formulas and stable task acceptance: [PUB_CELLAR_UPSTAIRS_2026-10-26.md](PUB_CELLAR_UPSTAIRS_2026-10-26.md). PUB-EXP-001–006 is complete within the declared game-model scope and this acceptance evidence. The cellar/upstairs scope is distinct from the outstanding whole-town utility programmes and professional approvals.

An optional additional TinyFish visitor run could not start because its wallet was out of funds; no TinyFish gameplay pass is claimed for this release. No billing changes were made.
