import json
import os

benchamrk_file_loc = ".asv/results/benchmarks.json"
results_dir = ".asv/results/marian-notebook"
data_formats = ["Csv", "Json", "Xml", "Hdf5Fixed", "Hdf5Table", "Parquet", "Feather", "Orc", "Pickle", "Excel"]

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
        if key == "params":
            benchmark_data[bench][key] = [data_formats]

benchamrk_file = open(benchamrk_file_loc, "w")
json.dump(benchmark_data, benchamrk_file,  indent=4)
benchamrk_file.close()


result_filename = os.listdir(results_dir)
result_filename.remove("machine.json")

results_file_loc = ".asv/results/marian-notebook/" + result_filename[0]
results_file = open(results_file_loc, "r")
results_data = json.load(results_file)
results_file.close()

for bench in benchamrk_names:
    for bench_results in results_data["results"][bench]:
        results_data["results"][bench][1] = [data_formats]

results_file = open(results_file_loc, "w")
json.dump(results_data, results_file,  indent=4)
results_file.close()