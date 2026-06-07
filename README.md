# nepidesk.de — htmforge Dashboard



## Struktur

```
nepidesk/
├── static/
│   ├── css/
│   │   └── main.css    
│   └── js/
│       └── main.js
│
├── app.py                      # Flask App
├── components.py               # HTMforge Komponenten
├── data.py                     # Inhalte
└── nepidesk.service            # systemd unit
```

Kein Nginx, kein SSL-Bastle. Cloudflare Tunnel macht alles.