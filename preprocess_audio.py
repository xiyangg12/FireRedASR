#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import argparse
import subprocess

def main():
    parser = argparse.ArgumentParser(
        description="Convert all WAVs in input_dir to 16 kHz mono PCM WAVs and save to output_dir."
    )
    parser.add_argument("--input_dir", "-i", required=True,
                        help="Root directory containing input WAV files (e.g., segmented pairs).")
    parser.add_argument("--output_dir", "-o", required=True,
                        help="Directory to write converted WAV files.")
    args = parser.parse_args()

    in_dir = os.path.abspath(args.input_dir)
    out_dir = os.path.abspath(args.output_dir)
    os.makedirs(out_dir, exist_ok=True)

    print(f"Converting WAVs from:\n  {in_dir}\n→ {out_dir}\n")

    for sub in sorted(os.listdir(in_dir)):
        sub_in = os.path.join(in_dir, sub)
        if not os.path.isdir(sub_in):
            continue

        sub_out = os.path.join(out_dir, sub)
        os.makedirs(sub_out, exist_ok=True)

        for fname in sorted(os.listdir(sub_in)):
            if not fname.endswith(".wav"):
                continue

            inp = os.path.join(sub_in, fname)
            out = os.path.join(sub_out, fname)

            cmd = [
                "ffmpeg", "-hide_banner", "-loglevel", "error",
                "-y", "-i", inp,
                "-ar", "16000", "-ac", "1",
                "-acodec", "pcm_s16le", "-f", "wav", out
            ]
            subprocess.run(cmd, check=True)

    print("\n✅ All conversions complete.")

if __name__ == "__main__":
    main()
