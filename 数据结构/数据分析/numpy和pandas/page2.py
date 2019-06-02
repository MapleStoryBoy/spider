import numpy as np


us_file_path = "./youtube_video_data/US_video_data_numbers.csv"
uk_file_path = "./youtube_video_data/GB_video_data_numbers.csv"


t1 = np.loadtxt(us_file_path,delimiter=",",dtype="int",unpack=True)


print(t1)





