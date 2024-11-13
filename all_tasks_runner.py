import sys
import os
import glob


PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PATH)
LABS_NAMES = [f'Lab{i}' for i in range(1, 9)]


def run_tasks(labs_names=LABS_NAMES):
    for lab_name in labs_names:
        lab_path = os.path.join(PATH, lab_name)

        if os.path.exists(lab_path):
            for file in glob.iglob(f"{lab_name}/*/src/main.py"):
                os.system("python " + file)

if __name__ == '__main__':
    run_tasks()