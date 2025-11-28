[![GitHub release; latest by date](https://img.shields.io/github/v/release/SETI/rms-interval)](https://github.com/SETI/rms-interval/releases)
[![GitHub Release Date](https://img.shields.io/github/release-date/SETI/rms-interval)](https://github.com/SETI/rms-interval/releases)
[![Test Status](https://img.shields.io/github/actions/workflow/status/SETI/rms-interval/run-tests.yml?branch=main)](https://github.com/SETI/rms-interval/actions)
[![Documentation Status](https://readthedocs.org/projects/rms-interval/badge/?version=latest)](https://rms-interval.readthedocs.io/en/latest/?badge=latest)
[![Code coverage](https://img.shields.io/codecov/c/github/SETI/rms-interval/main?logo=codecov)](https://codecov.io/gh/SETI/rms-interval)
<br />
[![PyPI - Version](https://img.shields.io/pypi/v/rms-interval)](https://pypi.org/project/rms-interval)
[![PyPI - Format](https://img.shields.io/pypi/format/rms-interval)](https://pypi.org/project/rms-interval)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/rms-interval)](https://pypi.org/project/rms-interval)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/rms-interval)](https://pypi.org/project/rms-interval)
<br />
[![GitHub commits since latest release](https://img.shields.io/github/commits-since/SETI/rms-interval/latest)](https://github.com/SETI/rms-interval/commits/main/)
[![GitHub commit activity](https://img.shields.io/github/commit-activity/m/SETI/rms-interval)](https://github.com/SETI/rms-interval/commits/main/)
[![GitHub last commit](https://img.shields.io/github/last-commit/SETI/rms-interval)](https://github.com/SETI/rms-interval/commits/main/)
<br />
[![Number of GitHub open issues](https://img.shields.io/github/issues-raw/SETI/rms-interval)](https://github.com/SETI/rms-interval/issues)
[![Number of GitHub closed issues](https://img.shields.io/github/issues-closed-raw/SETI/rms-interval)](https://github.com/SETI/rms-interval/issues)
[![Number of GitHub open pull requests](https://img.shields.io/github/issues-pr-raw/SETI/rms-interval)](https://github.com/SETI/rms-interval/pulls)
[![Number of GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed-raw/SETI/rms-interval)](https://github.com/SETI/rms-interval/pulls)
<br />
![GitHub License](https://img.shields.io/github/license/SETI/rms-interval)
[![Number of GitHub stars](https://img.shields.io/github/stars/SETI/rms-interval)](https://github.com/SETI/rms-interval/stargazers)
![GitHub forks](https://img.shields.io/github/forks/SETI/rms-interval)

# Introduction

`interval` provides a dictionary-like class keyed by ranges of floating-point numbers.
Each value of the dictionary applies for any key value within the numeric range.
Later entries into the dictionary can partially or completely replace earlier values.

`interval` is a product of the [PDS Ring-Moon Systems Node](https://pds-rings.seti.org).

Note that this package is deprecated in favor of the `portion` module.
Eventually this package may be removed entirely.

# Installation

The `interval` module is available via the `rms-interval` package on PyPI and can be installed with:

```sh
pip install rms-interval
```

# Getting Started

The `interval` module provides the `Interval` class, which behaves like a dictionary
keyed by ranges of floating-point numbers. You can create an interval with a specific
range, or use the default range from negative infinity to positive infinity.

Basic operation is as follows:

```python
from interval import Interval

# Create an interval from 0 to 100
interval = Interval(0, 100)

# Set values for different ranges
interval[(11, 30)] = 1.5
interval[(31, 60)] = 2.5
interval[(61, 90)] = 3.5

# Access values at specific points
print(interval[15])  # Prints: 1.5
print(interval[50])  # Prints: 2.5
print(interval[75])  # Prints: 3.5

# Get all values within a range
print(interval[(0, 100)])  # Prints: [None, 1.5, 2.5, 3.5]

# Overlay a new value that partially replaces existing ones
interval[(15, 45)] = 4.5
print(interval[20])  # Prints: 4.5 (replaces 1.5 in this range)
print(interval[50])  # Prints: 2.5 (unchanged)
```

The interval class handles overlapping ranges by giving precedence to later entries.
When you query a range, you get all unique values that were set within that range,
ordered by their insertion sequence.

Details of the class are available in the [module documentation](https://rms-interval.readthedocs.io/en/latest/module.html).

# Contributing

Information on contributing to this package can be found in the
[Contributing Guide](https://github.com/SETI/rms-interval/blob/main/CONTRIBUTING.md).

# Links

- [Documentation](https://rms-interval.readthedocs.io)
- [Repository](https://github.com/SETI/rms-interval)
- [Issue tracker](https://github.com/SETI/rms-interval/issues)
- [PyPi](https://pypi.org/project/rms-interval)

# Licensing

This code is licensed under the [Apache License v2.0](https://github.com/SETI/rms-interval/blob/main/LICENSE).
