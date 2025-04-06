from PIL import Image
import io

def resize_and_compress_image(input_path, output_path, target_width, target_height, target_size_kb):
    # Open an image file
    with Image.open(input_path) as img:
        # Resize image
        img = img.resize((target_width, target_height), Image.ANTIALIAS)
        
        # Compress image
        buffer = io.BytesIO()
        quality = 85  # Initial quality level
        img.save(buffer, format="JPEG", quality=quality)
        
        # Reduce quality until the target size is reached
        while buffer.tell() > target_size_kb * 1024 and quality > 10:
            buffer = io.BytesIO()
            quality -= 5
            img.save(buffer, format="JPEG", quality=quality)
        
        # Save the compressed image
        with open(output_path, "wb") as f:
            f.write(buffer.getvalue())

# Example usage
resize_and_compress_image("input.jpg", "output.jpg", 200, 230, 50)