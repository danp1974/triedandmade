---
title: "Under-Extrusion: Gaps, Thin Walls, and a Clicking Extruder — Fixed in Order"
category: "3D Printing"
description: "Gaps between lines, walls you can see through, an extruder that clicks like a turn signal — under-extrusion has six causes and they're easy to tell apart. Work the list."
author: "Danny"
date: "2026-06-14"
---

## The Starving Printer

Under-extrusion is exactly what it sounds like: the printer isn't pushing as much plastic as the slicer asked for. You see it as gaps between lines, walls thin enough to see light through, weak parts that crumble along layers, missing chunks — and very often you *hear* it first, as a rhythmic click-click-click from the extruder. That click is the extruder motor losing its fight against something and skipping back.

Something is restricting flow. There are six suspects, and they check fastest-first. Work the list in order.

## 1. Partial Clog (Check This First)

The most common cause by far. Not a full jam — a partial blockage, usually carbonized plastic built up inside the nozzle, choking flow down without stopping it.

**The test:** heat the nozzle and manually push filament through (most printers have an extrude command in the menu). It should flow out in a straight, smooth stream. If it curls hard to one side, sputters, or takes real force to push — partial clog.

**The fix:** a cold pull. Heat to printing temp, push filament through, let the hotend cool to ~90°C for PLA (~120°C for PETG), then pull the filament out firmly. The cooled plug drags the gunk out with it — you'll see the dirt molded into the tip. Repeat until the tip comes out clean.

If cold pulls don't hold, just replace the nozzle. Brass nozzles cost a dollar or two — they are consumables, not heirlooms. Anyone who's run machine tools knows you don't nurse a worn cutter, and the same logic applies here.

## 2. The Nozzle Is Worn Out

Speaking of consumables: if you print abrasive filaments — anything with "carbon fiber," "glow," "wood," or "metal-filled" on the label — a brass nozzle wears out *fast*. Sometimes in a single spool. The opening erodes wider and out-of-round, and extrusion gets inconsistent and gappy no matter what you do.

If you've ever run abrasives through a brass nozzle, replace it now and switch to hardened steel for those materials. If you only print standard PLA/PETG, brass still wears — just over many months instead of days.

## 3. Wet or Bad Filament

Wet filament doesn't just string (covered in my [stringing guide](/guides/3d-print-stringing/)) — the moisture turns to steam in the nozzle and the resulting flow is inconsistent: pops, gaps, weak extrusion. If your prints declined slowly over weeks with no settings changes, dry the spool before touching anything else.

Cheap filament adds a second problem: diameter that wanders. Filament that's supposed to be 1.75 mm but swings between 1.65 and 1.85 will under- and over-extrude along the same print. Measure a few spots with calipers. If it's all over the place, the fix is a better spool — no setting compensates for inconsistent plastic.

## 4. The Extruder Itself

Open up the extruder and look at three things:

- **The drive gear teeth:** packed with ground filament dust? Brush them clean — clogged teeth can't grip.
- **Idler tension:** too loose and the gear slips on the filament; too tight and it crushes a flat into it. You want firm grip with visible tooth marks, not a crushed ribbon.
- **The idler arm:** on a lot of budget extruders the plastic lever arm *cracks* and the failure is nearly invisible — a hairline at the pivot. Tension feels normal, grip is gone. If your printer has the stock plastic extruder and you've been printing for a year, inspect it closely. An all-metal replacement is cheap insurance.

## 5. Calibration: E-Steps and Flow

If the hardware all checks out, the printer may simply be told to push the wrong amount.

**E-steps (do once per extruder):** mark 120 mm of filament from the extruder entry, command 100 mm of extrusion, measure what actually went in. If it's not 100 mm, adjust the firmware's steps-per-mm proportionally. Ten-minute job, permanent fix. Any time you change the extruder — like when I converted my Ender 5 Plus to direct drive — e-steps must be recalibrated, because the new hardware moves a different amount per motor step. (I'm putting together a full calibration series that walks through e-steps, flow, and dimensional accuracy step by step — stay tuned.)

**Flow / extrusion multiplier (per filament):** after e-steps are right, fine-tune per material by printing a single-wall cube and measuring wall thickness against what the slicer intended. Adjust the flow percentage to match.

## 6. Printing Too Fast for Your Hotend

Every hotend has a ceiling on how many cubic millimeters of plastic it can melt per second. Ask for more — by printing fast with big layers — and the filament passes through before it's fully melted. The result is under-extrusion that *only shows up on fast sections* and gets worse the longer the print runs.

The test: cut your print speed 30% and reprint. If the gaps vanish, you found it. Either print slower, print cooler sections smaller, or upgrade to a higher-flow hotend.

## Calibration Numbers Are Worthless If You Lose Them

Notice how much of this list ends in a number: e-steps value, flow percentage per filament, max speed per material, which nozzle was installed. Those numbers are the difference between a tuned machine and a mystery machine — and they're exactly the kind of thing that lives on a sticky note until the sticky note disappears.

Your slicer embeds the flow rate, speeds, temps, and hundreds of other settings into every G-code file it saves. [3DPrintLogPro](https://triedandmade.com/shop) reads them all out automatically and logs every print, searchable, with success/fail status and your notes ("new nozzle installed," "flow recalibrated to 96%"). Six months from now, when prints look starved again, you check what the last good print ran instead of starting this guide from step one.

I wrote this guide from experience. I wrote the app from the same experience.

## Quick Reference

| Symptom | Most likely cause | Fix |
|---|---|---|
| Curled/weak stream from nozzle | Partial clog | Cold pulls, or new nozzle |
| Printed abrasives recently | Worn nozzle | Replace; hardened steel for abrasives |
| Slow decline, popping sounds | Wet filament | Dry it |
| Clicking, chewed filament | Extruder grip/tension | Clean gear, check idler arm for cracks |
| Consistently thin everywhere | E-steps/flow | Calibrate both |
| Gaps only on fast sections | Hotend flow ceiling | Slow down 30% to confirm |

---

Worked the whole list and still starving? [Email me](mailto:info@triedandmade.com) — I read every one.

— Danny
