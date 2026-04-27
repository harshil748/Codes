from PIL import Image, ImageDraw, ImageFont

W, H = 1400, 820
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

try:
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 28)
    font_sub = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 17)
    font_sm = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
    font_xs = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
except:
    font_title = font_sub = font_sm = font_xs = ImageFont.load_default()

draw.text((W//2, 30), "VoiceAPI - Use Case Diagram", fill="black", font=font_title, anchor="mm")

# System boundary
draw.rectangle([160, 70, 1100, 790], outline="#555555", width=2)
draw.text((630, 88), "VoiceAPI System", fill="#555555", font=font_sub, anchor="mm")

def actor(x, y, label):
    draw.ellipse([x-20, y-45, x+20, y-5], outline="black", width=2)
    draw.line([x, y-5, x, y+35], fill="black", width=2)
    draw.line([x-25, y+10, x+25, y+10], fill="black", width=2)
    draw.line([x, y+35, x-18, y+65], fill="black", width=2)
    draw.line([x, y+35, x+18, y+65], fill="black", width=2)
    for i, part in enumerate(label.split("\n")):
        draw.text((x, y+80+i*18), part, fill="black", font=font_sm, anchor="mm")

actor(80, 280, "End User\n(Web UI)")
actor(80, 560, "Developer\n(API)")

def usecase(cx, cy, text, color_border, color_fill, color_text):
    draw.ellipse([cx-155, cy-30, cx+155, cy+30], outline=color_border, width=2, fill=color_fill)
    draw.text((cx, cy), text, fill=color_text, font=font_xs, anchor="mm")

# End User cases
eu_cases = [
    (400, 160, "Select Language & Voice"),
    (400, 250, "Enter Text for Synthesis"),
    (400, 340, "Control Style (Speed / Pitch / Energy)"),
    (400, 430, "Upload WAV for Voice Cloning"),
    (400, 520, "Play & Download Audio"),
]
for cx, cy, txt in eu_cases:
    usecase(cx, cy, txt, "#1565C0", "#E3F2FD", "#0D47A1")
    draw.line([110, 280, cx-155, cy], fill="#888", width=1)

# Developer cases
dev_cases = [
    (750, 180, "POST /synthesize"),
    (750, 280, "POST /clone"),
    (750, 380, "POST /batch"),
    (750, 480, "GET /voices & /styles"),
    (750, 580, "POST /preload & /unload"),
    (750, 680, "GET|POST /Get_Inference"),
]
for cx, cy, txt in dev_cases:
    usecase(cx, cy, txt, "#2E7D32", "#E8F5E9", "#1B5E20")
    draw.line([110, 560, cx-155, cy], fill="#888", width=1)

# TTS Engine box
draw.rectangle([920, 250, 1090, 620], outline="#E65100", width=2, fill="#FFF3E0")
draw.text((1005, 275), "TTS Engine", fill="#E65100", font=font_sub, anchor="mm")
for i, item in enumerate(["Text Normalizer", "Tokenizer", "Style Processor", "VITS / Coqui", "MMS / XTTS v2"]):
    draw.text((1005, 315 + i*55), item, fill="#BF360C", font=font_xs, anchor="mm")

# include arrows
draw.line([555, 250, 595, 280], fill="#999", width=1)
draw.text((570, 255), "<<include>>", fill="#777", font=font_xs, anchor="mm")

img.save(r"C:\Code\Codes\use_case_diagram.png")
print("Done")
