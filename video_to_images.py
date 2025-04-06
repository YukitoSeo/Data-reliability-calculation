import os
import cv2

########################
#フレーム画像に変換する動画までのパス(.mp4)
videoPath = "" 

#フレーム画像の保存先
output_dir = ""
########################

#動画を画像に切り出して保存するプログラム
def save_all_frames(video_path, dir_path, basename, ext='png'):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)
    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))
    n = 0
    count = 0

    while True:
        ret, frame = cap.read()

        if ret:
            cv2.imwrite('{}_{}.{}'.format(base_path, str(n).zfill(digit), ext), frame)
            n += 1
        else:
            return

cap = cv2.VideoCapture(videoPath)
print(f"frame_count: {cap.get(cv2.CAP_PROP_FRAME_COUNT)}")

save_all_frames(videoPath, output_dir, 'frame')