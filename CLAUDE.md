# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

DigiMotion は動画を一定間隔（例: 1秒ごと）でフレーム抽出し、中間の動きを間引くことで、被写体がまるで浮遊しながら移動しているように見える映像を生成するツールです。NHK「ピタゴラスイッチ」のデジタルウォークの概念を汎用化したもの。

- 言語: Python（動画処理は OpenCV / ffmpeg を想定）
- 出力先 `output/`、`frames/`、`tmp/` は `.gitignore` 対象

詳細なコーディング規約・セキュリティルールは `.github/copilot-instructions.md` を参照。

## Commands

```bash
# 依存パッケージのインストール
pip install -r requirements.txt

# 実行
python main.py <input_video>
python main.py sample.mp4 --interval 0.5 --output output/result.mp4

# ヘルプ
python main.py --help
```

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
