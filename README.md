# Astrometry.ch

Modern static astronomy catalogue by **Hamdy Abou El Anein**.

Explore https://astrometry.ch. The original site and scripts are preserved in the old GitHub branch and at /old/ on the server.

## Architecture

- Python 3 standard library builds HTML, CSS, JavaScript and JSON from curated data/orbital.json.
- Daily systemd timer runs as www-data; no Flask, database, background web service or tracking is required.
- Atomic file replacement avoids partially written HTML.
- Search and category filtering run locally in the browser.
- Source dates are historical/curated, not authoritative or live ephemerides. The interval bar is a calendar-time fraction, not physical orbital position.
- No invented future dates or extrapolation.
- Existing legacy API, media, social jobs and other server services are independent and unchanged.

## Development

Run: python3 build.py --source data/orbital.json --out dist/site
Run: python3 -m unittest discover -s tests -v

The old branch preserves the original implementation. Review the generated site and deploy/ systemd units before production deployment.

License: GNU GPL v3 (see LICENSE). Existing image and third-party rights remain with their respective authors.
