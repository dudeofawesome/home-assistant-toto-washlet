---
name: toto-washlet-ir-capture
description: Use when capturing live IR codes, especially to add new buttons, enum values, or received-command events
---

Capture live IR codes from an ESPHome IR device.

## Process

1. create minimal config: `scripts/gen-minimal-config.sh /tmp/washlet-proxy-config.yaml`
1. watch the logs: `esphome logs --device 10.0.16.10 /tmp/washlet-proxy-config.yaml`
   - consider cutting down the logs with something like `grep -iE 'remote|ir|receiver'`
   - custom_components/toto_washlet/commands.py contains codes that are already known
1. Remove temporary capture logs, scratch files, and private environment details before finishing
