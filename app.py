import json
import random
from PIL import Image, ImageSequence

bg_gif_names = ["Dark Net", "Dark Sky", "Flare Orbs", "Gradient Waves", "Lava", "Songbird Surge", "Stars", "Time Travel", "Trip", "Vortex"]
IMG_APES = 75

def output_ape_gif(bg_num, ape_num):
    gif_bg = Image.open('assets/gifbgs/' + bg_gif_names[bg_num] + '.gif')
    png_ape = Image.open('assets/pngapes/' + str(ape_num) + '.png')
    frames = [f.copy() for f in ImageSequence.Iterator(gif_bg)]
    gif_ape = []
    for frame in frames:
        frame.paste(png_ape, (0, 0), mask = png_ape)
        gif_ape.append(frame)
    gif_ape[1].save(
        'outputs/gifapes/' + str(ape_num) + '.gif',
        save_all = True,
        append_images = gif_ape[1:],
        loop = 0
    )
    print("Finished Ape No : " + str(ape_num))
    return

def update_ape_json(bg_num, ape_num):
    with open('assets/apesjson/' + str(ape_num) + '.json', 'r') as ape_json_file:
        file_contents = ape_json_file.read()
    parsed_json = json.loads(file_contents)
    parsed_json["attributes"][0]["value"] = bg_gif_names[bg_num]
    dumped_json = json.dumps(parsed_json, indent=2)

    with open('outputs/jsonapes/' + str(ape_num) + '.json', 'w') as ape_json_file2:
        ape_json_file2.write(dumped_json)
    return

def create_ape_gifs():
    for k in range(IMG_APES):
        rnd_bg = random.randint(0, 9)
        output_ape_gif(rnd_bg, k + 1)
        update_ape_json(rnd_bg, k + 1)
    return

create_ape_gifs()