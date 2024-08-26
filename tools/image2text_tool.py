import replicate

def image2text(image_url: str, prompt: str) -> str:
    """This tool is useful when we want to generate textual descriptions from images."""
    output = replicate.run(
        "yorickvp/llava-13b:80537f9eead1a5bfa72d5ac6ea6414379be41d4d4f6679fd776e9535d1eb58bb",
        input={
            "image": image_url,
            "top_p": 1,
            "prompt": prompt,
            "max_tokens": 1024,
            "temperature": 0.2
        }
    )
    return "".join(output)
