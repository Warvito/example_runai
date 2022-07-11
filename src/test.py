import os
from monai.config import print_config
from pathlib import Path

print("Hello world")

print_config()

for k, v in os.environ.items():
    print(f'{k}={v}')

home_dir = Path("/home/wds20")
print(f" /home/wds20/ exists? {home_dir.is_dir()}")
