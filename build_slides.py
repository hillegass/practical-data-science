import os

top_dir = '.'

# We need a place to put html files as they are created
tank_dir = os.path.join(top_dir, 'tmp')
os.system(f"rm -rf {tank_dir}")
os.makedirs(tank_dir)

# This is where the slides will be built
html_dir = os.path.join(top_dir, "slides")

# Look for directories that have a slides.md file
for path in os.listdir(top_dir):
    slide_path = os.path.join(top_dir, path, 'slides.md')
    if os.path.isfile(slide_path):

        # Where is the media for this slide?
        media_filename = path[:2] + '_media'
        media_path = os.path.join(top_dir, path, media_filename)
        os.system(f"mdslides {slide_path} --include {media_path}")

        # Move the index.html to the tank
        index_path = os.path.join(top_dir, "slides", "index.html")
        new_location = os.path.join(tank_dir, f"{path}.html")
        os.rename(index_path, new_location)

        # Move the media to the tank
        slide_media_path = os.path.join(top_dir, "slides", media_filename)
        new_slide_media_path = os.path.join(tank_dir, media_filename)
        os.rename(slide_media_path, new_slide_media_path)

# Move the stuff in the tank to the slides directory
os.system(f"mv {tank_dir}/* {html_dir}")

# Move in the custom stylesheet
os.system("cp *.css slides/dist/theme/")
        
        
