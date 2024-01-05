import json
import os

benchamrk_file_loc = ".asv/results/benchmarks.json"
results_dir = ".asv/results/marian-notebook"
data_formats = ["Csv", "Json", "Xml"]

benchamrk_file = open(benchamrk_file_loc, "r")
benchmark_data = json.load(benchamrk_file)
benchamrk_file.close()

benchamrk_names = []
for bench in benchmark_data:
    benchamrk_names.append(bench)
benchamrk_names.remove("version")

for bench in benchamrk_names:
    for key in benchmark_data[bench]:
        if key == "type" and benchmark_data[bench][key] == "track":
            benchmark_data[bench][key] = "memory"
        if key == "unit" and benchmark_data[bench][key] == "unit":
            benchmark_data[bench][key] = "bytes"

benchamrk_file = open(benchamrk_file_loc, "w")
json.dump(benchmark_data, benchamrk_file,  indent=4)
benchamrk_file.close()
