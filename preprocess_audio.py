import os
import subprocess

in_dir = "/home/xiyali/data/Whisper/Mandi_CMN_SST_split"
out_dir = "/home/xiyali/data/FireRedASR/data"
os.makedirs(out_dir, exist_ok=True)

for speaker in os.listdir(in_dir):
    speaker_dir = os.path.join(in_dir, speaker)
    out_speaker_dir = os.path.join(out_dir, speaker)
    for fname in os.listdir(speaker_dir):
        if fname.endswith(".wav"):
            inp = os.path.join(speaker_dir, fname)
            out = os.path.join(out_speaker_dir, fname)
            if not os.path.exists(out_speaker_dir):
                os.mkdir(out_speaker_dir)
            cmd = [
                "ffmpeg", "-y", "-i", inp,
                "-ar", "16000", "-ac", "1",
                "-acodec", "pcm_s16le", "-f", "wav", out
            ]
            subprocess.run(cmd, check=True)