import timm
import torch

model_name = "vit_base_patch16_384"
model_official = timm.create_model(model_name, pretrained=True)
model_official.eval()
print(type(model_official))

# Save the model weights
torch.save(model_official.state_dict(), "weight/model.pth")