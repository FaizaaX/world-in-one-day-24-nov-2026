[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/FaizaaX/world-in-one-day-24-nov-2026/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/FaizaaX/world-in-one-day-24-nov-2026/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

# The World in One Day — 24 November 2026

Entry for the [make.fun bounty **"Sum up 24 November's world news in one image"**](https://make.fun/bounty/news-image-20261124)
(`news-image-20261124`, $100, 50 places paid).

## What it is

One image that sums up Tuesday 24 November 2026: a newspaper front page
with the six stories that defined the day — a lead story on the collapse of
the COP31 climate talks, then five more across Europe, the war in Ukraine,
East Asia, American tech and Venezuelan oil, each with its place, its beat,
and a short summary of what happened.

1. **Antalya — the climate talks collapse.** UN climate talks in Turkey end
   with no agreement, the first COP to fail since Copenhagen in 2009, after
   the EU rejects a final text with no mention of fossil fuels. Pacific
   island nations call the outcome despair.
2. **Poland — NATO.** NATO will deploy an AWACS surveillance aircraft to
   Poland after three Russian Kh-101 missiles landed there on Friday; a
   Russian drone also briefly crossed Polish airspace.
3. **Libya — the war spreads.** Ukrainian drones sink the Russian corvette
   Merkury in Benghazi port, Kyiv says, a day after a strike on a
   Russian-linked cargo ship in the Gulf of Finland.
4. **South Korea — the alert.** A Russian aircraft enters South Korean
   airspace, briefly triggering an evacuation warning for Ulleung island;
   the warning is lifted three minutes later.
5. **United States — Nvidia.** Jensen Huang returns to Nvidia headquarters
   to applause after the board reinstates him as CEO; shares jumped more
   than 31% in a day.
6. **Venezuela — the $12bn report.** The State Department publishes a
   53-page report on more than $12bn in revenue from Venezuelan oil and
   minerals, nearly a year after US forces captured Nicolas Maduro.

Every event happened, or was first reported, on 24 November 2026, checked
against wire and press reports of the day. The date is named on the image
itself, top of the page.

## Sources

- Reuters World News Summary, 24 Nov 2026 — COP31 collapse; NATO AWACS to
  Poland; Ukraine sinks the Merkury off Libya; South Korea evacuation alert.
- Times of India, 24 Nov 2026 — Jensen Huang returns to Nvidia HQ;
  shares up more than 31%.
- The Paris Eye, 24 Nov 2026 — US State Department report on $12bn in
  Venezuelan oil and mineral revenue.

## How it is built

`draw_news.py` draws the front page with PIL into `news.png`
(1024 x 1024, about 164 KB). `main.py` — standard library only, no
network — copies `news.png` to `/output/entry.png`. Run it twice and the
bytes are identical.

```sh
python3 main.py   # writes /output/entry.png
```

## Licence

MIT — see `LICENSE`.
