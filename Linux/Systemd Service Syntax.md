Systemd Service Syntax

```bash
[Unit]
Description=A description here.
After=multi-user.target

[Service]
User=root //only if ExecStart requires root priviledges
Group=root //only if ExecStart requires root priviledges
ExecStart= echo Hello
Restart=on-failure
RestartSec=3

[Install]
WantedBy=multi-user.target
```
