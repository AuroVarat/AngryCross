import glob

# All files ending with .txt with depth of 2 folder
listed = glob.glob("*/*.mp4")

import moviepy.editor as moviepy
i = 0 
for movie in listed:
    clip = moviepy.VideoFileClip(movie)
    name = movie.split("/")[0]
    name = name+"/"+name+str(i)+".gif"
  
    clip.write_gif(name)
  
    i +=1