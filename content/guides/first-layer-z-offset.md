---
title: "First Layer Too Squished or Too High? How to Read It and Fix Your Z-Offset"
category: "3D Printing"
description: "Your first layer tells you exactly what's wrong — if you know how to read it. Here's how to dial in Z-offset, fix elephant's foot, and stop re-leveling every other print."
author: "Danny"
date: "2026-06-14"
---

## The First Layer Is a Gauge, Not a Guess

Most people treat the first layer like a coin flip — sometimes it works, sometimes it doesn't, no idea why. But the first layer is actually the most readable diagnostic on the whole machine. It shows you, in plastic, exactly how far your nozzle is from the bed. You just have to know what you're looking at.

This guide covers reading it, fixing it, and the two related problems people confuse with it: elephant's foot and a bed that won't stay leveled.

## How to Read Your First Layer

Start any print with a big flat first layer and watch the lines go down. There are only three things you'll see:

**Too high.** The lines look like round cords laid next to each other with visible gaps between them. They didn't get pressed into the bed — they got placed on it. These prints peel off mid-print, or pop off when you breathe on them.

**Correct.** The lines are flattened, slightly ironed into their neighbors, no gaps, no ridges. The surface looks like one continuous sheet with a faint line pattern. The lines look like an oval with even flat top and bottom.

**Too low.** The lines are translucent and scraped thin. Edges ripple or curl up where the nozzle is plowing through plastic it already laid down. You might hear the extruder click — that's it skipping because plastic has nowhere to go.

That's the whole skill. Round cords with gaps: Z-offset needs to go down. Transparent and rippling: Z-offset needs to go up.

## Fixing It: Baby Steps, Live

Almost every printer firmware lets you adjust Z-offset *while the print is running* — Marlin calls it baby-stepping, Klipper has it in the console, most touchscreens have it under Tune.

Start a first layer, watch it, and adjust in **0.02–0.05 mm increments**. Watch the line change in real time as you step. Within one test print you'll land on the right offset, and more importantly, you'll have calibrated your *eye* — from then on you can glance at any first layer and know which way to go.

Once it's right, **save it** (Marlin: Store Settings; Klipper: SAVE_CONFIG). People dial in a perfect offset and lose it on the next power cycle constantly.

## Elephant's Foot Is Not a Leveling Problem

If your first few layers bulge outward — the bottom of every print flares like a bell — that's elephant's foot, and people chase it with leveling for weeks when it's actually heat and squish.

The bottom layers are getting compressed while they're still soft from the heated bed. Three fixes, try them in order:

1. **Slicer setting:** PrusaSlicer and OrcaSlicer have "elephant foot compensation" — shrinks the first layer outline slightly. Start at 0.2 mm.
2. **Drop the bed temp 5°C** after the first few layers (most slicers let you set a different "other layers" bed temp).
3. **Design it away:** if it's your own model, put a small 45° chamfer on the bottom edge. Machinists have been breaking edges forever for exactly this kind of reason — a sharp corner is always the first thing to deform.

## "I Have to Re-Level Constantly" — No, Something Is Loose

A properly working printer holds its level for weeks or months. If you're re-leveling every few prints, leveling isn't the problem — something mechanical is moving. Check in this order:

- **Bed screws and springs:** worn springs sag under heat cycles. Silicone spacers replace springs and hold adjustment far longer.
- **Eccentric nuts / V-wheels:** grab the bed and the gantry and try to wiggle them. Any play means the wheels need adjusting.
- **Dual lead screws out of sync:** on machines like my Ender 5 Plus where the bed rides on two screws, the screws can get out of step with each other — then the bed is *tilted* and no amount of corner leveling fixes it. Re-sync them per your printer's manual.
- **The plate itself:** a warped or dirt-speckled plate reads as "unlevel" to a probe.

An auto-bed-leveling probe (BLTouch, CR Touch, or the inductive probes on newer machines) doesn't replace fixing the mechanics — it measures the bed's shape and compensates. On a mechanically sound printer it's the difference between thinking about first layers and never thinking about them again.

## Write the Number Down

Here's the part that bites you later: your perfect Z-offset isn't one number. It changes with the plate (smooth PEI vs textured), the nozzle (every nozzle swap moves it), and sometimes the material. Three months from now, after a nozzle change, you'll be starting from scratch — unless you kept records.

Your slicer already embeds the first layer height, first layer speed, and temps into every G-code file it saves. I built [3DPrintLogPro](https://triedandmade.com/shop) to read all of it automatically — every setting from every file, logged in a searchable database with a success/fail mark on each print. When the first layer was perfect in March, you can pull up exactly what "perfect" was in June.

It started as a pile of sticky notes on my desk. The app is just the sticky notes, organized, with a search box.

## Quick Reference

| What you see | What it means | Fix |
|---|---|---|
| Round lines, gaps between | Nozzle too high | Baby-step down, 0.02 mm at a time |
| Translucent, rippled, clicking | Nozzle too low | Baby-step up |
| Flat, fused, no gaps | Correct | Save the offset! |
| Bottom of print flares out | Elephant's foot | Compensation setting, –5°C bed |
| Level won't hold | Mechanical, not leveling | Springs, wheels, lead screw sync |

---

Still fighting it? [Email me](mailto:info@triedandmade.com) what your first layer looks like — I read every one.

— Danny
