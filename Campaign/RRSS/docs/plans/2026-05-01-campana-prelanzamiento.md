# Bare — Pre-Launch Campaign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce all content, copies, and calendars for Bare's pre-launch campaign on Instagram and TikTok, targeting 200 waitlist signups in 3 months.

**Architecture:** 3 phases (Brand → Waitlist → Close) · 5 content pillars · Manifesto/Bold tone · FOMO with real numbers. All campaign copy is in English.

**Deliverables:** Copy documents, visual briefs, and week-by-week calendars ready for production.

---

## File structure

```
Campaign/RRSS/
├── docs/specs/2026-05-01-campana-prelanzamiento-design.md  ← approved spec
├── docs/plans/2026-05-01-campana-prelanzamiento.md         ← this file
├── Mes1-Marca/
│   ├── 01-brief-identidad-visual.md      ✓ done
│   ├── 02-copies-manifiesto.md           ✓ done
│   ├── 03-brief-teaser-ui.md
│   └── 04-calendario-semanas1-4.md
├── Mes2-Waitlist/
│   ├── 05-copies-explicativo.md
│   ├── 06-copies-fomo.md
│   ├── 07-copies-contraste.md
│   └── 08-calendario-semanas5-8.md
└── Mes3-Cierre/
    ├── 09-copies-urgencia.md
    └── 10-calendario-semanas9-12.md
```

---

## Task 1: Visual identity brief ✓

**File:** `Mes1-Marca/01-brief-identidad-visual.md` — completed.

---

## Task 2: Copy bank — Manifesto pillar ✓

**File:** `Mes1-Marca/02-copies-manifiesto.md` — completed.

---

## Task 3: Teaser UI brief

**File:** Create `Mes1-Marca/03-brief-teaser-ui.md`
**Use:** Month 1 (weeks 1–4) and Month 3 as urgency backdrop

- [ ] **Step 1: Create the brief**

```markdown
# Brief — Teaser UI Pillar

## Goal
Show Bare's interface to generate product desire without revealing real users.
Not a demo — a visual seduction.

## Screens to show (by impact order)

### Screen 1 — Empty search
The creator search view with visible filters: discipline, palette, technique, atmosphere.
No results loaded. Only the filter architecture.
Overlaid copy: "FILTER BY PALETTE. BY TECHNIQUE. BY ATMOSPHERE."

### Screen 2 — Blank profile
An empty creator profile, clean, with visible structure.
Projects as empty blocks. The portfolio architecture.
Overlaid copy: "YOUR WORK. ONE PLACE."

### Screen 3 — The archive
The curated inspiration module. Reference grid, no images.
Only the structure and metadata of one reference (palette, technique, context).
Overlaid copy: "INSPIRATION WITH CONTEXT. NOT ACCUMULATION."

### Screen 4 — The access
The review process screen. The project submission form.
Overlaid copy: "YOU SUBMIT A PROJECT. WE REVIEW IT. YOU'RE IN OR YOU'RE NOT."

## Visual treatment
- All screens in dark mode
- Convert to black and white if the design uses color
- Overlay text in campaign typography (Switzer SemiBold, #FAFAFA, uppercase)
- Add "bare" signature in Geist Light, bottom left corner

## Formats per screen
- 1 IG feed post (1080×1080px)
- 1 story/TK vertical (1080×1920px) — animated text over the screen

## Publishing cadence
- 1 Teaser UI per week in Month 1
- 2 Teaser UI in Month 3 (as urgency backdrop with closing copy)
- Never publish two on the same day
```

- [ ] **Step 2: Commit**

```bash
git add Campaign/RRSS/Mes1-Marca/03-brief-teaser-ui.md
git commit -m "feat: add teaser UI brief with screen priorities"
```

---

## Task 4: Month 1 Calendar (Weeks 1–4)

**File:** Create `Mes1-Marca/04-calendario-semanas1-4.md`

- [ ] **Step 1: Create the calendar**

