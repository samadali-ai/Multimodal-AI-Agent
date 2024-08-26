import replicate

def text2image(text: str) -> str:
    """This tool is useful when we want to generate images from textual descriptions."""
    output = replicate.run(
        "xlabs-ai/flux-dev-controlnet:f2c31c31d81278a91b2447a304dae654c64a5d5a70340fba811bb1cbd41019a2",
        input={
            "steps": 28,
            "prompt": text,
            "lora_url": "",
            "control_type": "depth",
            "control_image": "https://replicate.delivery/pbxt/LUSNInCegT0XwStCCJjXOojSBhPjpk2Pzj5VNjksiP9cER8A/ComfyUI_02172_.png",
            "lora_strength": 1,
            "output_format": "webp",
            "guidance_scale": 2.5,
            "output_quality": 100,
            "negative_prompt": "low quality, ugly, distorted, artefacts",
            "control_strength": 0.45,
            "depth_preprocessor": "DepthAnything",
            "soft_edge_preprocessor": "HED",
            "image_to_image_strength": 0,
        }
    )
    print(output)
    return output[0]
