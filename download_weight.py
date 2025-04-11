import gdown, os
from pathlib import Path

# 1. Google Drive file URL
url = "https://drive.google.com/uc?id=13TxxDZvai-5xQEN-D7d1ElMm_q5ZibDv"  
output_file = "vit_ft_quick_draw.pth"
weight_folder = Path('weight')
weight_folder.mkdir(exist_ok=True)
gdown.download(url, os.path.join(weight_folder, output_file), quiet=False)

print(f"Downloaded '{output_file}' successfully.")
