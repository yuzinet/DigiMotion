"""
Core video processing logic for DigiMotion.

Extracts key frames at regular intervals and holds each frame for the
duration of the interval, creating the "digital walk" floating effect.
"""

import logging
import os
from pathlib import Path

import cv2

logger = logging.getLogger(__name__)


def process_video(
    input_path: str,
    output_path: str,
    frame_interval: float = 1.0,
    output_quality: int = 95,
    num_threads: int = 4,
) -> None:
    """
    Generate a DigiMotion video from the input video.

    Args:
        input_path: Path to the source video file.
        output_path: Path for the output video file.
        frame_interval: Seconds between key frames to extract.
        output_quality: JPEG quality hint (0-100); used when encoding with ffmpeg.
        num_threads: Number of OpenCV threads to use.
    """
    cv2.setNumThreads(num_threads)

    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        raise FileNotFoundError(f"Cannot open video: {input_path}")

    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / fps if fps > 0 else 0

    frames_per_interval = max(1, round(fps * frame_interval))

    logger.info(
        "Input: %s  |  %.1f fps  |  %dx%d  |  %.1fs",
        input_path, fps, width, height, duration,
    )
    logger.info(
        "Key frame every %.2fs (%d source frames held per interval)",
        frame_interval, frames_per_interval,
    )

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    frame_idx = 0
    key_frame = None

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_idx % frames_per_interval == 0:
            key_frame = frame
            logger.debug("Key frame captured at frame %d (%.2fs)", frame_idx, frame_idx / fps)

        writer.write(key_frame)
        frame_idx += 1

    cap.release()
    writer.release()

    logger.info("Output saved: %s", output_path)
