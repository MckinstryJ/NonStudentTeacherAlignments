import glob
import subprocess

in_path = 'path_to_wavs_directory'
out_path = 'path_to_output_directory'

sr = 16000

for file in glob.glob(in_path + '*.wav'):
    output_file = out_path + file[len(in_path):]
    subprocess.call(f"sox \"{file}\" -c 1 -r {sr} \"{output_file}\"", shell=True)
