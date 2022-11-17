''' Generates different render views from an .xyz file. 
    - Reads a .blend file as a template
    - Imports the .xyz file using imort_mesh.xyz addon (needs to be downloaded)
    - Generates 3 views (acording to the template currently loaded)
    - Settings have to be done in an input file. Only mandatory keyword is "files_to_render".
    - Not sure what indir will do, as currently using only ./ directory as input_dir
    - out_dir given by -o option will put the generated images in that dir
    '''
import bpy
import os
import sys       # to get command line args
import argparse  # to parse options for us and print a nice help message

sys.path.append("/home/captainbroccoli/scripts/sci/blender")
import config as cfg  # Moudle containing global variables

# get the args passed to blender after "--", all of which are ignored by
# blender so scripts may receive their own arguments
argv = sys.argv

if "--" not in argv:
    argv = []  # as if no args are passed
else:
    argv = argv[argv.index("--") + 1:]  # get all args after "--"

# When --help or no args are given, print this help
usage_text = \
"Run blender in background mode with this script:"
"  blender --background --python " + __file__ + " -- [options]"
"  blender -b -P " + __file__ + " -- [options]"

parser = argparse.ArgumentParser(description=usage_text)
parser.add_argument("-i", "--indir", dest="input_path", type=str,
        help="Path to be used to take the images")
parser.add_argument("-o", "--outdir", dest="out_path", type=str,
        help="Path to be used to render the movie. If nothing given,"
        "the 'indir' path will be used instead")
parser.add_argument("-f", "--file", dest="config_file", type=str,
        help="File containing the configuration settings")
args = parser.parse_args(argv)  # In this example we wont use the args

def read_input (filename):
    ''' Read input file given as -f option'''

    import os
    import sys
    import config  as cfg

    print ("----------")
    if isinstance(filename, str):
        f = open(filename)
    else: # Assume it's a file-like object
        f = filename
    data  = f.readlines()

    for n,line in enumerate(data):
        keyword = line.split()[0]
        if keyword is '#' or  keyword == '!':
            pass
        elif keyword == 'resx':
            value = line.split()[1]
            cfg.resx = int(value)
        elif keyword == 'resy':
            value = line.split()[1]
            cfg.resy = int(value)
        elif keyword == 'format':
            value = line.split()[1]
            cfg.format = str(value)
        elif keyword == 'prefix':
            value = line.split()[1]
            cfg.prefix = str(value)
        elif keyword == 'blend_file':
            value = line.split()[1]
            cfg.blend_file = str(value)
        elif keyword == 'thickness_mode':
            value = line.split()[1]
            cfg.thickness_mode = str(value)
        elif keyword == 'thickness':
            value = line.split()[1]
            cfg.thickness = float(value)
        elif keyword == 'lens':
            value = line.split()[1]
            cfg.lens = float(value)
        # Fill up the list with paths to files to render and its suffixes
        elif keyword == 'files_to_render':
            print ("Reading files to render")
            i=n+1
            file_path = data[i].split()[0]
            try:
                file_suffix = data[i].split()[1]
            except:
                file_suffix = ''
                pass
            while True:
                if file_path is '#':
                    i += 1
                    file_path = data[i].split()[0]
                    try:
                        file_suffix = data[i].split()[1]
                    except:
                        file_suffix = ''
                        pass
                    pass
                if file_path != 'end':
                    cfg.files_to_render.append((file_path,file_suffix))
                    i += 1
                    file_path = data[i].split()[0]
                    try:
                        # CHCK IF STRIPS WORKS
                        file_suffix = data[i].split()[1].strip()
                    except:
                        file_suffix = ''
                        pass
                else:
                    break

    print ("----------")

if not args.input_path:
    print("Warning: --indir=\"some path\" argument not given. Current dir will be used instead.")
    in_dir = os.getcwd() + "/"
else:
    in_dir = args.input_path
if not args.out_path:
    out_dir = in_dir
    print("Warning: --outdir will be the same as --indir")
else:
    out_dir = args.out_path
candidates = []
if not args.config_file:
    print ("please give a cofig file with -f option")
else:
    read_input(args.config_file)

for f in cfg.files_to_render:
    # Open the .blend template
    bpy.ops.wm.open_mainfile(filepath=cfg.blend_file)
    # Load the file to be rendered
    # f = ( /path/to/the/file.xyz , suffix_for_this_file ) 
    file_path = f[0]
    file_suffix = f[1]
    bpy.ops.import_mesh.xyz (filepath=file_path)

    bpy.data.scenes["Scene"].render.resolution_x = cfg.resx
    bpy.data.scenes["Scene"].render.resolution_y = cfg.resy
    bpy.data.scenes["Scene"].render.resolution_percentage = 100
    bpy.data.scenes["Scene"].render.image_settings.file_format = cfg.format
    bpy.data.scenes["Scene"].render.line_thickness_mode = cfg.thickness_mode
    bpy.data.scenes["Scene"].render.line_thickness = cfg.thickness

    # # Show the obects on the scene
    # for i in bpy.data.objects:
    #     print (i)

    bpy.data.cameras["Camera"].lens = cfg.lens
    bpy.data.cameras["Camera.001"].lens = cfg.lens
    bpy.data.cameras["Camera.002"].lens = cfg.lens

    # Set each camera and render
    bpy.context.scene.camera = bpy.data.objects["Camera"]
    bpy.data.scenes["Scene"].render.filepath = out_dir + cfg.prefix + file_suffix +   "v1." + cfg.format.lower()
    bpy.ops.render.render( animation=False, write_still=True)
    # 
    bpy.context.scene.camera = bpy.data.objects["Camera.001"]
    bpy.data.scenes["Scene"].render.filepath = out_dir + cfg.prefix + file_suffix +   "v2." + cfg.format.lower()
    bpy.ops.render.render( animation=False, write_still=True)
    # 
    bpy.context.scene.camera = bpy.data.objects["Camera.002"]
    bpy.data.scenes["Scene"].render.filepath = out_dir + cfg.prefix + file_suffix +   "v3." + cfg.format.lower()
    bpy.ops.render.render( animation=False, write_still=True)
