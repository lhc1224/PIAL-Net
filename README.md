# PIAL-Net
1. [📎 Paper Link](#1)
2. [💡 Abstract](#2)
3. [📖 Method](#3)
4. [📂 Dataset](#4)
5. [📊 Experimental Results](#5)
6. [✉️ Statement](#6)
7. [✨ Other Relevant Works](#7)
8. [🔍 Citation](#8)

## 📎 Paper Link <a name="1"></a> 
* Leverage Interactive Affinity for Affordance Learning  [[PDF](https://openaccess.thecvf.com/content/CVPR2023/papers/Luo_Leverage_Interactive_Affinity_for_Affordance_Learning_CVPR_2023_paper.pdf)]
> Authors:
> Hongchen Luo, Wei Zhai, Jing Zhang, Yang Cao, Dacheng Tao

## 💡 Abstract <a name="2"></a> 
Perceiving potential "action possibilities" (i.e., affordance) regions of images and learning interactive functionalities of objects from human demonstration is a challenging task due to the diversity of human-object interactions. Prevailing affordance learning algorithms often adopt the label assignment paradigm and presume that there is a unique relationship between functional region and affordance label, yielding poor performance when adapting to unseen environments with large appearance variations. In this paper, we propose to leverage interactive affinity for affordance learning, i.e., extracting interactive affinity from human-object interaction and transferring it to non-interactive objects. Interactive affinity, which represents the contacts between different parts of the human body and local regions of the target object, can provide inherent cues of interconnectivity between humans and objects, thereby reducing the ambiguity of the perceived action possibilities. Specifically, we propose a pose-aided interactive affinity learning framework that exploits human pose to guide the network to learn the interactive affinity from human-object interactions. Particularly, a keypoint heuristic perception (KHP) scheme is devised to exploit the keypoint association of human pose to alleviate the uncertainties due to interaction diversities and contact occlusions. Besides, a contact-driven affordance learning (CAL) dataset is constructed by collecting and labeling over 5,000 images. Experimental results demonstrate that our method outperforms the representative models regarding objective metrics and visual quality. 
<p align="center">
    <img src="./img/fig1.jpg" width="600"/> <br />
    <em> 
    </em>
</p>


**Interactive affinity.** (a) This paper explores the associations of interactable regions between diverse images by considering the context of contact regions with different body parts. (b) This paper considers leveraging the connection of human pose keypoints to alleviate the uncertainties due to interaction diversities and contact occlusions.

	

<p align="center">
    <img src="./img/motivation.jpg" width="700"/> <br />
    <em> 
    </em>
</p>

**Motivation.**  (a) This paper explores the associations of interactable regions between diverse images by considering the context of contact regions with different body parts. (b) This paper considers leveraging the connection of human pose keypoints to alleviate the uncertainties due to interaction diversities and contact occlusions.

## 📖 Method <a name="3"></a> 

<p align="center">
    <img src="./img/method.jpg" width="800"/> <br />
    <em> 
    </em>
</p>

**Overview of the proposed pose-aided interactive affinity learning framework.** Our model mainly consists of an interactive feature enhancement (IFE) module and a keypoint heuristic perception (KHP) scheme.

## 📂 Dataset <a name="4"></a> 

<p align="center">
    <img src="./img/dataset.jpg" width="800"/> <br />
    <em> 
    </em>
</p>

You can download the CAL dataset from [ [Google Drive](https://drive.google.com/drive/folders/1GrDUoLAQHRnqMbYu2mYBexxMfbZZfmPf?usp=share_link) | [Baidu Pan](https://pan.baidu.com/s/1pANrZ36EIur_8hfH0vda4g) (ap83) ].

**Some examples and properties of Contact-driven Affordance Learning (CAL) dataset.** (a) Statistics on the quantity of interactive and non-interactive images in each affordance category. (b) Confusion matrix for each affordance category interacting with body parts. (c) Some examples of interactive and non-interactive images and annotations in the dataset.

## 📊 Experimental Results <a name="5"></a> 

<p align="center">
    <img src="./img/result1.jpg" width="800"/> <br />
    <em> 
    </em>
</p>

**The results of different methods on the CAL dataset.** 

<p align="center">
    <img src="./img/result2.jpg" width="800"/> <br />
    <em> 
    </em>
</p>


**Visualization of prediction results.** We show the visualization results of our model, few-shot segmentation (HSNet [33]), the best human pose estimation model (HRFormer [68]) and the segmentation model (SegFormer [61]).

## ✉️ Statement <a name="6"></a> 
For any other questions please contact [lhc12@mail.ustc.edu.cn](lhc12@mail.ustc.edu.cn) or [wzhai056@ustc.edu.cn](wzhai056@ustc.edu.cn).

## ✨ Other Relevant Works <a name="7"></a> 

1.The paper "One-Shot Affordance Detection" was accepted by IJCAI2021 and the corresponding paper and code are available from  the [[link](https://github.com/lhc1224/OSAD_Net)].

2.The paper "Phrase-Based Affordance Detection via Cyclic Bilateral Interaction" was accepted by IEEE Transactions on Artificial Intelligence (T-AI). The papers and code can be downloaded from the [[link](https://github.com/lulsheng/CBCE-Net)].

3.The paper "Learning Affordance Grounding from Exocentric Images" was accepted by CVPR22 and the corresponding paper and code are available from [[link](https://github.com/lhc1224/Cross-View-AG)].

4.The paper "Grounding 3D Object Affordance from 2D Interactions in Images" and corresponding code are obtained from the [[link](https://github.com/yyvhang/IAGNet)].

## 🔍 Citation <a name="8"></a> 

```
@InProceedings{Luo_2023_CVPR,
    author    = {Luo, Hongchen and Zhai, Wei and Zhang, Jing and Cao, Yang and Tao, Dacheng},
    title     = {Leverage Interactive Affinity for Affordance Learning},
    booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
    month     = {June},
    year      = {2023},
    pages     = {6809-6819}
}
```
