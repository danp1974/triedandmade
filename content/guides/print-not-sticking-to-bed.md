---
title: "3D Print Not Sticking to the Bed? Fix It in Order, Not at Random"
category: "3D Printing"
description: "First layer won't stick? Here are the five causes in order of likelihood — and the one habit that keeps the problem from coming back."
author: "Danny"
date: "2026-06-14"
---

## We've All Been There

You start a print, walk away, and come back to a bird's nest of filament dragging around the bed. Or worse — the first layer looked fine, and you found out six hours in that it wasn't.

When this happened to me on my Ender 5 Plus, I did what everybody does: I changed five settings at once, the next print stuck, and I had absolutely no idea which change fixed it. Three months later the problem came back and I was starting from zero.

So here's the deal. There are really only five causes, and they fail in a predictable order of likelihood. Work through them in order. Change one thing at a time. And write down what you changed — more on that at the end, because losing track of what worked is its own problem.

## 1. Your Bed Is Dirty (Yes, Really)

This is the cause more often than everything else on this list combined, and it's the one everybody skips because it feels too simple.

Every time you touch the build plate, you leave skin oil on it. PLA will not bond through a fingerprint. A bed that "was fine yesterday" and won't stick today is usually just dirty.

The fix: wash the plate with warm water and a drop of dish soap, then dry it with a paper towel. Isopropyl alcohol between prints is fine for maintenance — but IPA smears oil around as much as it removes it. Soap and water is the reset button.

Handle the plate by the edges from now on. If a freshly washed bed fixes it, you're done. If not, keep going.

## 2. Your First Layer Height Is Wrong

This covers most of the rest. The first layer needs to be *squished* into the bed — not resting on top of it, and not scraped so thin you can see through it.

Watch your first layer go down and read it like this:

- **Lines look like round spaghetti with gaps between them** — nozzle too high. The plastic is being laid on the bed instead of pressed into it.
- **Lines are flat and slightly ironed together, no gaps** — that's correct. Leave it alone.
- **Lines are see-through, edges curling, nozzle clicking or skipping** — too low.

Adjust your Z-offset in 0.02–0.05 mm steps while the first layer is printing — most firmware lets you baby-step it live. Watch the line change as you turn the knob. Those two minutes will teach you more than any YouTube video.

Adjusting the Z-offset value in the positive direction will move the nozzle away from the bed; decreasing the Z-offset will bring the nozzle closer to the bed.

One more thing: if you're re-leveling constantly, the leveling isn't the problem. On the Ender 5 Plus, the bed rides on dual lead screws — if those get out of sync, no amount of corner-leveling will ever hold. Check the mechanics before you blame the settings. There are several printable jigs available on sites like [Thingiverse](https://www.thingiverse.com/) and [Printables](https://www.printables.com/) that can help align dual lead screws.

## 3. Bed Temp Too Low — or a Draft You Haven't Noticed

Plastic sticks to a bed that keeps it just soft at the contact point. Starting points that work:

- **PLA:** 60°C
- **PETG:** 75–85°C
- **ABS:** 100–110°C, and honestly, an enclosure

Here's the one people miss: airflow. I'm in Central Florida, and I spent years working in attics where even the slightest breeze through a soffit vent could give you chills in 140°F heat — your body reacts to moving air that fast. A heated build plate is the same way. A printer sitting in the path of an AC vent or a garage door draft will curl corners all day long with otherwise perfect settings. Block the draft — an enclosure, or even a cardboard box over the printer — and the problem disappears.

I picked up a simple fireproof enclosure tent — the kind that fits an Ender 5 Plus or CR-10 — and it made a world of difference. Definitely one of the better upgrades I've made.

## 4. First Layer Speed Is Too Fast

The first layer needs time to bond. If your slicer runs it at full speed, the plastic gets dragged before it grips. Think of it as more of a smear than a bonding layer.

Set first layer speed to 20–25 mm/s. Yes, it adds a few minutes to the print. A failed print adds hours.

While you're in the slicer, check two more first-layer settings: nozzle temp about 5°C hotter than the rest of the print, and bump your first layer height slightly above your normal layer height — if you're printing at 0.2 mm layers, try a first layer of 0.23–0.25 mm; if you're at 0.3 mm, try 0.33–0.35 mm. That little extra squish helps embed the first layer into the build plate. Most default profiles do this already — but if you've been tweaking settings for months, you'd be surprised what you've actually got in there.

## 5. Your Build Surface Is Worn Out — or Wrong for the Material

PEI sheets lose their grip over time. Thousands of heat cycles and scraper passes eventually polish the texture right off. If a plate that worked for a year slowly got worse, it's the plate. Not you.

And materials matter:

- **PETG on smooth PEI sticks TOO well** — it can rip chunks out of the surface on removal. Use textured PEI, or a glue stick layer as a release agent.
- **Glass beds** want a thin layer of glue stick or unscented hairspray for anything including PLA. Whatever you use, make sure it's a thin layer — too much causes issues with adhesion as well.

## The Part Nobody Tells You

Here's the trap waiting at the end of this guide. You wash the bed, fix the Z-offset, bump the temp, and slow the first layer — all in the same afternoon. The next print sticks. Great. *Which one fixed it?*

You don't know. I didn't either. That's how I ended up with sticky notes all over my desk and a drawer full of guesses.

Every setting I just talked about is already written into your G-code file — your slicer embeds all of it, around 356 settings in PrusaSlicer alone. I got tired of digging through G-code in Notepad to figure out what my last good print used, so I built [3DPrintLogPro](https://triedandmade.com/shop). It reads every setting out of every G-code file automatically, logs it in a searchable database, and lets you mark each print success or fail. When something works, you know exactly what "working" was — forever.

I built it because I needed it. If it saves you one roll of filament, that's why I made it.

## Quick Reference

| Symptom | Most likely cause | Fix |
|---|---|---|
| Stuck yesterday, not today | Dirty bed | Soap and water wash |
| Round lines with gaps | Nozzle too high | Lower Z-offset in 0.02 mm steps |
| Corners curling up | Bed temp or a draft | +5°C bed, block the airflow |
| Plastic drags instead of grips | First layer too fast | 20–25 mm/s first layer |
| Slow decline over months | Worn PEI sheet | Replace it |

---

Still stuck, or got a problem this didn't cover? [Send me an email](mailto:info@triedandmade.com) — I read every one.

— Danny
