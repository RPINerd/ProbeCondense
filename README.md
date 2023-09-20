# Probe Condense

## Description

This script is designed to analyze an input list of oligos (primers/blockers/probes) and condense them into a smaller list of oligos that will still cover the same targets. This is useful for reducing the cost of a probe set, or for reducing the number of oligos in a multiplexed assay.

## Usage

```bash
python3 probecondense.py -f my_targets.fasta -p my_probes.txt -o my_condensed_probes.txt
```

## Input

Expected input is a fasta/q file of target sequences (i.e. what you want your oligos to bind to) and a text file of oligos (one per line) that you want to condense.

## Output

The output is a text file of oligos (one per line) where oligos that overlap or are redundant have been pruned out

