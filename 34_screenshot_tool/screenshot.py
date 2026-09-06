#!/usr/bin/env python3
"""
Screenshot Tool
Cross-platform screenshot capture. Uses Pillow's ImageGrab (Windows/Mac), or pyscreenshot on Linux if Pillow not available.
"""

import sys
from pathlib import Path
from datetime import datetime

try:
    from PIL import ImageGrab
except Exception:
    ImageGrab = None

try:
    import pyscreenshot as ImageGrabFallback
except Exception:
    ImageGrabFallback = None


def capture(save_dir: Path, filename: str = None):
    save_dir = save_dir.expanduser().resolve()
    save_dir.mkdir(parents=True, exist_ok=True)
    if not filename:
        filename = datetime.now().strftime('screenshot_%Y%m%d_%H%M%S.png')
    out = save_dir / filename
    if ImageGrab:
        img = ImageGrab.grab()
        img.save(out)
    elif ImageGrabFallback:
        img = ImageGrabFallback.grab()
        img.save(out)
    else:
        raise RuntimeError('No screenshot backend available. Install Pillow or pyscreenshot.')
    return out


def main():
    save_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('~').expanduser() / 'Pictures'
    try:
        out = capture(save_dir)
        print('Saved screenshot to', out)
    except Exception as e:
        print('Error:', e)
        sys.exit(1)


if __name__ == '__main__':
    main()