```markdown
# Month 1 Calendar — Building Brand
## Weeks 1–4 · No waitlist CTA yet

Legend:
- [M] = Manifesto
- [UI] = Teaser UI
- [S] = Story

---

## Week 1 — Appearance

| Day | IG Feed | IG Stories | TikTok |
|---|---|---|---|
| Monday | [M] Copy A3 "BARE. COMING SOON." | [S] Black background, "bare" centered | — |
| Wednesday | — | [S] Typography detail of the logo | [M] A3 animated (5s) |
| Friday | [UI] Screen 1 — Empty search | [S] Zoom into the search | — |

*Week 1 goal: get the name Bare circulating without context. Pure intrigue.*

---

## Week 2 — Declaration

| Day | IG Feed | IG Stories | TikTok |
|---|---|---|---|
| Monday | [M] Copy A1 "NOT A PORTFOLIO..." | [S] A1 in vertical format | [M] A1 animated (7s) |
| Wednesday | [UI] Screen 2 — Blank profile | [S] Empty profile detail | — |
| Friday | [M] Copy A2 "ONE PLATFORM..." | [S] A2 vertical | [M] A2 animated (8s) |

---

## Week 3 — Depth

| Day | IG Feed | IG Stories | TikTok |
|---|---|---|---|
| Monday | [M] Copy A4 "GREAT WORK IS FINDABLE..." | [S] A4 vertical | — |
| Wednesday | [UI] Screen 3 — Archive | [S] Zoom archive metadata | [UI] Archive walkthrough (15s) |
| Friday | [M] Copy A6 "NO MINIMUM POSTING FREQUENCY..." | [S] A6 vertical | [M] A6 animated |

---

## Week 4 — Access (preview)

| Day | IG Feed | IG Stories | TikTok |
|---|---|---|---|
| Monday | [M] Copy A5 "YOUR WORK GETS IN OR IT DOESN'T..." | [S] A5 vertical | [M] A5 animated |
| Wednesday | [UI] Screen 4 — Access process | [S] "Next week, more." | — |
| Friday | [M] Copy A7 "ACCESS IS EARNED BY WHAT YOU MAKE..." | [S] 7-day countdown to "something" | [M] A7 animated |

*Week 4: start hinting something happens next week (waitlist opening). Don't say it explicitly — only the Friday Story with countdown.*

---

## Month 1 KPIs
- IG followers gained: target +250
- TK followers gained: target +150
- Total estimated reach: depends on starting point — log benchmark week 1
- IG engagement rate target: >4%
- TK engagement rate target: >6%
```

- [ ] **Step 2: Commit**

```bash
git add Campaign/RRSS/Mes1-Marca/04-calendario-semanas1-4.md
git commit -m "feat: add Month 1 content calendar weeks 1-4"
```

---

## Task 5: Copies — Explicativo pillar

**File:** Create `Mes2-Waitlist/05-copies-explicativo.md`
**Use:** Month 2 (weeks 5–8), IG carousel format and TK video

- [ ] **Step 1: Create copies**

```markdown
# Copies — Explicativo Pillar

## IG Carousel — "What is Bare and how access works" (7 slides)

**Slide 1 (cover):**
```
WHAT IS BARE
AND HOW ACCESS
WORKS.
```

**Slide 2:**
```
BARE IS A PLATFORM
FOR VISUAL CREATORS.

Inspiration archive.
Professional portfolio.
Contact directory.

One place.
```

**Slide 3:**
```
IT'S NOT OPEN.

To get in, you submit
a project.
A team reviews it.
You're in or you're not.
```

**Slide 4:**
```
WHAT DO WE EVALUATE?

The quality of the work.
The coherence of the proposal.
Nothing else.

Not your follower count.
Not your years in the field.
```

**Slide 5:**
```
ONCE INSIDE:

— Your portfolio organized
  by complete projects.

— An inspiration archive
  filterable by palette, technique
  and atmosphere.

— Direct contact with clients
  and other creators.
  No intermediaries.
```

**Slide 6:**
```
SEARCH WORKS
DIFFERENTLY HERE.

A client searches:
"Illustration · earth palette ·
hand process · calm atmosphere"

And finds exactly that.
Not the most followed profile.
The most precise work.
```

**Slide 7 (CTA):**
```
WAITLIST OPEN.
30 SPOTS THIS WEEK.

