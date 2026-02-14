import argparse
import vertexai
from vertexai.preview.vision_models import ImageGenerationModel

def generate_bouquet_image(
    project_id: str, location: str, output_file: str, prompt: str
):
    """Generate an image using a text prompt."""
    # Initialize Vertex AI
    vertexai.init(project=project_id, location=location)

    # Load the image generation model
    model = ImageGenerationModel.from_pretrained("imagen-3.0-generate-002")

    # Generate the image
    images = model.generate_images(
        prompt=prompt,
        number_of_images=1,
        seed=1,
        add_watermark=False,
    )

    # Save the first image
    images[0].save(output_file)
    print(f"Image saved to {output_file}")

    return images

# Run the function
generate_bouquet_image(
    project_id='qwiklabs-gcp-02-9ad999e3e626',
    location='us-central1',
    output_file='image.jpeg',
    prompt='Create an image containing a bouquet of 2 sunflowers and 3 roses',
)
