# ocr-microservices
Steps to run keycloak Dock
"docker pull quay.io/keycloak/keycloak:22.0.5 "
"docker run -p 8180:8080 \
  -e KEYCLOAK_ADMIN=admin \
  -e KEYCLOAK_ADMIN_PASSWORD=admin \
  quay.io/keycloak/keycloak:22.0.5 \
  start-dev"