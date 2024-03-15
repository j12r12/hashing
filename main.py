import sys
import os
import imagehash
from PIL import Image


def create_hash_dict(file_list):
  hash_file_dict = {}
  for file in file_list:
    img = Image.open(file)
    hashed = imagehash.average_hash(img)
    hash_file_dict[hashed] = file
  return hash_file_dict

if __name__ == "__main__":

  if len(sys.argv) != 3:
      print("Usage: python3 main.py directory1 directory2")
      sys.exit(200)

  dir1 = sys.argv[1]
  dir2 = sys.argv[2]

  files1 = [os.path.join(dir1, f) for f in os.listdir(dir1) if f.endswith(".jpg")]
  files2 = [os.path.join(dir2, f) for f in os.listdir(dir2) if f.endswith(".jpg")]

  dir1_dict = create_hash_dict(files1)
  dir2_dict = create_hash_dict(files2)

  intersection = set(dir1_dict.keys()).intersection(set(dir2_dict.keys()))

  dups = [(dir1_dict[i], dir2_dict[i]) for i in intersection] 

  print("Duplicate files...")
  print(dups)
