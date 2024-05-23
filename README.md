<p align="center">
  <picture>
    <img alt="Hugging Face Transformers Library" src="https://jvaleroliet.github.io/images/deepdiggin.png" width="250" style="max-width: 100%;">
  </picture>
</p>

## Introduction

This project aims to construct a python library to classify vinyl records according to the [Goldmine Grading](https://www.goldminemag.com/collector-resources/record-grading-101).

The package is constructed with my finetuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) called [wav2vec2-base-vinyl_condition](https://huggingface.co/jvalero/wav2vec2-base-vinyl_condition)

### Features

- Obtain grading condition from an audio clip of the vinyl.

Future features:

- Obtain visual grading condition from a photo of the vinyl.
- Obtain visual grading condition of the cover from a photo of it.

