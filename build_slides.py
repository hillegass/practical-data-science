import os

top_dir = '.'

# We need a place to put html files as they are created
tank_dir = os.path.join(top_dir, 'tmp')
os.system(f"rm -rf {tank_dir}")
os.makedirs(tank_dir)

# This is where the slides will be built
html_dir = os.path.join(top_dir, "slides")

# Look for directories that have a slides.md file
filelist = []
for path in os.listdir(top_dir):
    slide_path = os.path.join(top_dir, path, 'slides.md')
    if os.path.isfile(slide_path):

        path_end = path.find('_')
        if path_end > 0:
            prefix = path[:path_end]
        else:
            prefix = path[:2]

        # Where is the media for this slide?
        media_filename = prefix + '_media'
        media_path = os.path.join(top_dir, path, media_filename)
        os.system(f"mdslides {slide_path} --include {media_path}")

        # Move the index.html to the tank
        index_path = os.path.join(top_dir, "slides", "index.html")
        new_filename = f"{path}.html"
        filelist.append(new_filename)
        new_location = os.path.join(tank_dir, new_filename)
        os.rename(index_path, new_location)

        # Move the media to the tank
        slide_media_path = os.path.join(top_dir, "slides", media_filename)
        new_slide_media_path = os.path.join(tank_dir, media_filename)
        os.rename(slide_media_path, new_slide_media_path)
filelist.sort()
indexf = open(os.path.join(tank_dir, "index.html"), 'w')

indexf.write("""
<!doctype html>
<html><head><title>All Slides</title></head>
   <body>
""")

for filename in filelist:
    indexf.write(f"<p><a href=\"{filename}\">{filename}</a>")
indexf.write("</body></html>")
indexf.close()
        
# Move the stuff in the tank to the slides directory
os.system(f"mv {tank_dir}/* {html_dir}")

# Move in the custom stylesheet
os.system("cp *.css slides/dist/theme/")
        
        
