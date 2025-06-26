#!/bin/bash
docker build -t sitio8888 .
docker run -d --name cont8888 -p 8888:8888 sitio8888
sleep 2
if curl -s http://localhost:8888 >/dev/null; then
  echo "OK: sitio8888 up"
else
  echo "ERROR: no responde"
fi
docker ps --filter name=cont8888
