from PIL import Image, ImageDraw, ImageFont
import os

def create_icon(size, output_path):
    # Create a gradient background
    img = Image.new('RGB', (size, size), color='white')
    draw = ImageDraw.Draw(img)
    
    # Draw gradient circles
    for i in range(size // 2):
        color_val = int(102 + (118 - 102) * (i / (size / 2)))
        draw.ellipse([i, i, size - i, size - i], 
                    outline=(color_val, 126, 234), 
                    width=2)
    
    # Draw bell emoji/icon
    # Simple bell shape
    bell_size = size // 2
    x_center = size // 2
    y_center = size // 2
    
    # Bell body
    points = [
        (x_center - bell_size // 3, y_center - bell_size // 4),
        (x_center + bell_size // 3, y_center - bell_size // 4),
        (x_center + bell_size // 2, y_center + bell_size // 3),
        (x_center - bell_size // 2, y_center + bell_size // 3)
    ]
    draw.polygon(points, fill=(102, 126, 234))
    
    # Bell top
    draw.ellipse([
        x_center - bell_size // 6, 
        y_center - bell_size // 2,
        x_center + bell_size // 6,
        y_center - bell_size // 4
    ], fill=(118, 74, 162))
    
    # Save
    img.save(output_path)

# Generate icons
sizes = [16, 48, 128]
for size in sizes:
    create_icon(size, f'/home/claude/zara-monitor/extension/icons/icon{size}.png')
    print(f'Created icon{size}.png')
