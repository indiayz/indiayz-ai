# Quick Start

This guide helps you get started with indiayz in under 2 minutes.

---

## Import the SDK

import indiayz

---

## Wikipedia Search

result = indiayz.wikipedia_search("India")
print(result)

---

## Download Media

result = indiayz.media_download(
    url="https://www.youtube.com/watch?v=example",
    format="mp4"
)

print(result)

---

## Random Quote

quote = indiayz.random_quote()
print(quote)

---

That’s it.  
You are now using backend-powered AI utilities with indiayz.
