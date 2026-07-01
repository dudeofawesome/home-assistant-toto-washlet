This is a custom Home Assistant integration to control TOTO Washlet bidets. Specifically, it has known support for the S7a model (including flush kit).

TOTO bidets use IR to communicate between the remote and seat. The manual for one can be found [here](https://www.totousa.com/filemanager_uploads/product_assets/OwnersManual/D07G46_Instruction%20Manual_EN.pdf).

This integration uses an [ESPHome IR proxy](https://www.home-assistant.io/blog/2026/04/01/release-20264/#infrared-becoming-a-first-class-citizen-of-home-assistant)

Similar integrations include the [LG](https://github.com/home-assistant/core/tree/dev/homeassistant/components/lg_infrared) and [Marantz](https://github.com/home-assistant/core/tree/dev/homeassistant/components/marantz_infrared) IR components

Run non-basic commands from inside the devenv (`devenv shell --quiet -- {command}`), which will not work in Codex's sandbox.
