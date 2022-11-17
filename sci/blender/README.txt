Generates different render views from an .xyz file using blender and cycles. 
The script has to be run with blender: 

  blender --background|-b --python|-P  /path/to/the/script.py -- [options]

  where [options]: 
   --indir | -i  : Not sure what it will do in this script. Avoid. ( FIXME )
   --outdir | -o : Directory where the images will be saved
   --file | -f   : file with the settings and the mandatory files_to_render keyword

Keywords 
========

# This is a comment
resx  integer [1080]
resy  integer [1080]
format  string (PNG| JPG ...) [PNG]
thickness_mode  ABSOLUTE|RELATIVE [ABSOLUTE]
thickness float [0.3]
prefix string [tip_]
blend_file string ( path/where/is/the/blend_file.blend )
# No comments are allowd inside files_to_render (or maybe yes? CHECK )
files_to_render [mandatory]
 /path/to/the/file.xyz   surffix_for_this_file
 /path/to/the/file_2.xyz   surffix_for_this_file_2
 /path/to/the/file_3.xyz   surffix_for_this_file_3
end
# Note the files_to_render needs an end to indicate when it finishes.

IMPORTANT: Do not leave blank lines in the input_file. Even at the end of the file!
           An empty comment is allowed though.
