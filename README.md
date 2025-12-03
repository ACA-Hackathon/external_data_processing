# External data processing
This repo contains a minimalist ETL pipeline for consolidate external data into parquet files.
## Setup
A basic setup is a conda environment with python 3.11.0. **We should build a clean Poetry project to avoid dependencies bugs**.

## Main data sources

### AGRESTE
AGRESTE is the institution responsible for public statistics on agriculture, food, forestry, and fishing.
Every year, they publish the SAA (Statistique Agricole Annuelle), a report on agricultural surfaces and yields at the departmental level.

## TO-DO
- [ ] Set up a poetry project for betterdependencyy management.
- [x] Import and transform AGRESTE data from 2010.
- [ ] Import and transform AGRESTE data for years before 2010. 
- [ ] Unify and harmonize AGRESTE data, by choising key crops.
- [ ] Import and transform GDP variation.
- [ ] Import and transform culture typologies prix evolutions.
- [ ] Import and transform soil data by cell (the grid is heritated from wheater data).

## Outputs
Using the make commands, this project enables the generation of following files:

- ```agreste_2010_2024_{*}.parquet```

As a backup, these files are saved [here](link_to_hf_repository).