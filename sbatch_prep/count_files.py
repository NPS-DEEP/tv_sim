#!/usr/bin/env python3.6
import os, glob, json, shutil
from os.path import exists

if __name__=="__main__":
    glob_path_500="/smallwork/bdallen/executable_files_500/*/*.tmp"
    glob_path_1000="/smallwork/bdallen/executable_files_1000/*/*.tmp"
    glob_path_from_neil="/smallwork/bdallen/executable_files_from_neil/*/*.tmp"
    glob_path_tv_500="/smallwork/bdallen/executable_files_500/*/*.tv"
    glob_path_tv_1000="/smallwork/bdallen/executable_files_1000/*/*.tv"
    glob_path_tv_from_neil="/smallwork/bdallen/executable_files_from_neil/*/*.tv"
    dest_path_tv_500="/smallwork/bdallen/tv_files_500/*.tv"
    dest_path_tv_1000="/smallwork/bdallen/tv_files_1000/*.tv"

    paths = [
             glob_path_500,
             glob_path_1000,
             glob_path_from_neil,
             glob_path_tv_500,
             glob_path_tv_1000,
             glob_path_tv_from_neil,
             dest_path_tv_500,
             dest_path_tv_1000,
            ]

    for path in paths:
        files = glob.glob(path)
        print("count for %s: %d"%(path, len(files)))
