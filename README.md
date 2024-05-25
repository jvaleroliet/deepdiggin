<p align="center">
  <picture>
    <img alt="deepdiggin" src="https://jvaleroliet.github.io/images/deepdiggin-large.png" style="max-width: 100%;">
  </picture>
</p>

## Introduction

This project aims to construct a simple python library to classify vinyl records according to the [Goldmine Grading](https://www.goldminemag.com/collector-resources/record-grading-101).

The package is constructed with my finetuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) called [wav2vec2-base-vinyl_condition](https://huggingface.co/jvalero/wav2vec2-base-vinyl_condition).

### Features

- Obtain grading condition from an audio clip of the vinyl.
- Find out wherever a vinyl is scratched or not.

Future features:

- Improve model accuracy.
- Obtain visual grading condition from a photo of the vinyl.
- Obtain visual grading condition of the cover from a photo of it.
- Process entire folders creating a dataframe with paths and conditions.
- Determine the genre of the vinyl.
- Identification of vinyl from photo.
- Get value of the record based on discogs price.

## Installation

To install, run the following command in your terminal:

`pip install git+https://github.com/jvaleroliet/deepdiggin.git@main`

## Basic Usage

```python
from  deepdiggin import predict

condition = predict.condition_from_audio('path/to/audio')

print(condition)

scratch_test = predict.scrath_detection('path/to/audio')

print(scratch_test)
```

## Under Construction

The package is under construction. Feel free to collaborate! 🎵

