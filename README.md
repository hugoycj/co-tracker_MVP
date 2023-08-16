---
title: co-tracker_MVP
emoji: 🐠
colorFrom: gray
colorTo: blue
sdk: gradio
sdk_version: 3.38.0
app_file: app.py
pinned: false
license: apache-2.0
---

# An Out-Of-The-Box Version of CoTracker
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/chongjie/co-tracker_MVP)

## Introduction
Video motion prediction is a crucial task in computer vision, typically relying on either estimating the instantaneous motion of all points in a video frame using optical flow, or tracking the motion of individual points throughout the video independently. However, tracking points individually can overlook the strong correlation that often exists between points, especially when they originate from the same physical object, potentially impacting performance.

[CoTracker](https://co-tracker.github.io/) introduces a novel approach to this problem by proposing an architecture that jointly tracks multiple points throughout an entire video. This architecture is based on several ideas from the optical flow and tracking literature, and combines them in a new, flexible, and powerful design. It is based on a transformer network that models the correlation of different points in time via specialized attention layers.

[Demo Video](https://co-tracker.github.io/videos/teaser/bmx-bumps.mp4 "Demo Video")

## Usage

There are several ways you can use or interact with this project:

* **Direct Use**: If you want to use the space directly without any modifications, simply click [here](https://huggingface.co/spaces/chongjie/co-tracker_MVP). This will take you to the live application where you can interact with it as is.

* **Duplicate the Space**: If you want to create a copy of this space for your own use or modifications, click [here](https://huggingface.co/spaces/chongjie/co-tracker_MVP/settings?duplicate=true). This will create a duplicate of the space under your account, which you can then modify as per your needs.

* **Run with Docker**: If you prefer to run the application locally using Docker, you can do so with the following command:

    ```bash
    docker run -it -p 7860:7860 --platform=linux/amd64 \
	registry.hf.space/chongjie-co-tracker-mvp:latest python app.py
    ```

## Acknowledgments
This repository is based on original [CoTracker](https://github.com/facebookresearch/co-tracker)