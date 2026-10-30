import os

base = "C:/Users/Admin/Documents/GitHub/hellocrmwebsite/src"
if os.path.exists(base):
    dirs = [d for d in os.listdir(base) if os.path.isdir(os.path.join(base, d))]
    print("Directories in src:", dirs)
    
    # Check if there are data or config files
    for root, subdirs, files in os.walk(base):
        for f in files:
            if any(k in f.lower() for k in ["pricing", "features", "navigation", "competitor", "matrix", "plans"]):
                print(os.path.join(root, f))
else:
    print("Base path not found:", base)

