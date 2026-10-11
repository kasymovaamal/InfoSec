# Lab 9: Package Management

Performed inside a Docker Ubuntu container (`docker run -it --name lab9 ubuntu bash`), since `apt` is Debian/Ubuntu-specific and unavailable on macOS.

## Commands explored
- `apt update` — refreshed package index
- `apt install -y nginx` — installed nginx and its dependencies (nginx-common, nginx-core)
- `apt search nginx` — listed related packages (nginx-core, libnginx-mod-*, etc.)
- `apt-cache depends nginx` — listed nginx's dependencies
- `service nginx start` / `service nginx status` — started and verified nginx is running
- `curl localhost` — confirmed nginx served its default welcome page
- `apt remove -y nginx` then `apt purge -y nginx` — removed nginx; purge also cleared config files and freed 1635 kB
- `apt autoremove -y` — cleaned up leftover `nginx-common` dependency, freeing an additional 232 kB

## Findings
- `apt update` only refreshes the package index; it doesn't install/upgrade anything by itself.
- `apt remove` leaves config files behind; `apt purge` removes them too.
- `apt-cache depends` shows what a package requires to run (its dependency chain).
- Docker containers don't auto-start services on install (`invoke-rc.d: policy-rc.d denied execution`) — services must be started manually with `service <name> start`.
- `apt autoremove` cleans up dependencies that are no longer needed after a package is purged.
