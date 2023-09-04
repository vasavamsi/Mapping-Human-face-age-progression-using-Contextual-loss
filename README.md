# Mapping Human face age progression using Contextual-loss
This work is completed as a part of Master's Thesis at IIT Gandhinagar

## Abstract
Age progression is a process of projection of futuristic aging characteristics onto the subject face image. This kind of task finds applications in cyber-cell forensics, age-invariant facial recognition, and in entertainment sectors up to a certain extent. Most of the previous works tried projecting similar kinds of texture-based artifacts such as artificial wrinkles and dullness of eyes on the test subjects. Even, the analysis to convince the aging effects, as well as identity preservation in the generated images, is not studied in a detailed manner. In this work, we for the first time used the Attention mechanism in combination with weighted contextual loss to accomplish age progression of the human face. We used Attention UNet Generator architecture with the pyramid architecture of discriminator to aid the realness of the generated images. We have also shown the ablation studies for generators with different blocks in encoder and decoder. By using weighted Contextual loss, we induced the aging artifacts onto the test subject without losing the original identity. We have shown how perceptually close the results are to the real images. Performance evaluation of our work is carried out with the help of external age estimation and identity matching agents for better convincing and reliable quantitative analysis. Our method is robust to occlusion and some regular positions of the faces. This work is done under the guidance and collaboration of the premier R&D organization Center for Development of Advanced Computing (C-DAC), Hyderabad. 

## Needed installations

● Pytorch 1.0
● Python 3.6
● Visdom 0.1.8
● Pillow 6.0
● Contextual loss module (https://github.com/S-aiueo32/contextual_loss_pytorch)

## Training the model

Images in the dataset corresponding to | Path to be moved to
Age 20-29 | training_data/elder2/2
Age 30-39 | training_data/elder3/3
Age 40-49 | training_data/elder4/4
Age 50-59 | training_data/elder5/5
Age 60-69 | training_data/elder6/6
Age 70+ | training_data/elder7/7
