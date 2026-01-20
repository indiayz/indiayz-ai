# Media Download

The Media module allows downloading videos or audio using a backend-powered.

---

## Supported Platforms

- YouTube
- Instagram
- Facebook
- Twitter / X
- 2000+ sites supported by yt-dlp

---

## Usage

import indiayz

result = indiayz.media_download(
    url="VIDEO_URL",
    format="mp4"
)

---

## Audio Download

result = indiayz.media_download(
    url="VIDEO_URL",
    format="mp3"
)

---

## Notes

- Downloads are processed server-side
- Client never runs yt-dlp locally
- Safer and faster for developers
