import gradio as gr
import os
import torch
import numpy as np

from PIL import Image
from cotracker.utils.visualizer import Visualizer, read_video_from_path
from cotracker.predictor import CoTrackerPredictor

checkpoint='./checkpoints/cotracker_stride_4_wind_8.pth'
def cotracker(video_path: str, grid_size: int, grid_query_frame: int, backward_tracking: bool):
    # load the input video frame by frame
    video = read_video_from_path(video_path)
    video = torch.from_numpy(video).permute(0, 3, 1, 2)[None].float()
    model = CoTrackerPredictor(checkpoint=checkpoint)
    if torch.cuda.is_available():
        model = model.cuda()
        video = video.cuda()
    else:
        print("CUDA is not available!")

    pred_tracks, pred_visibility = model(
        video,
        grid_size=grid_size,
        grid_query_frame=grid_query_frame,
        backward_tracking=backward_tracking,
    )
    print("computed")

    # save a video with predicted tracks
    seq_name = video_path.split("/")[-1]
    vis = Visualizer(save_dir="./saved_videos", pad_value=120, linewidth=3)
    vis.visualize(video, pred_tracks, query_frame=grid_query_frame)

    return "./saved_videos/video_pred_track.mp4"

iface = gr.Interface(
    fn=cotracker, 
    inputs=[
        gr.inputs.Video(label='video', type='mp4'),
        gr.inputs.Slider(minimum=0, maximum=20, step=1, default=10, label="Grid Size"),
        gr.inputs.Slider(minimum=0, maximum=10, step=1, default=0, label="Grid Query Frame"),
        gr.inputs.Checkbox(label="Backward Tracking"),
    ], 
    outputs=gr.outputs.Video(label="Output")
)
iface.queue()
iface.launch()