cat >"$1" <<EOL
esphome: {name: foo}
esp8266: {board: esp8285}
logger: {}
wifi: { ssid: foo, password: password, min_auth_mode: WPA2 }
api: {encryption: {key: "$(kubectl exec -n esphome deployments/esphome -- awk '/^api:/{a=1} a&&/key:/{gsub(/.*key: *"?|"?$/,""); print; exit}' /config/washlet-proxy.yaml)"}}
EOL
