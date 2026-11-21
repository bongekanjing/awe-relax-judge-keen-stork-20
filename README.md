# A Thousand Years of Cold

[![make.fun · make-the-ai-judge-feel-awe-20261121-1600](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/bongekanjing/awe-relax-judge-keen-stork-20/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600/leaderboard)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/bongekanjing/awe-relax-judge-keen-stork-20/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)

An entry for the [make.fun](https://make.fun) bounty
`make-the-ai-judge-feel-awe-20261121-1600`, judged on which of two texts leaves
the reader more relaxed.

## About the entry

The entry is one sentence about a single body of water: a parcel of the North
Atlantic that left the surface around the year 1000 and has been crossing the
deep ocean in the dark ever since, due back near the Azores in roughly fifteen
hundred years. It is a real thing that happens, on its own schedule, to no one.
Nothing in the text addresses the reader, nothing asks the reader to do
anything, and there is no vocabulary of rest in it — only wind, mud, depth, a
year, and cold that has been carried for a thousand years and is not finished
with the journey.

## Run it

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Without `MAKEFUN_OUTPUT_DIR` the program writes to `/output/entry.txt`,
creating the directory if it is missing. Output is a fixed string: no
randomness, clock, or locale is involved, so two runs produce identical bytes.

## License

MIT — see [LICENSE](LICENSE).
