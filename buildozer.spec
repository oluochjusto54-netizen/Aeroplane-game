
- name: Build APK
  shell: bash
  run: |
    source .venv/bin/activate
    python -m pip install appdirs "colorama>=0.3.3" jinja2 "sh>=2,<3.0" meson ninja build toml packaging setuptools "wheel~=0.43.0"
    buildozer android debug
