# Cloudflare Pages

Developer: Hamdy Abou El Anein.

Branch: publish/cloudflare-pages-20261103. Framework: None. Root: repository root. Build command: `python3 scripts/build-pages.py`. Output: `public-site`.

Python generates the current catalogue from data/orbital.json, retaining the public picture/font/archive assets copied from the Pi. Search and filters run in the browser. Legacy server APIs and social jobs are not migrated to Pages and must remain on their existing backend if still used.

Daily freshness: the Raspberry Pi runs `astrometry-pages-publish.timer` at 00:10 Europe/Zurich with up to 90 seconds of delay and catch-up after downtime. The dedicated pages-publisher account rebuilds public-site and commits/pushes only those public files to the Pages production branch. Its SSH deploy key has write access only to this repository. No Cloudflare token or Deploy Hook is needed. The previous astrometry-build.timer is disabled. If the Pi is off, the site remains online with its last published data.

Test the pages.dev preview before attaching astrometry.ch and www.astrometry.ch. Preserve mail DNS and unrelated subdomains.


## Pi maintenance after migration

The shared cloudflared tunnel remains required for MinerWatch and Nextcloud. The six root/www site routes were removed from its local ingress configuration after the custom domains became active on Pages. Five old Apache site configurations were disabled; the MinerWatch virtual host remains enabled. Former web roots, configuration snapshots and obsolete certificate-renewal definitions are archived under /var/backups/cloudflare-pages-migration on the Pi. Issued certificates were retained. The signed APT working directory and its signing key remain on the Pi. Do not remove the publisher deploy keys while the update jobs use them.

Publisher source: `deploy/pages-publish.py`. Service account: pages-publisher; state: /var/lib/pages-publisher; installed script: /usr/local/lib/pages-publisher/publish.py. Production branch remains publish/cloudflare-pages-20261103; coordinate the service configuration if changing branches. Publisher jobs refuse uncommitted or diverged work and never force-push.
