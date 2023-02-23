import io

import torch
from donut import DonutModel
from PIL import Image

from fastapi import Form, File, UploadFile


async def POST(photo: UploadFile = File()):
    # Use donut fine-tuned on an OCR dataset.
    task_prompt = "<s_cord-v2>"
    pretrained_model = DonutModel.from_pretrained(
        "naver-clova-ix/donut-base-finetuned-cord-v2", cache_dir='/root/model_cache'
    )

    # Initialize model.
    pretrained_model.half()
    device = torch.device("cuda")
    pretrained_model.to(device)

    # Run inference.
    input_img = Image.open(io.BytesIO(photo.file.read()))
    output = pretrained_model.inference(image=input_img, prompt=task_prompt)[
        "predictions"
    ][0]

    return {"output": str(output)}
