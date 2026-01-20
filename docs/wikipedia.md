# Wikipedia API

The Wikipedia module provides real-time summaries from Wikipedia.

---

## Usage

import indiayz

response = indiayz.wikipedia_search("Python programming")

---

## Response Structure

- success: boolean
- source: wikipedia
- data:
  - title
  - summary
  - url
  - image (optional)

---

## Notes

- Results are fetched from the official Wikipedia REST API
- No scraping
- No rate-limit issues for SDK users
