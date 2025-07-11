import os
from PIL import Image, ImageDraw, ImageFont

def generate_thumbnail(video_type, title, output_path):
    try:
        # Define colors
        background_color = (30, 30, 30) if video_type == "short" else (15, 15, 60)
        text_color = (255, 255, 255)
        box_color = (255, 99, 71)
        label_bg = (255, 255, 255)
        label_fg = (0, 0, 0)

        # Canvas dimensions
        width, height = 1280, 720
        thumbnail = Image.new("RGB", (width, height), color=background_color)
        draw = ImageDraw.Draw(thumbnail)

        # Font path
        font_path = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
        title_font = ImageFont.truetype(font_path, 72)
        label_font = ImageFont.truetype(font_path, 36)

        # Add emoji prefix to title
        if "🎬" not in title:
            title = f"🎬 {title}"

        # Wrap text for title
        max_line_width = 1000
        words = title.split()
        lines = []
        current_line = ""
        for word in words:
            test_line = f"{current_line} {word}".strip()
            if draw.textlength(test_line, font=title_font) < max_line_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word
        if current_line:
            lines.append(current_line)

        # Calculate vertical position
        total_text_height = sum(title_font.getbbox(line)[3] + 20 for line in lines)
        start_y = (height - total_text_height) // 2

        # Draw each line of the title
        for line in lines:
            text_width = draw.textlength(line, font=title_font)
            text_height = title_font.getbbox(line)[3]
            x = (width - text_width) // 2
            y = start_y
            draw.rectangle((x - 30, y - 20, x + text_width + 30, y + text_height + 20), fill=box_color)
            draw.text((x, y), line, fill=text_color, font=title_font)
            start_y += text_height + 40

        # Draw label: "🤖 AI Generated"
        label_text = "🤖 AI Generated"
        label_width = draw.textlength(label_text, font=label_font)
        label_height = label_font.getbbox(label_text)[3]
        padding = 20
        label_x = width - label_width - padding
        label_y = height - label_height - padding

        draw.rectangle((label_x - 10, label_y - 10, label_x + label_width + 10, label_y + label_height + 10), fill=label_bg)
        draw.text((label_x, label_y), label_text, fill=label_fg, font=label_font)

        # Save the thumbnail
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        thumbnail.save(output_path, "JPEG")
        print(f"✅ Thumbnail saved: {output_path}")

    except Exception as e:
        print(f"❌ Error generating thumbnail: {e}")
