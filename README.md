# Sentiment-Classification-Via-Galvanic-Skin-Response-Based-on-Deep-Learning-Models 

# Table of Contents  

- [Introduction](#intro1)
- [MDSTC](#mdstc2)
- [Preprocessed](#PROCESS3)
- [Denoising](#denoising4)

<a name="intro1"></a>
## Sentiment Classification Via Galvanic Skin Response ##
### Introduction
We collected a a multimodal dataset for sentiment classification, the dataset is showed in MDSTC. The Facial Expression of the MDSTC folder contains facial expressions of volunteers watching emotional stimulation clips. The GSR and Pulse File folder contains Galvanic Skin Response and Pulse of volunteers. In this paper, we used Galvanic Skin Response for sentiment classificaiton


<a name="mdstc2"></a>
## MDSTC ##
In this section, we will show the detail of MDSTC.

This image shows the facial expressions of volunteers watching six types of inspired videos. In the XML file, "Person_info" record the personal information of volunteer, "Film_name" denotes the name of stimulation clips, "PIDIAN" recorded the Galvanic Skin Response, "MAIBO" recorded the pulse.
![image](https://github.com/HTDPNJ/Sentiment-Classification-Via-Galvanic-Skin-Response-Based-on-Deep-Learning-Models/blob/master/Pic/git.png)

This image shows the Galvanic Skin Response and Pulse of volunteers watching six types of inspired videos.
![image](https://github.com/HTDPNJ/Sentiment-Classification-Via-Galvanic-Skin-Response-Based-on-Deep-Learning-Models/blob/master/Pic/xml.png)

<a name="PROCESS3"></a>
## Preprocessed ##
If a small amount of data is missing, we fill it with adjacent data. If a large amount of data is missing in a, we delete the data.


<a name="denoising4"></a>
## Denoising and Data standardization ##
We use the Butterworth filter to denoise the signal, enhance the
useful information, and recover the information degradation
caused by the interference..
