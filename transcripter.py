from pathlib import Path
import json, os, subprocess, tempfile, shutil
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

root = Path(__file__).parent / "videos"
out = Path("transcripts.json")
client = Groq(api_key=os.environ["GROQ_API_KEY"])

def ffmpeg_bin() -> str:
    candidates = [
        os.getenv("FFMPEG_BIN"),
        shutil.which("ffmpeg"),
        r"C:\Program Files\ffmpeg\bin\ffmpeg.exe",
        r"C:\Program Files (x86)\ffmpeg\bin\ffmpeg.exe",
    ]
    winget_root = Path(os.getenv("LOCALAPPDATA", "")) / "Microsoft/WinGet/Packages"
    candidates += [str(p) for p in winget_root.glob("**/ffmpeg.exe")]
    for c in candidates:
        if c and Path(c).exists():
            return c
    raise FileNotFoundError("ffmpeg não encontrado; defina FFMPEG_BIN no .env ou adicione ao PATH")

def extract_audio(video: Path) -> Path:
    fd, tmp_path = tempfile.mkstemp(suffix=".mp3")
    os.close(fd)  # fecha o descritor antes do ffmpeg no Windows
    tmp = Path(tmp_path)
    subprocess.run(
        [ffmpeg_bin(), "-y", "-i", str(video), "-vn", "-acodec", "libmp3lame", str(tmp)],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return tmp

def transcribe(audio: Path) -> str:
    with audio.open("rb") as f:
        r = client.audio.transcriptions.create(model="whisper-large-v3", file=f)
    return r.text

def main():
    data = {}
    for creator_dir in root.iterdir():
        if not creator_dir.is_dir():
            continue
        creator = creator_dir.name
        data[creator] = []
        for video in creator_dir.glob("*"):
            if not video.is_file():
                continue
            audio = extract_audio(video)
            try:
                data[creator].append({"video": video.name, "text": transcribe(audio)})
            finally:
                audio.unlink(missing_ok=True)
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

if __name__ == "__main__":
    main()