#!/usr/bin/env bash
export XDG_STATE_HOME="$HOME/Library/Application Support/state"
mkdir -p "$XDG_STATE_HOME"
uv run marimo edit example.py