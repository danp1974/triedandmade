---
title: "Why Did My 3D Print Fail Halfway Through? Read the Wreckage"
category: "3D Printing"
description: "A print that dies at hour 9 left evidence behind. Spaghetti, a shifted layer, a clean stop — each failure looks different and points to a different cause. Here's how to read it."
author: "Danny"
date: "2026-06-14"
---

## The Worst Kind of Failure

A print failing in the first ten minutes costs you ten minutes. A print failing at hour nine of fourteen costs you a day, half a spool, and a little piece of your soul.

Here's the good news: a mid-print failure almost always leaves evidence, and each cause leaves *different* evidence. Don't clear the bed yet. Look at the wreckage first — it'll tell you which of these five things happened.

## 1. Spaghetti on Top of a Good Print: The Part Came Loose

If the bottom portion printed fine and then there's a bird's nest piled on top, the part detached from the bed (or from its supports) partway up, and the printer kept extruding into the air.

Tall narrow prints are the usual victim — the nozzle bumps the part thousands of times, and a small footprint eventually lets go. Fixes:

- Bed adhesion first — full walkthrough in my [bed adhesion guide](/guides/print-not-sticking-to-bed/)
- Add a **brim** for tall/narrow parts — more footprint, more grip
- In your slicer, enable **Z-hop on retract** so the nozzle lifts slightly during travels instead of dragging across the top of the part
- Check for **drafts** — a part that holds for 6 hours and lets go overnight often let go when the room temperature changed

## 2. The Print Shifted Sideways and Kept Going

Everything below a certain layer is perfect; everything above it is offset, like someone slid the top of the print over. That's a **layer shift** — the printhead or bed lost position and the printer, having no idea, kept printing in the new spot.

Causes, most common first:

- **Loose belt:** pluck the X and Y belts like guitar strings. They should give a low note, not flop. Tension them per your printer's manual.
- **Collision:** a curled-up edge or a blob of plastic that the nozzle slammed into hard enough to skip the motor. If you find one shifted layer right at a blob, that's your answer.
- **Loose pulley grub screw:** the tiny set screw holding the motor pulley works loose, and the pulley slips on the shaft. Check it with a hex key — this one is famous for causing "random" shifts.
- **Too fast / too hot motor drivers:** less common, but printing very fast in a hot enclosure can overheat stepper drivers, which skip when they thermally cut out.

## 3. Nothing Coming Out: Clog or Runout

The print stops getting plastic but the printer keeps moving — you come back to a half-finished part with the nozzle "air printing" above it.

- **Filament ran out** and you don't have a runout sensor. The fix is a runout sensor — most modern boards support one, and it pauses the print instead of killing it.
- **The spool tangled.** A loop slipped under another loop on the spool and pulled tight until the extruder couldn't win. This is almost always self-inflicted — it happens when a loose end was let go during a filament change. Keep the end clipped to the spool, always, and use a spool holder that turns freely.
- **Heat creep clog:** the hotend slowly jammed mid-print, usually on long prints with lots of slow sections. Filament softened too high up in the hotend and stuck. Check that the hotend cooling fan (not the part fan — the one on the heatsink) is actually spinning; a dying heatsink fan is the #1 cause. A cold pull clears the clog; replacing the fan stops it from coming back.
- **Ground-down filament:** look at the filament at the extruder — if there's a chewed divot, the extruder gear ground through it after the clog started. Clear the clog, snip past the damage, and brush the gear teeth clean.

## 4. It Just... Stopped. Cleanly.

The print ends mid-layer with no spaghetti, no shift, no grinding — like someone hit pause and never came back.

- **Thermal runaway protection tripped.** The firmware saw the hotend or bed temperature misbehaving and shut down on purpose. That's the printer protecting your house — take it seriously. Usual culprits: a loose thermistor, a failing heater cartridge connector, or a part-cooling fan blowing across the nozzle harder than the heater can fight. Spent enough years around HVAC controls to tell you: when a safety cuts equipment off, the safety is rarely the problem. Find what tripped it.
- **Power blip.** Florida summer storms ask your printer a question every afternoon. Some printers have power-loss recovery; a small UPS is better.
- **The computer fell asleep.** If you print over USB from a PC or laptop, the PC sleeping kills the print. Print from SD/internal storage, or run a dedicated Pi with OctoPrint — that's how I run mine, and it also gives you a camera to check on prints remotely instead of wondering all day.

## 5. It Failed at the Exact Same Height. Twice.

If the failure repeats at the same layer every attempt, stop blaming hardware — it's the **file**. A bad layer in the model or a slicer hiccup at that Z height. Re-slice the model; if it still dies there, run the STL through a mesh repair (most slicers have one built in) or re-export it. A corrupted SD card does this too — re-copy the G-code or try another card.

## The Question That Actually Matters

When a long print fails, the first question is "what happened?" — that's what this guide is for. The second question is the one that saves the *next* fourteen hours: **"what settings was I running the last time this exact print worked?"**

Most people can't answer it. The G-code file knows — your slicer wrote every setting into it, all several hundred of them — but nobody's digging through G-code in Notepad at 11pm. That's why I built [3DPrintLogPro](https://triedandmade.com/shop). It reads every setting out of every file automatically and logs each print as a success or failure. When something dies at hour nine, you pull up the last success, compare, and see exactly what changed. The Folder Watcher even logs every file your slicer saves without you lifting a finger.

I built it standing next to a failed overnight print, holding a sticky note that didn't have the answer on it.

## Quick Reference

| The wreckage | What happened | Fix |
|---|---|---|
| Spaghetti on a good base | Part detached mid-print | Adhesion, brim, Z-hop |
| Top offset from bottom | Layer shift | Belts, pulley grub screws, collisions |
| Air-printing, no plastic | Runout, tangle, or clog | Runout sensor, check heatsink fan, cold pull |
| Clean stop, mid-layer | Thermal protection or power | Find what tripped it; UPS |
| Same layer every time | Bad file | Re-slice, repair mesh, re-copy card |

---

Got wreckage that doesn't match any of these? [Email me a photo](mailto:info@triedandmade.com) — I read every one.

— Danny
