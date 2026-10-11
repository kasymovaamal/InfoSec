# Lab 10: Configuring NGINX

Performed inside a Docker Ubuntu container (`docker run -it --name lab10 ubuntu bash`), since nginx site configuration and `/etc/nginx/` paths are Linux-specific.

## Setup
- Installed nginx: `apt update && apt install -y nginx`
- Created site config `/etc/nginx/sites-available/my_site` listening on port 8000, serving `/var/www/html/my_site.html`
- Created `my_site.html` with sample content
- Enabled the site: `ln -s /etc/nginx/sites-available/my_site /etc/nginx/sites-enabled/` (initially missed this step — caused nginx to only serve the default site; fixed by creating the symlink)
- Tested config: `nginx -t` → syntax OK
- Started nginx with `service nginx start` / reloaded with `service nginx reload` (used instead of `systemctl` since Docker containers don't run systemd)
- Verified with `curl localhost:8000` → returned the HTML content

## Task: proxy_pass to a running API
- Installed Python, pip, and Flask (`apt install -y python3 python3-pip`, `pip3 install flask --break-system-packages`)
- Created a simple Flask API (`/api/hello`) running on port 5000
- Added a `location /api/ { proxy_pass http://127.0.0.1:5000/api/; }` block to the nginx config
- Reloaded nginx: `nginx -t && service nginx reload`
- Verified with `curl localhost:5000/api/hello` (direct) and `curl localhost:8000/api/hello` (via nginx) → both returned `{"message":"Hello from the API!"}` with HTTP 200

## Troubleshooting encountered
- Got `502 Bad Gateway` initially because the Flask API wasn't actually running yet (file wasn't created due to missing `nano`/`pip3` at the time)
- Installing `python3`/`tzdata` triggered an interactive timezone prompt (selected Asia → Bishkek) that needed to be resolved before continuing

## Findings
- `proxy_pass` lets nginx act as a reverse proxy, forwarding specific URL paths to a backend application server while still serving other content (like static files) directly.
- The client only interacts with nginx on port 8000; the backend API on port 5000 is never exposed directly.
- Forgetting to symlink a site into `sites-enabled/` means nginx silently ignores it, even if the config file itself is valid — a common and non-obvious source of errors.
