# API Reference

This page documents all public SDK functions.

---

## wikipedia_search(query)

Returns a Wikipedia summary.

Parameters:
- query (string)

---

## media_download(url, format)

Downloads media via backend.

Parameters:
- url (string)
- format (mp4 or mp3)

---

## random_quote()

Returns a random quote.

---

## Error Handling

All SDK errors raise IndiayzAPIError exceptions.
Always wrap calls in try/except for production use.
