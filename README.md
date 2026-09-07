# AnonChatBot

A cross-platform rewrite of an old screen-reading Telegram automation project.

AnonChatBot is being rebuilt from scratch with a cleaner architecture, portable dependencies, and a simple rule: platform-specific code should end before screen processing and OCR begin.

> Status: active rewrite. The project is not ready for normal use yet.

## What it is meant to do

AnonChatBot should be able to:

- locate a supported Telegram client window;
- support both Telegram Desktop and AyuGram where possible;
- determine the window position and dimensions;
- capture only the required screen region;
- convert the captured region into a Pillow image;
- pass that image to OCR;
- react to recognised text without being tied to one operating system.

The current rewrite deliberately separates window discovery, screen capture, OCR, and application logic so each part can be changed without rebuilding the rest of the project.

## Architecture

```text
window backend
    ↓
window bounds
    ↓
screen capture
    ↓
PIL.Image.Image
    ↓
OCR
    ↓
text
    ↓
application logic
```

Current source layout:

```text
src/anonchatbot/
├── local/
│   └── types.py
├── screen/
│   └── capture.py
└── window/
    ├── locator.py
    ├── linux.py
    ├── windows.py
    └── macos.py
```

## Platform status

| Platform | Status | Notes |
| --- | --- | --- |
| Linux / X11 | In progress | Window discovery is currently being implemented with `python-xlib`. |
| Windows | Planned | Will use a Windows-specific backend while keeping the same public interface. |
| macOS | Unverified | Backend is intentionally not considered supported until tested on real hardware. |

macOS development policy:

```text
Implementation derived from documentation.
Hardware verification: none.
Paranormal verification: pending.
```

Wayland support is not implemented yet. Window discovery under Wayland requires a different approach from X11.

## Current progress

Working now:

- monitor-aware screen capture with `mss`;
- local capture regions using named coordinates;
- validation for invalid or out-of-bounds regions;
- conversion from `mss.screenshot.ScreenShot` to `PIL.Image.Image`;
- operating-system dispatch structure;
- Linux X11 connection and root-window access;
- reading `_NET_CLIENT_LIST` from the X11 window manager.

Still to do:

- finish Linux window discovery and geometry retrieval;
- map a found Telegram/AyuGram window to the correct monitor;
- calculate the Telegram chat region relative to the window;
- add OCR;
- add Windows window discovery;
- verify or implement macOS support;
- connect recognition results to the actual automation behaviour.

## Dependencies

The project currently uses:

- `mss` — fast cross-platform screen capture;
- `Pillow` — image representation and processing;
- `python-xlib` — Linux/X11 window discovery;
- `RapidOCR` / ONNX Runtime — planned OCR layer;
- `PyAutoGUI` — portable keyboard/mouse automation where appropriate.

Python 3.12 or newer is required.

## Installation

This project uses `uv`.

```bash
 git clone git@github.com:UrrovenGrrunta/AnonChatBot.git
 cd AnonChatBot
 uv sync
```

Run project modules during development with `uv run`.

Example:

```bash
uv run src/anonchatbot/window/linux.py
```

## Design goals

The rewrite follows a few practical rules:

- screen capture should not care which Telegram client is being used;
- OCR should receive an image and know nothing about the operating system;
- platform-specific APIs stay inside their own backend modules;
- coordinates are validated before reaching lower-level libraries;
- temporary experiments are acceptable while behaviour is still being understood;
- once behaviour is understood, the code gets cleaned up.

The code style follows PEP 8 together with UGPEP — UrrovenGrrunta Python Enhancement Proposal.

## Development status

AnonChatBot is currently a development project and APIs may change without warning.

The old implementation is used only as a reference for behaviour. The current repository is a fresh rewrite rather than a refactor of the original codebase.
