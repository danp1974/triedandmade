---
title: "PETG Settings That Actually Work (And Why Yours Don't)"
category: "3D Printing"
description: "PETG promises strength and delivers blobs, strings, and chunks ripped out of your build plate — until you stop printing it like PLA. Here are the settings that work."
author: "Danny"
date: "2026-06-14"
---

## PETG Is Not Hard. It's Just Not PLA.

Everybody's first PETG print goes the same way. You hear it's stronger than PLA, more heat resistant, great for functional parts. You load it, keep your PLA profile, bump the temps because the spool says so, and hit print.

What you get: strings like a haunted house, blobs welded to the print, and — if you're really lucky — a chunk of your PEI sheet ripped clean off when you remove the part.

PETG fails when you print it like PLA. It's a different material with different rules, and once you set it up right, it's one of the most reliable filaments there is. Here's the full setup.

## The Settings

**Nozzle: 230–245°C.** Start at 235. Too cold and layers don't bond (PETG's whole reason for existing is layer strength). Too hot and it strings and blobs worse.

**Bed: 75–85°C.** PETG wants a hot bed and holds onto it hard — which leads to the next point.

**Protect your build plate.** This is the one nobody warns you about: PETG bonds to smooth PEI *too well*. It can tear the coating off the sheet when you remove the part. Two options:
- Use a **textured** PEI sheet — the texture limits contact area and parts pop off when the bed cools.
- On smooth PEI or glass, put down a thin layer of **glue stick or unscented hairspray** first. It's not for adhesion — it's a *release layer* so the part lets go.

**First layer: back OFF the squish.** Opposite of PLA. PETG hates being smushed into the bed — it wads up around the nozzle and drags blobs across the print. Raise your Z-offset slightly from your PLA setting (about 0.02–0.04 mm) so the first layer is laid on rather than pressed in. The hot bed does the gripping.

**Speed: slow down.** 40–50 mm/s for outer walls. PETG is thicker and lazier than PLA out of the nozzle; give it time. Modern fast printers with input shaping handle more, but if you're troubleshooting, slow is where you start.

**Fan: 30–50%, not 100%.** Full cooling kills PETG's layer bonding — parts snap along layer lines. Run 30–50% for general printing; go up only for bridges and overhangs (most slicers let you set a separate bridging fan speed). For maximum-strength parts, run even less fan and accept slightly softer details.

**Retraction: tune it again.** Your PLA retraction numbers are wrong for PETG. It's stringier by nature — expect to add a little distance and reduce nozzle temp before chasing perfection. (Full process in my [stringing guide](/guides/3d-print-stringing/).) Also expect *some* fine wisps no matter what. That's PETG. A two-second pass with a heat gun clears them.

## Dry It. Seriously.

PETG drinks moisture out of the air faster than almost anything except nylon. Wet PETG pops and crackles at the nozzle, strings uncontrollably, and prints cloudy and brittle.

I live in Florida. A spool left out here in the open is compromised in under two weeks — I've watched the same spool go from clean prints to fuzz with zero settings changes. If your PETG printed fine a month ago and looks bad now, dry it before you touch one setting.

A filament dryer pays for itself the first time it saves you from re-buying a "bad" spool that was just wet. Store spools in a sealed bin with desiccant between uses.

## What PETG Is For (And Not For)

Worth knowing what you bought:

- **Use it for:** brackets, clips, enclosures, outdoor parts (UV-resistant), anything near heat that PLA would sag in, parts that flex slightly instead of snapping. Most of the printed fixtures and brackets around my shop are PETG.
- **Skip it for:** fine miniatures and sharp detail (PLA wins), parts needing zero stringing cleanup, anything you'll sand and paint (PETG sands gummy).

One of the most useful PETG prints I've done are the little clips that hold the metal hooks on pegboards. In one of my shops, which is not air conditioned, I have both walls lined with pegboard and every single hook or holder has a printed PETG clip to stop the hooks from moving when I remove a tool. It's the simple things that make life a lot easier. I got the design from [Thingiverse](https://www.thingiverse.com/) — search "pegboard hook clip" and you'll find a dozen versions.

## One Profile Per Brand — and Keep the Receipts

Here's the thing about PETG that makes record-keeping matter more than with PLA: brands vary wildly. One brand's PETG runs perfect at 235°C; another strings until you hit 228. You will end up with a different tuned profile for every brand on your shelf, and six months from now you won't remember which was which.

Every one of those tuned profiles is already written into the G-code files you printed with. [3DPrintLogPro](https://triedandmade.com/shop) reads them all out automatically — temps, retraction, speeds, fan, all of it — and logs each print with its filament brand and a success/fail status. Reload a brand you haven't run since spring, search it, and you're printing on a proven profile instead of starting over. You can even export the settings straight back out as a slicer profile.

That's the entire reason the app exists. I had the sticky notes to prove it.

## Quick Reference

| Setting | PLA habit | PETG reality |
|---|---|---|
| Nozzle | 200–215°C | 230–245°C |
| Bed | 60°C | 75–85°C |
| First layer | Squished in | Backed off — laid on |
| Fan | 100% | 30–50% |
| Smooth PEI | Fine | Glue stick release layer or textured sheet |
| Wet spool tolerance | Forgiving | Almost none — dry it |

---

Got a PETG problem this didn't cover? [Email me](mailto:info@triedandmade.com) — I read every one.

— Danny
