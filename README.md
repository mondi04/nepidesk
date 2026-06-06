# belchenstrasse5.de — htmforge Dashboard

Ersetzt das statische `index.html` durch eine Flask-App die alles mit **htmforge** rendert.

## Setup auf g7

```bash
# 1. Dateien hochladen
scp -r . moritz@g7:~/belchenstrasse5/

# 2. Dependencies
pip install flask gunicorn htmforge

# 3. systemd
sudo cp belchenstrasse5.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now belchenstrasse5

# 4. Cloudflare Tunnel → belchenstrasse5.de → localhost:5000
# (in cloudflared config.yml)
# - hostname: belchenstrasse5.de
#   service: http://localhost:5000
```

## Struktur

```
belchenstrasse5/
├── app.py                    # Flask + htmforge App
└── belchenstrasse5.service   # systemd unit
```

Kein Nginx, kein SSL-Bastle. Cloudflare Tunnel macht alles.