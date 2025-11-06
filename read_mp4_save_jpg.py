import cv2
import os

# 输入视频路径
video_path = "D:/MyData/NewProject@Jeff/icra26/website/materials/extreme-case/compare.mp4"

# 输出帧保存目录
output_folder = "D:/MyData/NewProject@Jeff/icra26/website/game4grasp.github.io/static/interpolation/stacked"
os.makedirs(output_folder, exist_ok=True)

# 打开视频文件
cap = cv2.VideoCapture(video_path)

loop_count, frame_count = 0, 0
while True:
    if loop_count % 6 == 0:
        ret, frame = cap.read()
        if not ret or frame_count >= 100:
            break

        # 保存帧为 jpg 图片
        save_path = os.path.join(output_folder, f"{frame_count:06d}.jpg")
        cv2.imwrite(save_path, frame)
        
        frame_count += 1
    loop_count += 1

cap.release()
