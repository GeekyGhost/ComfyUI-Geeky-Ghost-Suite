#image input and output template
import torch
from PIL import Image

class ExtractFramesTest:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": { "image_in" : ("IMAGE", {}) },
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image_out",)
    FUNCTION = "extract_frames"
    CATEGORY = "👻 Geeky Ghost"

    def extract_frames(self, image_in):
        image_out = image_in
        return (image_out,)

NODE_CLASS_MAPPINGS = {
    "ExtractFramesTest": ExtractFramesTest
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ExtractFramesTest": "ExtractFramesTest"
}
