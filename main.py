"""
DigiMotion CLI

Usage:
    python main.py <input_video> [options]

Examples:
    python main.py sample.mp4
    python main.py sample.mp4 --interval 0.5 --output output/result.mp4
"""

import argparse
import logging
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

from digimotion.processor import process_video

load_dotenv()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="DigiMotion: generate a floating-motion video by sampling frames at regular intervals."
    )
    parser.add_argument("input", help="Path to the input video file")
    parser.add_argument(
        "--output", "-o",
        help="Path for the output video (default: output/<input_stem>_digimotion.<format>)",
    )
    parser.add_argument(
        "--interval", "-i",
        type=float,
        default=float(os.getenv("DEFAULT_FRAME_INTERVAL", 1.0)),
        help="Seconds between key frames (default: %(default)s)",
    )
    parser.add_argument(
        "--quality", "-q",
        type=int,
        default=int(os.getenv("OUTPUT_QUALITY", 95)),
        help="Output quality 0-100 (default: %(default)s)",
    )
    parser.add_argument(
        "--format", "-f",
        default=os.getenv("OUTPUT_FORMAT", "mp4"),
        help="Output format extension (default: %(default)s)",
    )
    parser.add_argument(
        "--threads",
        type=int,
        default=int(os.getenv("NUM_THREADS", 4)),
        help="Number of processing threads (default: %(default)s)",
    )

    args = parser.parse_args()

    log_level = os.getenv("LOG_LEVEL", "INFO").upper()
    logging.basicConfig(
        level=getattr(logging, log_level, logging.INFO),
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S",
    )

    input_path = args.input
    if not Path(input_path).exists():
        print(f"Error: input file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    if args.output:
        output_path = args.output
    else:
        stem = Path(input_path).stem
        output_path = f"output/{stem}_digimotion.{args.format}"

    process_video(
        input_path=input_path,
        output_path=output_path,
        frame_interval=args.interval,
        output_quality=args.quality,
        num_threads=args.threads,
    )


if __name__ == "__main__":
    main()
