---
title: "3D Print Stringing: How to Actually Fix It (Not Just Hide It)"
category: "3D Printing"
description: "Spider webs between every part of your print? Stringing comes down to four causes. Here's how to fix them in order — including the retraction numbers nobody gives you."
author: "Danny"
date: "2026-06-14"
---

## The Spider Web Problem

You print something with two towers, or a part with gaps in it, and every open space fills with fine hairs of plastic. You can burn them off with a heat gun. You can pick them off with pliers. But you shouldn't have to — stringing is the printer telling you something specific, and it's fixable.

Four causes, in order of likelihood. Same rule as always: change one thing, test, write it down.

## 1. Your Retraction Settings Are Wrong

Stringing happens when the nozzle travels between two points and plastic oozes out along the way. Retraction is the fix — the extruder pulls filament back before the nozzle travels, so there's nothing left at the tip to ooze.

The numbers depend entirely on one thing: whether your extruder is **Bowden** (motor on the frame, long tube to the hotend) or **direct drive** (motor right on top of the hotend).

**Starting points:**
- **Bowden:** 4–6 mm retraction distance, 40–45 mm/s retraction speed
- **Direct drive:** 0.5–2 mm distance, 30–40 mm/s speed

I learned this difference the hard way. My Ender 5 Plus came stock with a Bowden setup, and I was running 6 mm of retraction to keep it under control. When I converted it to direct drive with a Dragonfly hotend, I kept my old retraction settings — and the printer started clicking, jamming, and grinding filament. Direct drive needed less than 1 mm. Same printer, completely different number. If you've changed *anything* about your extruder or hotend, your old retraction settings are wrong now.

**How to tune it:** print a retraction test tower (free on Printables — search "retraction test"). It prints the same two towers repeatedly while stepping the retraction distance up. The level where the strings disappear is your number. Takes 30 minutes and ends the guessing forever.

## 2. Your Nozzle Is Too Hot

Hotter plastic is runnier plastic. Runnier plastic oozes. If retraction tuning got you 80% of the way and the last fine hairs won't go away, drop your nozzle temperature 5°C and reprint. You can usually go down 5–10°C from the filament's "recommended" temp before layer adhesion suffers.

A temperature tower (also free on Printables) tests this the same way the retraction tower does — one print, every temperature, pick the level that looks best.

## 3. Your Filament Is Wet

Filament soaks up moisture from the air, and wet filament strings no matter what your settings are. The dead giveaway: you hear faint popping or crackling at the nozzle, and prints that used to come out clean suddenly look fuzzy.

I'm in Florida. Leaving a spool out on the printer for two weeks here is the same as leaving it in a steam room. PETG and nylon are the worst offenders, but even PLA goes bad eventually.

**The fix:** dry the spool — a filament dryer is the easy way, or a few hours in an oven at the filament maker's recommended temp if you trust your oven's thermostat (many run hot, be careful). Then store spools in a sealed bin with desiccant instead of on the machine.


If your prints got stringier slowly over weeks with no settings changes — it's this one. Dry the spool before you touch a single setting.

## 4. Travel Settings Are Letting It Happen

Two slicer settings reduce how much ooze ever reaches your print:

- **Travel speed:** raise it. 150+ mm/s travel means the nozzle spends less time over open gaps. Fast travel literally outruns the ooze.
- **"Avoid crossing perimeters" / combing:** tells the slicer to route travel moves over the inside of the print instead of across open space. Any ooze lands where you'll never see it.

These don't fix the cause — they hide the symptom. Do them last, after retraction, temp, and dry filament.

## The Trap at the End

Here's what actually happens when someone fixes stringing: they tune retraction, drop the temp 5°, dry the spool, and bump travel speed — across four different test prints over a weekend. The strings disappear. Six weeks later they load a different brand of PLA and the strings are back, and they cannot remember what the winning combination was.

Every one of those settings is embedded in the G-code of every test you printed. Your slicer writes them all into the file — retraction distance, retraction speed, temps, travel speed, hundreds more. That's exactly why I built [3DPrintLogPro](https://triedandmade.com/shop): it pulls every setting out of every G-code file automatically and logs it with a success/fail status. Your retraction test isn't a memory anymore — it's a database row you can search next time a new filament starts stringing.

I built it after one too many weekends spent re-solving problems I'd already solved.

## Quick Reference

| Symptom | Most likely cause | Fix |
|---|---|---|
| Strings everywhere, always has | Retraction not tuned | Retraction test tower |
| Tuned retraction, fine hairs remain | Temp too high | Drop nozzle 5°C |
| Got worse over weeks, popping sounds | Wet filament | Dry the spool, sealed storage |
| Strings only across big gaps | Travel settings | Faster travel + combing |
| Started after a hotend/extruder change | Old retraction numbers | Re-tune from scratch |

---

Still stuck, or got a problem this didn't cover? [Send me an email](mailto:info@triedandmade.com) — I read every one.

— Danny
