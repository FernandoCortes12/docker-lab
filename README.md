# Docker Lab – Redes Avanzadas I

Una colección de tres ejercicios de laboratorio sobre Docker y Flask/HTTP estático, implementados en una VM DevNetLab. Cada ejercicio muestra tu IP o un mensaje desde dentro de un contenedor, escuchando en distintos puertos.

---

## 📋 Resumen de ejercicios

| Ejercicio | Descripción                                     | Puerto Docker | URL de prueba                   |
|-----------|-------------------------------------------------|---------------|---------------------------------|
| 1         | Flask “pro” con Bootstrap muestra tu IP         | 8000          | `http://<IP_VM>:8000`           |
| 2         | Flask + plantilla Jinja2 “pro” muestra tu IP    | 8181          | `http://<IP_VM>:8181`           |
| 3         | Sitio estático servido por Flask/Gunicorn       | 8888          | `http://<IP_VM>:8888`           |

> **IPs de ejemplo en la VM:**  
> - Contenedor app1 (8000): `172.17.0.1`  
> - Contenedor app2 (8181): `10.0.2.15`  
> - Contenedor sitio estático (8888): `127.0.0.1`

---

## 🖥️ Entorno de trabajo

- **VM**: Oracle VirtualBox “DEVASC-LABVM” importada desde Cisco DevNet.  
- **SO invitado**: Ubuntu 20.04 LTS  
- **Herramientas**:  
  - Docker & Docker-Compose  
  - Python 3.9 + Flask + Gunicorn  
  - Git + GitHub (SSH keys configuradas)  
- **Red**: NAT de VirtualBox, puertos 8000, 8181, 8888 mapeados a la VM.

---

## 📂 Estructura del repositorio

```text
docker-lab/
├── app1/            # Ejercicio 1: Flask + Bootstrap
│   ├── app1.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── static/
│   │   └── style.css
│   └── templates/
│       └── index.html
├── app2/            # Ejercicio 2: Flask + Plantilla Jinja2
│   ├── app2.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── static/
│   │   └── style.css
│   └── templates/
│       └── index.html
├── sitio8888/       # Ejercicio 3: HTML estático servido con Flask/Gunicorn
│   ├── app3.py
│   ├── index.html
│   ├── requirements.txt
│   ├── Dockerfile
│   └── run_site.sh
└── README.md        # (este archivo)
