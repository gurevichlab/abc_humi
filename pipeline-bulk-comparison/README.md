# Bulk comparison against ABC-HuMi

Note that the pipeline requires Docker to run antiSMASH 7.0. Alternatively, antiSMASH reports can be submitted as input.

To run the pipeline on the test data, please follow the steps below:
- Download test data
    ```
    cd test_data && python generate_test_data.py
    ```
- Download the desired set of BGCs and precomputed BiG-SCAPE cache files from the ABC-HuMi [downloads page](https://ccb-web.cs.uni-saarland.de/abc_humi/downloads),
    ```
    mkdir resources
    wget -P resources https://ccb-compute2.cs.uni-saarland.de/abc-humi-download/BGC_All.tar.gz
    wget -P resources https://ccb-compute2.cs.uni-saarland.de/abc-humi-download/bigscape_cache.tar.gz
    ```
- Run the pipeline
    ```
    snakemake -s workflow/Snakefile --use-conda --cores 32 
    ```
- The reports will be generated in the `results/summary` directory.

To run the pipeline on custom data, please modify the input path in `config/config.yml`. 