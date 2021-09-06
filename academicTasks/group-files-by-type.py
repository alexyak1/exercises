# Your computer's hard drive is almost full.
# In order to make some space, you need to complite some file statistics.

# music ("mp3", "aac", "flac")
# image ("jpg", "bmp", "gif")
# move ("mp4", "avi", "mkv")
# other as instance ("7z", "txt", "zip")

# S = "my.song.mp3 11b /n greatSong.flac 100b /n not3.txt 5b"


def solution(S):
    music = ["mp3", "aac", "flac"]
    image = ["jpg", "bmp", "gif"]
    movie = ["mp4", "avi", "mkv"]
    # other = ["7z", "txt", "zip"] just example

    result = {"music": 0, "images": 0, "movies": 0, "other": 0}

    files = S.split("\n")
    for one_file in files:
        splited = one_file.split(" ")
        file_format = splited[0].split(".")[-1]
        file_size = splited[1][:-1]

        if file_format in music:
            result["music"] = result["music"] + int(file_size)
        elif file_format in image:
            result["images"] = result["images"] + int(file_size)
        elif file_format in movie:
            result["movies"] = result["movies"] + int(file_size)
        else:
            result["other"] = result["other"] + int(file_size)

    result_list = "\n".join([f"{key} {value}b" for key, value in result.items()])
    return result_list
