from PIL import Image, ImageDraw, ImageSequence

# Create a function to generate frames
def create_frame(color, size=(100, 100)):
    img = Image.new('RGB', size, 'white')
    draw = ImageDraw.Draw(img)
    draw.ellipse((25, 25, 75, 75), fill=color)
    return img

# Define the colors and durations
colors = ['red', 'darkgreen']
durations = [120, 200]  # durations in milliseconds

# Generate the frames
frames = [create_frame(color) for color in colors]

# Save the frames as a GIF
frames[0].save('color_changing_circle.gif', save_all=True, append_images=frames[1:], duration=durations, loop=0)