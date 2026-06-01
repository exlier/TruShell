import subprocess

from trushell.chronoterm import sound
from trushell import pyfunny


def test_play_alarm_uses_quiet_subprocess(monkeypatch):
    calls = []
    monkeypatch.setattr(sound.sys, "platform", "linux")

    def fake_which(name: str) -> str | None:
        return "/usr/bin/" + name if name == "paplay" else None

    class FakeResult:
        returncode = 0

    def fake_run(cmd, stdout, stderr, check):
        calls.append({"cmd": cmd, "stdout": stdout, "stderr": stderr, "check": check})
        return FakeResult()

    monkeypatch.setattr(sound.shutil, "which", fake_which)
    monkeypatch.setattr(sound.subprocess, "run", fake_run)

    sound.play_alarm()

    assert calls
    assert calls[0]["stdout"] == subprocess.DEVNULL
    assert calls[0]["stderr"] == subprocess.DEVNULL
    assert calls[0]["check"] is False
    assert calls[0]["cmd"][0] == "paplay"


def test_play_sound_uses_requested_sound_file(monkeypatch, tmp_path):
    sound_file = tmp_path / "custom-sound.mp3"
    sound_file.write_text("not real audio")
    calls = []

    monkeypatch.setattr(pyfunny, "_sound_path", lambda filename: sound_file)

    def fake_play_file(path):
        calls.append(path)

    monkeypatch.setattr(sound, "play_audio_file", fake_play_file, raising=False)
    monkeypatch.setattr(pyfunny, "play_audio_file", fake_play_file, raising=False)

    pyfunny._play_sound("custom-sound.mp3")

    assert calls == [sound_file]