bare · link in bio
```

---

## TK Video — "Why human review" (30–45s)

**Script:**

[0–5s] Text on screen: "Why can't anyone get in?"
[5–15s] Voice over or animated text:
"Because if anyone gets in, the overall level drops.
And Bare exists exactly so that doesn't happen."
[15–25s] Text: "You submit a project. We review it.
We're not looking for the most famous. We're looking for the most rigorous."
[25–35s] Text: "If you don't get in now, you can try again."
[35–45s] CTA: "Waitlist open. 30 spots this week. Link in bio."

---

## TK Video — "What happens when you get in" (20–30s)

**Script:**

[0–5s] "This is what you get when you're inside Bare."
[5–10s] Screen: search with filters
[10–15s] Screen: profile with projects
[15–20s] Screen: inspiration archive
[20–25s] "No algorithm. No minimum frequency. Just your work."
[25–30s] CTA: "Waitlist. Link in bio."
```

- [ ] **Step 2: Commit**

```bash
git add Campaign/RRSS/Mes2-Waitlist/05-copies-explicativo.md
git commit -m "feat: add explicativo copies — IG carousel and TK scripts"
```

---

## Task 6: Copies — FOMO / Scarcity pillar

**File:** Create `Mes2-Waitlist/06-copies-fomo.md`
**Use:** Month 2 (weeks 5–8) and Month 3 (weeks 9–12)

- [ ] **Step 1: Create copies**

```markdown
# Copies — FOMO / Scarcity Pillar

## Golden rule
Numbers are always real. Never publish a number that isn't the current one.
Update templates each week with real data before publishing.

---

## IG Story templates — Weekly batch opening

### Opening (Monday of each week, Month 2)
```
BATCH [N] OPEN.
30 SPOTS THIS WEEK.

[closing day, e.g. "Closes Sunday."]

bare · waitlist in bio
```

### Mid-week (Wednesday)
```
[X] SPOTS TAKEN.
[30-X] LEFT.

bare · link in bio
```

### Closing (Sunday)
```
BATCH [N] CLOSED.
[X] OUT OF 30 SPOTS TAKEN.

NEXT BATCH
MONDAY.

bare
```

---

## IG Feed posts — Waitlist milestones

### At 50 signups
```
50 INSIDE.

150 SPOTS LEFT
UNTIL LAUNCH.

bare · waitlist in bio
```

### At 100 signups
```
HALFWAY.

100 CREATORS
ALREADY IN BARE.

100 MORE SPOTS.
AFTER THAT,
WAITLIST ONLY.

bare · waitlist in bio
```

### At 150 signups
```
150.

50 SPOTS LEFT
TO CLOSE THE WAITLIST.

bare · waitlist in bio
```

---

## TK Videos — FOMO

### "Why we close the waitlist before launch" (20s)
[0–5s] "Bare closes the waitlist before launch."
[5–10s] "Not because it's full. Because we want day one to have the right level."
[10–15s] "Those inside get in on day 1."
[15–20s] "Those who don't, wait. Waitlist in bio."

### Final countdown (Month 3, 15s)
[0–5s] "[X] spots left."
[5–10s] "Bare launches [date]."
[10–15s] "Link in bio."

---

## FOMO publishing cadence

| Week | Monday | Wednesday | Sunday |
|---|---|---|---|
| 5–8 (Month 2) | Story batch opening | Story mid-week | Story batch closing |
| 9–11 (Month 3) | Feed post milestone | Story spots remaining | Story urgency |
| 12 (last) | Feed post closing | Story "last 24h" | Official closing post |
```

- [ ] **Step 2: Commit**

```bash
git add Campaign/RRSS/Mes2-Waitlist/06-copies-fomo.md
git commit -m "feat: add FOMO copy bank with weekly templates"
```

---

## Task 7: Copies — Contrast pillar

**File:** Create `Mes2-Waitlist/07-copies-contraste.md`
**Use:** Month 2 only, maximum 1 piece every 2 weeks (total: 2 pieces)

- [ ] **Step 1: Create copies**

```markdown
# Copies — Contrast Pillar

## Usage rules
- MAXIMUM 2 pieces in all of Month 2 (week 6 and week 8)
- Never in Month 1 or Month 3
- The problem is the backdrop — one sentence, not a lecture
- Always ends with Bare as the direct answer

---

## Piece 1 — Week 6 (IG feed)

```
YOU HAVE 4 TABS OPEN
WHILE TRYING
TO CREATE.

BARE IS ONE.

