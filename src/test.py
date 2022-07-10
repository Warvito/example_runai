import os

from monai.config import print_config

print("Hello world")

print_config()

for k, v in os.environ.items():
    print(f'{k}={v}')
