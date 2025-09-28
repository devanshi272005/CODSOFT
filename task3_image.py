import os

# Define a simple rule-based caption dictionary
caption_rules = {
    "dog.jpg": "A happy dog playing in the garden.",
    "cat.jpg": "A curious cat sitting on the windowsill.",
    "sunset.jpg": "A beautiful sunset over the ocean.",
    "car.jpg": "A red sports car parked on the street.",
    "mountain.jpg": "Snow-covered mountains under a clear blue sky."
}

def generate_caption(image_path):
    filename = os.path.basename(image_path)
    caption = caption_rules.get(filename, "No caption available for this image.")
    return caption

# Example usage
if __name__ == "__main__":
    print("Rule-Based Image Captioning")
    image_path = input("Enter the image filename (e.g., dog.jpg): ")
    caption = generate_caption(image_path)
    print(f"Caption: {caption}")
