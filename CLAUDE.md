# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

DigiMotion is a video processing tool. The project is in early development — no source code exists yet beyond environment configuration.

## Environment Configuration

Copy `.env.example` to `.env` and adjust values as needed:

```
DEFAULT_FRAME_INTERVAL=1.0   # Seconds between frames
DEFAULT_SKIP_FRAMES=2        # Number of frames to skip
OUTPUT_QUALITY=95            # Output quality (0-100)
OUTPUT_FORMAT=mp4            # Output video format
LOG_LEVEL=INFO               # Logging verbosity
NUM_THREADS=4                # Worker thread count
```
