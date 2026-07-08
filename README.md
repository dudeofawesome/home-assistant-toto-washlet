# TOTO Washlet Integration for Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/integration)
[![Validate](https://github.com/dudeofawesome/home-assistant-toto-washlet/actions/workflows/validate.yml/badge.svg)](https://github.com/dudeofawesome/home-assistant-toto-washlet/actions/workflows/validate.yml)

## Features

- Control supported TOTO Washlet bidet functions through Home Assistant entities.
- Send commands through a configured Home Assistant infrared emitter.
- Optionally listen for Washlet remote commands through a configured infrared receiver.

## Prerequisites

- **Home Assistant 2026.4.0** or newer
- **Home Assistant IR Integration** must be configured and working

## Installation

### HACS (Recommended)

Use this repository as a HACS custom repository:

[![Open your Home Assistant instance and add this repository to HACS.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=dudeofawesome&repository=home-assistant-toto-washlet&category=integration)

1. Open HACS in Home Assistant
2. Click the three dots menu and select "Custom repositories"
3. Add this repository URL and select "Integration" as the category
4. Click "Add"
5. Install the "TOTO Washlet" integration
6. Restart Home Assistant

### Manual Installation

1. Copy the `custom_components/toto_washlet` folder to your Home Assistant `config/custom_components/` directory
2. Restart Home Assistant

## Configuration

1. In Home Assistant, go to **Settings** > **Devices & services**
2. Click **Add integration**
3. Search for **TOTO Washlet**
4. Select the infrared emitter entity that points at the Washlet
5. Optionally select an infrared receiver entity in the integration options

## Support

Open an issue on GitHub if you find a bug or have a supported-model report:

https://github.com/dudeofawesome/home-assistant-toto-washlet/issues
