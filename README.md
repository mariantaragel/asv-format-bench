# ASV FormatBench
ASV FormatBench is a Python benchmark of data formats written in framework [asv](https://github.com/airspeed-velocity/asv). This project aims to evaluate different data formats for storing tabular and image data.

Check out also: [FormatBench](https://github.com/mariantaragel/format-bench)

## Usage
Run all benchmark suites or selected suites locally and preview website:
```
asv run --quick [--bench <benchmark_suite>]
python3 postprocessing.py
asv publish
asv preview
```

Script `cron.sh` can automate the process of running benchmarks. Results will be published to an interactive [website](https://mariantaragel.github.io/asv-format-bench/).

Run all benchmarks and publish them to website:
`./cron.sh`

## Related publication
TARAGEĽ, Marián. *Column-oriented and Image Data Format Benchmarks*. Brno, 2024. Bachelor’s thesis. Brno University of Technology, Faculty of Information Technology. Supervisor Ing. Jakub Špaňhel

## Acknowledgements
I would like to convey my gratitude to Ing. Jakub Špaňhel for his supervision. I also express my thanks to my consultant Ing. Petr Chmelař. Both of them provided me with support and advice during the work on this thesis. Last but not least, I would like to thank the external submitter, the Innovatrics company, for their professional help.
