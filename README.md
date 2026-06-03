# Real-Time Object Detection using Multi-Thresholding and Intel RealSense

This project implements a real-time object detection system using image multi-thresholding techniques and an Intel RealSense D435 camera. The objective is to segment an image into multiple intensity regions and detect specific objects automatically, displaying bounding boxes around each detected object.

The system was developed as part of a Computer Vision course and focuses on classical image processing techniques rather than machine learning approaches.

## Project Objectives

* Capture live video from an Intel RealSense camera.
* Apply automatic multi-threshold segmentation.
* Detect multiple objects in real time.
* Generate bounding boxes around detected objects.
* Label detected objects within the scene.

## Scenario Description

Three physical objects were selected to create a simple real-world scenario:

| Object | Color  | Purpose                            |
| ------ | ------ | ---------------------------------- |
| Lid    | Blue   | Support base                       |
| Ramp   | Red    | Access path                        |
| Camel  | Yellow | Object that moves through the ramp |

The objects interact as a small environment where the ramp is placed on top of the lid, allowing the camel to climb.

## Hardware and Software

### Hardware

* Intel RealSense D435 Camera

### Software

* Python 3.11
* OpenCV
* NumPy
* pyrealsense2

## Methodology

### 1. Video Acquisition

The Intel RealSense camera captures RGB frames in real time.

The setup was carefully arranged to reduce shadows and improve segmentation quality.

### 2. Grayscale Conversion

Captured images are converted from:

```text
BGR → Grayscale
```

This reduces computational complexity by transforming the image into a single intensity channel.

Advantages:

* Faster processing
* Simpler segmentation
* Reduced sensitivity to color variations

### 3. Multi-Threshold Segmentation

The grayscale image is divided into multiple intensity regions.

Configuration:

* 4 intensity levels
* 3 object regions
* 1 background region

Threshold values are generated automatically across the intensity range:

```text
0 – 255
```

Each pixel is assigned to one of the four regions, producing a segmented image with different gray levels.

### 4. Object Detection

After segmentation:

* Connected regions are identified.
* Small contours are removed as noise.
* Relevant objects are selected.
* Contours are extracted.

### 5. Bounding Box Generation

For each detected object:

* A bounding rectangle is generated.
* An object identifier is displayed.
* Detection results are visualized in real time.

## Processing Pipeline

```text
Camera Frame
      ↓
Grayscale Conversion
      ↓
Multi-Threshold Segmentation
      ↓
Contour Detection
      ↓
Noise Filtering
      ↓
Object Selection
      ↓
Bounding Box Generation
      ↓
Real-Time Visualization
```

## Results

The system successfully achieved:

* Real-time camera visualization.
* Automatic multi-threshold segmentation.
* Detection of multiple objects.
* Bounding box generation.
* Object labeling.
* Simultaneous display of original and segmented images.

Key outcomes:

* 4-level automatic thresholding.
* Robust object localization.
* Low computational requirements.
* Real-time execution.

## Technologies

* Python
* OpenCV
* NumPy
* Intel RealSense SDK (pyrealsense2)

## Applications

The techniques implemented in this project can be extended to:

* Industrial inspection
* Object counting
* Robotics
* Pick-and-place systems
* Quality control
* Educational computer vision systems

## Future Improvements

* Adaptive thresholding methods.
* Otsu multi-level thresholding.
* Morphological filtering.
* Color-based segmentation in HSV space.
* Object tracking across frames.
* Depth information integration using RealSense sensors.
* Machine learning-based object recognition.

## Learning Outcomes

This project provides practical experience in:

* Image segmentation
* Thresholding techniques
* Contour extraction
* Real-time computer vision
* Camera interfacing
* Classical object detection methods

## Author

Universidad de Guanajuato – Computer Vision Course

Rafael Alejandro Frías Cortez