waitlist in bio
```

**TK (20s):**
[0–5s] "How many apps do you have open right now to manage your work?"
[5–10s] "Pinterest. Behance. Instagram. LinkedIn."
[10–15s] "Bare is one."
[15–20s] "Waitlist in bio."

---

## Piece 2 — Week 8 (IG feed)

```
78% OF A CREATOR'S TIME
GOES TO SELF-PROMOTION.

22% TO CREATING.

BARE WON'T FIX THAT.
BUT IT REDUCES IT.

waitlist in bio
```

**Note:** This copy uses the real Hesmondhalgh (2013) data from the theoretical framework.
Never fabricate data. If the stat is updated, update the copy.
```

- [ ] **Step 2: Commit**

```bash
git add Campaign/RRSS/Mes2-Waitlist/07-copies-contraste.md
git commit -m "feat: add contrast copy — 2 pieces for Month 2"
```

---

## Task 8: Month 2 Calendar (Weeks 5–8)

**File:** Create `Mes2-Waitlist/08-calendario-semanas5-8.md`

- [ ] **Step 1: Create the calendar**

```markdown
# Month 2 Calendar — Reveal + Waitlist
## Weeks 5–8 · Waitlist opens in batches of 30

---

## Week 5 — Opening

| Day | IG Feed | IG Stories | TikTok |
|---|---|---|---|
| Monday | Carousel "What is Bare" (7 slides) | Story Batch 1 opening: "30 spots this week" | Video "What happens when you get in" (20s) |
| Wednesday | — | Story mid-week: "[X] spots taken, [Y] left" | — |
| Friday | [M] Copy A5 (identity reminder) | — | Video "Why human review" (40s) |
| Sunday | — | Story Batch 1 closing | — |

*Pre-action week 5: publish a Story on Sunday of week 4 with "Tomorrow we open something."*

---

## Week 6 — Contrast + Batch 2

| Day | IG Feed | IG Stories | TikTok |
|---|---|---|---|
| Monday | — | Story Batch 2 opening | — |
| Wednesday | [C] Contrast piece 1 "4 TABS OPEN" | Story mid-week spots | [C] TK contrast 1 (20s) |
| Friday | [UI] Screen 2 profile (with CTA) | — | — |
| Sunday | — | Story Batch 2 closing | — |

---

## Week 7 — Milestone 50/100 + Batch 3

| Day | IG Feed | IG Stories | TikTok |
|---|---|---|---|
| Monday | — | Story Batch 3 opening | — |
| Wednesday | Milestone post (50 or 100 per real count) | Story mid-week | TK video "Why we close before launch" |
| Friday | [M] Copy A7 with CTA | — | — |
| Sunday | — | Story Batch 3 closing | — |

---

## Week 8 — Contrast 2 + Batch 4 + Month 3 preview

| Day | IG Feed | IG Stories | TikTok |
|---|---|---|---|
| Monday | — | Story Batch 4 opening | — |
| Wednesday | [C] Contrast piece 2 "78% self-promotion" | Story mid-week | [C] TK contrast 2 |
| Friday | Post: "Next month, we close." | Story: "Next month, countdown." | TK: closing preview |
| Sunday | — | Story Batch 4 closing | — |

---

## Month 2 KPIs
- Waitlist spots filled: target 120 by end of week 8
- Bio visit → waitlist conversion rate: log from week 5
- Batches sold out in <72h: target 3 out of 4 batches
- IG followers: +400 cumulative from start
- TK followers: +250 cumulative from start
```

- [ ] **Step 2: Commit**

```bash
git add Campaign/RRSS/Mes2-Waitlist/08-calendario-semanas5-8.md
git commit -m "feat: add Month 2 content calendar weeks 5-8"
```

---

## Task 9: Copies — Urgency and Closing

**File:** Create `Mes3-Cierre/09-copies-urgencia.md`

- [ ] **Step 1: Create copies**

```markdown
# Copies — Month 3: Urgency and Closing

## Month 3 communication milestones

### Month 3 start — "Last month"
**IG Feed:**
```
LAST MONTH
OF WAITLIST.

AFTER [CLOSING DATE],
WAITLIST ONLY.

bare · link in bio
```

**TK (15s):**
"Bare closes the waitlist in [X] weeks.
After [date], if you're not in, you wait.
Link in bio."

---

### Week 10 — Visible countdown
**IG Story (publish daily):**
```
[X] DAYS TO
CLOSING.

[Y] SPOTS LEFT.

