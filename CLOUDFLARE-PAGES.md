# Cloudflare Pages

Developer: Hamdy Abou El Anein.

Branch: publish/cloudflare-pages-20261103. Framework: None. Root: repository root. Build command: `python3 scripts/build-pages.py`. Output: `public-site`.

Python generates the current catalogue from data/orbital.json, retaining the public picture/font/archive assets copied from the Pi. Search and filters run in the browser. Legacy server APIs and social jobs are not migrated to Pages and must remain on their existing backend if still used.

Daily freshness: the current Pi systemd timer must remain enabled until a Pages Deploy Hook is configured and its scheduled rebuild verified. The Pi can POST to this hook from its daily build job; the hook URL must remain in a private file, never in this repository. Only after that verification may the Pi publication job be retired. Each Pages build recalculates dates in Europe/Zurich.

Test the pages.dev preview before attaching astrometry.ch and www.astrometry.ch. Preserve mail DNS and unrelated subdomains.
