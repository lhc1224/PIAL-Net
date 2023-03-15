# PIAL-Net
PyTorch implementation of our PIAL models. 
The code will coming soon.
1. [📎 Paper Link](#1)
2. [💡 Abstract](#2)
3. [📖 Method](#3)
4. [📂 Dataset](#4)
5. [📊 Experimental Results](#7)
6. [✉️ Statement](#8)
7. [✨ Other Relevant Works](#9)
8. [🔍 Citation](#10)

## 📎 Paper Link <a name="1"></a> 
* Learning Affordance Grounding from Exocentric Images (CVPR2022) [[pdf]()] [[Supplementary Material]()]
> Authors:
> Hongchen Luo, Wei Zhai, Jing Zhang, Yang Cao, Dacheng Tao

## 💡 Abstract <a name="2"></a> 
Perceiving potential "action possibilities" (i.e., affordance) regions of images and learning interactive functionalities of objects from human demonstration is a challenging task due to the diversity of human-object interactions. Prevailing affordance learning algorithms often adopt the label assignment paradigm and presume that there is a unique relationship between functional region and affordance label, yielding poor performance when adapting to unseen environments with large appearance variations. In this paper, we propose to leverage interactive affinity for affordance learning, i.e., extracting interactive affinity from human-object interaction and transferring it to non-interactive objects. Interactive affinity, which represents the contacts between different parts of the human body and local regions of the target object, can provide inherent cues of interconnectivity between humans and objects, thereby reducing the ambiguity of the perceived action possibilities. Specifically, we propose a pose-aided interactive affinity learning framework that exploits human pose to guide the network to learn the interactive affinity from human-object interactions. Particularly, a keypoint heuristic perception (KHP) scheme is devised to exploit the keypoint association of human pose to alleviate the uncertainties due to interaction diversities and contact occlusions. Besides, a contact-driven affordance learning (CAL) dataset is constructed by collecting and labeling over 5,000 images. Experimental results demonstrate that our method outperforms the representative models regarding objective metrics and visual quality. 
<p align="center">
    <img src="./img/fig1.jpg" width="600"/> <br />
    <em> 
    </em>
</p>

**Observation.** By observing the exocentric diverse interactions, the human learns affordance knowledge determined by the object’s intrinsic properties and transfer it to the egocentric view.

<p align="center">
    <img src="./img/Motivation.png" width="700"/> <br />
    <em> 
    </em>
</p>

**Motivation.** (a) Exocentric interactions can be decomposed into affordance-specific features M and differences in individual habits E. (b) There are co-relations between affordances, e.g.“Cut with” inevitably accompanies “Hold” and is independent of the object category (knife and scissors). Such co-relation is common between objects. In this paper, we mainly consider extracting affordance-specific cues M from diverse interactions while preserving the affordance co-relations to enhance the perceptual capability of the network.


## 📖 Method <a name="3"></a> 

<p align="center">
    <img src="./img/Method.png" width="800"/> <br />
    <em> 
    </em>
</p>

**Overview of the proposed cross-view knowledge transfer affordance grounding framework.** It mainly consists of an Affordance Invariance Mining (AIM) module and an Affordance Co-relation Preservation (ACP) strategy. The AIM module (see in Sec. 3.1) aims to obtain invariant affordance representations from diverse exocentric interactions. The ACP strategy (see in Sec. 3.2) enhances the network’s affordance perception by aligning the co-relation of the outputs of the two views.

## 📂 Dataset <a name="4"></a> 

<p align="center">
    <img src="./img/dataset.png" width="800"/> <br />
    <em> 
    </em>
</p>

**The properties of the AGD20K dataset.** (a) Some examples from the dataset. (b) The distribution of categories in AGD20K. (c) The word cloud distribution of affordances in AGD20K. (d) Confusion matrix between the affordance category and the object category in AGD20K, where the horizontal axis denotes the object category and the vertical axis denotes the affordance category.

## 📊 Experimental Results <a name="7"></a> 

<p align="center">
    <img src="./img/result1.png" width="800"/> <br />
    <em> 
    </em>
</p>

**The results of different methods on AGD20k.** The best results are in bold. “Seen” means that the training set and the test set contain the same object categories, while “Unseen” means that the object categories in the training set and the test set do not overlap. The * defines the relative improvement of our method over other methods. “Dark red”, “Orange” and “Purple” represent saliency detection, weakly supervised object localization and affordance grounding models, respectively.

<p align="center">
    <img src="./img/result2.png" width="800"/> <br />
    <em> 
    </em>
</p>


**Visual affordance heatmaps on the AGD20K dataset.** We select the prediction results of representative methods of affordance grounding (Hotspots [33]), weakly supervised object localization (EIL [30]), and saliency detection (DeepGazeII [21]) for presentation.

## ✉️ Statement <a name="8"></a> 
This project is for research purpose only, please contact us for the licence of commercial use. For any other questions please contact [lhc12@mail.ustc.edu.cn](lhc12@mail.ustc.edu.cn) or [wzhai056@mail.ustc.edu.cn](wzhai056@mail.ustc.edu.cn).

## ✨ Other Relevant Works <a name="9"></a> 

1.The paper "One-Shot Affordance Detection" was accepted by IJCAI2021 and the corresponding paper and code are available from [https://github.com/lhc1224/OSAD_Net](https://github.com/lhc1224/OSAD_Net).

2.The language-annotated PAD-L dataset is available for download via [ [link](https://arxiv.org/abs/2202.12076) ], and related papers and code can be downloaded from the [[link](https://github.com/lulsheng/CBCE-Net)].

## 🔍 Citation <a name="9"></a> 

```
@inproceedings{Leverageluo,
  title={Leverage Interactive Affinity for Affordance Learning},
  author={Luo, Hongchen and Zhai, Wei and Zhang, Jing and Cao, Yang and Tao, Dacheng},
  booktitle={CVPR},
  year={2023}
}
```