bare · link in bio
```

**IG Feed:**
```
[X] SPOTS.
[Y] DAYS.

bare · waitlist in bio
```

---

### Week 11 — Last 30 spots
**IG Feed:**
```
LAST 30 SPOTS.

BARE LAUNCHES [DATE].
THE WAITLIST CLOSES
BEFORE THAT.

bare · link in bio
```

**TK (20s):**
"30 spots left in Bare's waitlist.
After this, waitlist only.
The platform launches with whoever is inside.
Link in bio."

---

### Official closing — Waitlist closing day
**IG Feed:**
```
WAITLIST CLOSED.

200 CREATORS
INSIDE.

BARE LAUNCHES [DATE].
```

**IG Story:**
```
CLOSED.
SEE YOU ON [DATE].
```

**TK (15s):**
"Bare's waitlist is closed.
200 creators inside.
Bare launches [date].
Thank you."

---

## Month 3 rules
1. Daily Stories from week 10 with days and spots remaining (always real data)
2. No more than 1 urgency feed post every 3 days (avoid saturating)
3. Tone stays: sober, direct, never aggressive or "last chance!"
4. Closing day: one single post. Clean. No excessive celebration.
```

- [ ] **Step 2: Commit**

```bash
git add Campaign/RRSS/Mes3-Cierre/09-copies-urgencia.md
git commit -m "feat: add urgency and closing copies for Month 3"
```

---

## Task 10: Month 3 Calendar (Weeks 9–12)

**File:** Create `Mes3-Cierre/10-calendario-semanas9-12.md`

- [ ] **Step 1: Create the calendar**

```markdown
# Month 3 Calendar — Closing and Urgency
## Weeks 9–12 · Countdown to launch

---

## Week 9 — Countdown starts

| Day | IG Feed | IG Stories | TikTok |
|---|---|---|---|
| Monday | Post "Last month of waitlist" | Story: "[X] spots left" | TK "Closing in 1 month" (15s) |
| Wednesday | [UI] Screen 1 with urgency copy | Story: countdown days | — |
| Friday | [M] Copy B1 (updated with real date) | Story countdown | [M] B1 animated |

---

## Week 10 — Tension rising

| Day | IG Feed | IG Stories | TikTok |
|---|---|---|---|
| Monday | Milestone post (150 if not yet reached) | Daily story: days + spots | TK countdown (15s) |
| Wednesday | [M] Copy B2 "The waitlist closes before..." | Daily story | — |
| Friday | [UI] Screen 4 access process + urgent CTA | Daily story | TK "last few weeks" |

---

## Week 11 — Last 30 spots

| Day | IG Feed | IG Stories | TikTok |
|---|---|---|---|
| Monday | Post "Last 30 spots" | Daily story | TK "30 spots left" (20s) |
| Wednesday | [M] Copy B3 "[X] out of 200" | Daily story | — |
| Friday | Post: "Next week, we close." | Daily story | TK closing preview |

---

## Week 12 — Closing

| Day | IG Feed | IG Stories | TikTok |
|---|---|---|---|
| Monday | [M] Copy B4 "Last few weeks" | Story: "[X] days and [Y] spots left" | TK max urgency (15s) |
| Wednesday | — | Story: "last 48h" | TK: "last 48h" |
| Thursday | — | Story: "last 24h" | — |
| Friday [CLOSING] | Official closing post "WAITLIST CLOSED. 200 CREATORS INSIDE." | Closing story | TK closing (15s) |

---

## Month 3 KPIs
- Waitlist complete: 200 people ✓
- Last batch sold out before closing day
- IG followers at close: +1,000 from campaign start
- TK followers at close: +500 from campaign start
- Batches sold out in <72h during Month 3: target 100%
```

- [ ] **Step 2: Final commit**

```bash
git add Campaign/RRSS/Mes3-Cierre/10-calendario-semanas9-12.md
git commit -m "feat: add Month 3 content calendar weeks 9-12"
git push origin main
```

---

## Prerequisites checklist before publishing

- [ ] UI mockups for all 4 screens ready and in black and white
- [ ] Landing page / waitlist form live and operational
- [ ] Spot management system configured (for real-time counting)
- [ ] IG and TK accounts created with bio and link in bio active
- [ ] Approximate launch date confirmed (needed from Month 3)
- [ ] Someone assigned to update daily countdown Stories in Month 3
