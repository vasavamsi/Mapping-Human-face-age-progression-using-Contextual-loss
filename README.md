# Mapping Human face age progression using Contextual-loss
This work is completed as a part of Master's Thesis at IIT Gandhinagar

## Abstract
Age progression is a process of projection of futuristic aging characteristics onto the subject face image. This kind of task finds applications in cyber-cell forensics, age-invariant facial recognition, and in entertainment sectors up to a certain extent. Most of the previous works tried projecting similar kinds of texture-based artifacts such as artificial wrinkles and dullness of eyes on the test subjects. Even, the analysis to convince the aging effects, as well as identity preservation in the generated images, is not studied in a detailed manner. In this work, we for the first time used the Attention mechanism in combination with weighted contextual loss to accomplish age progression of the human face. We used Attention UNet Generator architecture with the pyramid architecture of discriminator to aid the realness of the generated images. We have also shown the ablation studies for generators with different blocks in encoder and decoder. By using weighted Contextual loss, we induced the aging artifacts onto the test subject without losing the original identity. We have shown how perceptually close the results are to the real images. Performance evaluation of our work is carried out with the help of external age estimation and identity matching agents for better convincing and reliable quantitative analysis. Our method is robust to occlusion and some regular positions of the faces. This work is done under the guidance and collaboration of the premier R&D organization Center for Development of Advanced Computing (C-DAC), Hyderabad. 

Graphical representation of the generator and discriminator architecture.

![Generator architecture](https://github.com/vasavamsi/Mapping-Human-face-age-progression-using-Contextual-loss/assets/58003228/9ddf11f8-653d-4c99-94a4-f4393bac4c86)

![discriminator](https://github.com/vasavamsi/Mapping-Human-face-age-progression-using-Contextual-loss/assets/58003228/6c56451f-3ce8-4d34-8250-a7e9bfb936ba)

## Needed installations

● Pytorch 1.0
● Python 3.6
● Visdom 0.1.8
● Pillow 6.0
● Contextual loss module (https://github.com/S-aiueo32/contextual_loss_pytorch)

## Dataset
CACD dataset - https://bcsiriuschen.github.io/CARC/
UTK face dataset - https://susanqq.github.io/UTKFace/

## Training the model

Images in the dataset corresponding to | Path to be moved to
--- | ---
Age 20-29 | training_data/elder2/2
Age 30-39 | training_data/elder3/3
Age 40-49 | training_data/elder4/4
Age 50-59 | training_data/elder5/5
Age 60-69 | training_data/elder6/6
Age 70+ | training_data/elder7/7

Change the defaults arguments in the parameters section of the “train.py” in the repo (scroll to the last
part of the code.

❖ Learning parameters can be set as per required.

❖ Provide the paths to young training data, testing data and validating data which are by default as
follows:

Path for | parameter in code | Default set
--- | --- | ---
Young images for Training | young_dataroot | './training_data/elder2/'
Young images for Testing | test_dataroot | './testing_data/elder2/'
Young images for Validating | val_dataroot | './val_data/elder2/'

❖ Provide the path to the older age dataset to training on the aging features from that data and also
change the train_age parameter to the respective training age. By default the set age is 3 (i.e
within the age span of 30-39). The path provided in elder_dataroot is './training_data/elder3/3/'.

❖ Provide the path for the trained checkpoints for generator and discriminator to be saved after
certain pre-defined (100 by default) epochs. The parameter used is model_dir and the default path
provided is '.training_saves/checkpoints/'.

❖ Provide a path to save the inferred results for the saved checkpoints. The parameter used is
train_img_dir and the default path provided is './training_saves/training_imgs/'.

❖ For training, the boolean parameter is_training should be set “True”.

❖ If the training is to be resumed from a certain epoch the learning parameters should be changed
accordingly and the paths to the trained generator and discriminator architecture are to be
provided as inputs to the parameters "netG_pth" and "netD_pth".

## For Inferring (testing) the model:

❖ The pre-trained weights are already stored in the folder pre-trained_checkpoints. To test on any
other data (young faces) simply move the data to be tested to “./testing_data/elder2/2”. After the
inference is done the images will be stored at the path provided as test_img_dir which is set as
'./results/' by default.

❖ The pre-trained weights for the different age clusters are saved after 50,000 epochs. The
checkpoints trained for each age cluster on CACD dataset are stored in the sub-folder named the same.

❖ The default generator checkpoints path provided in netG_pth is './pre-trained_checkpoints/3/netG_epoch_49900.pth'.

❖ For testing/inferring purposes set is_training parameter to ‘False’.

## Results obtained

Here we have shown the results obtained on UTK and CACD face datasets.

![common_catalogue](https://github.com/vasavamsi/Mapping-Human-face-age-progression-using-Contextual-loss/assets/58003228/3a7ee31e-3d4b-4c0f-aa45-2ca9044cfd1a)

Outputs on occluded images (such as hat, spects etc.) shown below.

![occlusion_pose](https://github.com/vasavamsi/Mapping-Human-face-age-progression-using-Contextual-loss/assets/58003228/5fb8cb61-f919-4d66-9d19-5a2280563164)

Highlights of our work- The formation of wrinkles on the cheeks, Beard whitening, Hair transformation, Eyeline transformation, Intact Lip expressions.

![facial_details](https://github.com/vasavamsi/Mapping-Human-face-age-progression-using-Contextual-loss/assets/58003228/75f5e5fc-2e41-42aa-8cb1-fb62019347a5)

Age estimation results using pre-trained VGG16 age estimation model

  | Dataset | age-3 | age-4 | age-5 | age-6 | age-7
--- | --- | --- | --- | --- | --- | ---
Synthesized | CACD Dataset | 30.3988 ± 6.1177 | 39.6783 ± 0.5499 | 52.1785 ± 12.3002 | 56.4529 ± 13.8786 | 77.4484 ± 4.3017
  | UTKFace | 29.5927 ± 5.3880 | 40.2513 ± 10.5704 | 51.5 ± 12.6375 | 55.5082 ± 13.7190 | 78.2325 ± 4.4575
Real  |CACD Dataset | 29.9234 ± 4.7330 | 38.2818 ± 7.3171 | 46.9073 ± 8.7357 | 56.0291 ± 10.3238 | 71.9371 ± 12.1049
  | UTKFace | 29.037 ± 4.2668 | 36.3529 ± 7.0510 | 45.5284 ± 8.6302 | 54.2988 ± 10.5100 | 70.3005 ± 12.959
