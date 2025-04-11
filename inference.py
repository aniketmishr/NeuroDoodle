from torchvision import transforms
from model import VisionTransformer
import torch 

def pipeline(image, device = 'cpu', threshold = 0.5): 
    model_path = "weight/vit_ft_quick_draw.pth"
    quickdraw_labels = dict(enumerate(open("classes.txt")))
    model_config = {
    'img_size':384,
    'patch_size':16,
    "in_chans":3,
    "n_classes":len(quickdraw_labels),
    "embed_dim":768,
    "depth":12,
    "n_heads":12,
    "mlp_ratio":4.,
    "qkv_bias":True,
    'p':0.,
    "attn_p":0.,
}
    assert len(image.getbands()) == 3, "The number of channels in Image must be 3"
    transform = transforms.Compose([
    transforms.Resize(384), 
    transforms.ToTensor(), 
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])
    img_tensor = transform(image).unsqueeze(0).to(device) #(1,3,384,384)
    model = VisionTransformer(**model_config).to(device)
    model.load_state_dict(torch.load(model_path, weights_only=True, map_location=torch.device(device)))
    with torch.no_grad(): 
        output = model(img_tensor)
        output = torch.nn.functional.softmax(output, dim=1)
    prob, pred = torch.max(output,1)
    label = quickdraw_labels[pred.item()]
    print(pred)
    print(prob)
    return f'{label} ( {int(prob.item()*100)}% sure )' if prob.item()>threshold else "Not Sure!"

