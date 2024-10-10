import os
import cv2
import json
import numpy as np
import torch
def read_heatmap_json(json_file,k_ratio=3):
    with open(json_file, 'r') as load_f:
            json_data = json.load(load_f)
            k_size = int(np.sqrt(json_data['image_height'] * json_data['image_width']) / k_ratio)
            if k_size % 2 == 0:
                k_size += 1
            # Compute the heatmap using the Gaussian filter.
            #### heatmap1
            heatmap1 = np.zeros((json_data['image_height'], json_data['image_width']),dtype=np.float32)
            point1s = json_data['kps1']
            for point in point1s:
                x = point[1]
                y = point[0]
                row = int(x)
                col = int(y)
                try:
                    heatmap1[row, col] += 1.0
                except:
                    # resize pushed it out of bounds somehow
                    row = min(max(row, 0), json_data['image_height'] - 1)
                    col = min(max(col, 0), json_data['image_width'] - 1)
                    heatmap1[row, col] += 1.0
            heatmap1 = cv2.GaussianBlur(heatmap1, (k_size, k_size), 0)
            heatmap1=cv2.resize(heatmap1,(224,224))
            heatmap1 = (heatmap1 - np.min(heatmap1)) / (np.max(heatmap1) - np.min(heatmap1) + 1e-10)
           
            #### heatmap2
            heatmap2 = np.zeros((json_data['image_height'], json_data['image_width']), dtype=np.float32)
            point2s = json_data['kps2']
            for point in point2s:
                x = point[1]
                y = point[0]
                row = int(x)
                col = int(y)
                try:
                    heatmap2[row, col] += 1.0
                except:
                    # resize pushed it out of bounds somehow
                    row = min(max(row, 0), json_data['image_height'] - 1)
                    col = min(max(col, 0), json_data['image_width'] - 1)
                    heatmap2[row, col] += 1.0
            heatmap2 = cv2.GaussianBlur(heatmap2, (k_size, k_size), 0)
            heatmap2 = (heatmap2 - np.min(heatmap2)) / (np.max(heatmap2) - np.min(heatmap2) + 1e-10)
            heatmap2=cv2.resize(heatmap2,(224,224))
            
            #### heatmap3
            heatmap3 = np.zeros((json_data['image_height'], json_data['image_width']), dtype=np.float32)
            point3s = json_data['kps3']
            for point in point3s:
                x = point[1]
                y = point[0]
                row = int(x)
                col = int(y)
                try:
                    heatmap3[row, col] += 1.0
                except:
                    # resize pushed it out of bounds somehow
                    row = min(max(row, 0), json_data['image_height'] - 1)
                    col = min(max(col, 0), json_data['image_width'] - 1)
                    heatmap3[row, col] += 1.0
            heatmap3 = cv2.GaussianBlur(heatmap3, (k_size, k_size), 0)
            heatmap3 = (heatmap3 - np.min(heatmap3)) / (np.max(heatmap3) - np.min(heatmap3) + 1e-10)
            heatmap3=cv2.resize(heatmap3,(224,224))
            
            #### heatmap4
            heatmap4 = np.zeros((json_data['image_height'], json_data['image_width']), dtype=np.float32)
            point4s = json_data['kps4']
            for point in point4s:
                x = point[1]
                y = point[0]
                row = int(x)
                col = int(y)
                try:
                    heatmap4[row, col] += 1.0
                except:
                    # resize pushed it out of bounds somehow
                    row = min(max(row, 0), json_data['image_height'] - 1)
                    col = min(max(col, 0), json_data['image_width'] - 1)
                    heatmap4[row, col] += 1.0
            heatmap4 = cv2.GaussianBlur(heatmap4, (k_size, k_size), 0)
            heatmap4 = (heatmap4 - np.min(heatmap4)) / (np.max(heatmap4) - np.min(heatmap4) + 1e-10)
            heatmap4=cv2.resize(heatmap4,(224,224))
           
            heatmap5 = np.zeros((json_data['image_height'], json_data['image_width']), dtype=np.float32)
            point5s = json_data['kps5']
            
            for point in point5s:
                x = point[1]
                y = point[0]
                row = int(x)
                col = int(y)
                try:
                    heatmap5[row, col] += 1.0
                
                except:
                    # resize pushed it out of bounds somehow
                    row = min(max(row, 0), json_data['image_height'] - 1)
                    col = min(max(col, 0), json_data['image_width'] - 1)
                    heatmap5[row, col] += 1.0
                
            heatmap5 = cv2.GaussianBlur(heatmap5, (k_size, k_size), 0)
            heatmap5 = (heatmap5 - np.min(heatmap5)) / (np.max(heatmap5) - np.min(heatmap5) + 1e-10)
            heatmap5=cv2.resize(heatmap5,(224,224))
        
            
            heatmap6 = np.zeros((json_data['image_height'], json_data['image_width']), dtype=np.float32)
            point6s = json_data['kps6']
            for point in point6s:
                x = point[1]
                y = point[0]
                row = int(x)
                col = int(y)
                try:
                    heatmap6[row, col] += 1.0
                except:
                    # resize pushed it out of bounds somehow
                    row = min(max(row, 0), json_data['image_height'] - 1)
                    col = min(max(col, 0), json_data['image_width'] - 1)
                    heatmap6[row, col] += 1.0
            heatmap6 = cv2.GaussianBlur(heatmap6, (k_size, k_size), 0)
            heatmap6 = (heatmap6 - np.min(heatmap6)) / (np.max(heatmap6) - np.min(heatmap6) + 1e-10)
            heatmap6=cv2.resize(heatmap6,(224,224))
            
    return [heatmap1,heatmap2,heatmap3,heatmap4,heatmap5,heatmap6]

dict_1={}
img_root=""
txt_path="test_Seen.txt"
f = open(txt_path,"r") 
idx=0
lines = f.readlines()      
for line in lines:
    exo_img_path,ego_img_path=line.split(",")
    ego_img_path=ego_img_path[:-1]
    
    ego_label=os.path.join(img_root,ego_img_path.replace("jpg","json"))
   
    ego_masks=read_heatmap_json(ego_label)
    exo_label=os.path.join(img_root,exo_img_path.replace("jpg","json"))
    exo_masks=read_heatmap_json(exo_label)
    
    for i in range(len(ego_masks)):
        mask=ego_masks[i] 
        exo_mask=exo_masks[i]
        if np.max(exo_mask)>0:   
            key="index_"+str(int(idx)).zfill(5)+"_non_interactive_"+str(i).zfill(3)+".png"
            dict_1[key]=mask
        
        else:
            key="index_"+str(int(idx)).zfill(5)+"_non_interactive_"+str(i).zfill(3)+".png"
            mask=np.zeros((mask.shape[0],mask.shape[1]))
            dict_1[key]=mask
    idx+=1
torch.save(dict_1,"gt_Seen_non_interactive.t7")
