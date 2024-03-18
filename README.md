# Talking Head Label Requirement

## 1. Resolution & Quality

+ **4K**  
+ Facial region rates more than **15%** in whole frame.
+ **Facial features** are sharply defined, with **intricate details** and **distinct teeth.**

## 2. Video Format

+ **Mp4** is highly recommended

## 3. Content

+ Speaking directly to the camera.
+ Only  continuous speaking segments.
+ The background is random without limitation.
+ **Take special notice !!!**
  + Segments where background individuals are speaking or there is background audio while the foreground focused person is not speaking are **not allowed.**
  + Excessive background noise is also **not allowed**.
  + Avoid any sudden movements of the head (such as rapid rotation or quick movements).

## 4. Speaker

+ Chinese .
+ English.
+ Languages tailored for specific **application scenarios.**

## 5. Distribution of Speaker

+ 60% of young people.
+ 20% of elderly.
+ 20% of children.

## 6. Number of Videos

+ A total of 50 hours of video content .
+ As many speaker as possible.

## 7. Accessible Open Source Dataset

> Summary

+ | Dataset Name | Year | Hours | Image_size(resol, fps) | Speaker | Sentence | Head pose | Envir |
  | ------------ | ---- | ----- | ---------------------- | ------- | -------- | --------- | ----- |
  | GRID         | 2006 | 27.5  | 720x576, 25            | 33      | 33K      | N         | Lab   |
  | LRW          | 2017 | 173   | 256x256, 25            | 1K+     | 539K     | N         | TV    |
  | ObamaSet     | 2017 | 14    | N/A, 25                | 1       | N/A      | Y         | TV    |
  | VoxCeleb2    | 2018 | 2.4k  | N/A                    | 6.1K+   | 153.5K   | Y         | TV    |
  | MEAD         | 2020 | 39    | 1920x1080, 30          | 60      | 20       | Y         | Lab   |
  | HDTF         | 2021 | 15.8  | 1080x720/1920x1080, 30 | 362     | 10K      | Y         | TV    |

+ **LSR2**（Lipreading Sentences 2)

  | **Set**    | **Dates**       | **# utterances** | **# word instances** | **Vocab** |
  | ---------- | --------------- | ---------------- | -------------------- | --------- |
  | Pre-train  | 11/2010-06/2016 | 96,318           | 2,064,118            | 41,427    |
  | Train      | 11/2010-06/2016 | 45,839           | 329,180              | 17,660    |
  | Validation | 06/2016-09/2016 | 1,082            | 7,866                | 1,984     |
  | Test       | 09/2016-03/2017 | 1,243            | 6,663                | 1,698     |

+ **LRW**

  | **Set**    | **Dates**               | **# class** | **# per class** |
  | ---------- | ----------------------- | ----------- | --------------- |
  | Train      | 01/01/2010 - 31/08/2015 | 500         | 800-1000        |
  | Validation | 01/09/2015 - 24/12/2015 | 500         | 50              |
  | Test       | 01/01/2016 - 30/09/2016 | 500         | 50              |

+ **LSR3-TED**

  | **Set**   | **# videos** | **# utterances** | **# word instances** | **Vocab** |
  | --------- | ------------ | ---------------- | -------------------- | --------- |
  | Pre-train | 5,090        | 118,516          | 3.9M                 | 51k       |
  | Trainval  | 4,004        | 31,982           | 358k                 | 17k       |
  | Test      | 412          | 1,321            | 10k                  | 2k        |

+ **HDTF5**

  + The original videos in the dataset are either in 720P or 1080P resolution.
  + Each cropped video within the dataset is resized to a resolution of 512 x 512.
  + We now can download 404 video.

+ **VoxCeleb1**

  | dev                 | **test** |       |
  | ------------------- | -------- | ----- |
  | **# of speakers**   | 1,211    | 40    |
  | **# of videos**     | 21,819   | 677   |
  | **# of utterances** | 148,642  | 4,874 |

+ **VoxCeleb2**

  |                     | **dev**   | **test** |
  | ------------------- | --------- | -------- |
  | **# of speakers**   | 5,994     | 118      |
  | **# of videos**     | 145,569   | 4,911    |
  | **# of utterances** | 1,092,009 | 36,237   |

+ **MEAD**

  + Emotional dataset
  + Conclude total **60** ID
  + Every ID has **7 head positions**
    + down
    + front
    + left_30
    + left_60
    + right_30
    + right_60
    + tops
  + Every position has **8 emotions**
    + angry
    + contempt
    + disgusted
    + fear
    + happy
    + neutral
    + sad
    + surprised
  + Every emotion has **3 different levels**

## 8. More

+ **Youtubev1**
  + Our high resolution dataset
  + Total 1000 mkv video.
  + Just raw without processed
