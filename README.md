# Brain Enhancing Region Radiological analYsis ![logo](doc/img/berry0_128.png)

The BERRY app uses a pretrained CNN classifier scheme for voxel-wise classification of enhancing brain tumours into P-CNS-lymphoma, glioblastoma or brain metastasis, from dynamic susceptibility contrast (DSC) MRI data.

![Probability maps](doc/img/probmaps.png)

This is the code repository of the BERRY tumour classification pipeline described in the work *An accessible deep learning tool for voxel-wise classification of brain malignancies from perfusion MRI* by Raquel Perez-Lopez and colleagues from the Vall d'Hebron Institute of Oncology (VHIO), Barcelona, Spain. Manuscript currently under review.


BERRY will be freely accessible online soon at:  [berry-app.vhio.org](https://berry-app.vhio.org/)


[Visit us here!](https://radiomicsgroup.github.io/)

## Requirements
### Python
- Python 3.8
- Python packages listed in `requirements.txt`
- Optionally, to handle compressed DICOMs: pydicom (2.1.2 tested), gdcm (2.8.9 tested)

### External
#### 3D Slicer 4.8.1

- [windows](https://slicer-packages.kitware.com/api/v1/file/60add7aeae4540bf6a89c0eb/download)

- [mac](https://slicer-packages.kitware.com/api/v1/file/60add78bae4540bf6a89c0c4/download)

- [linux](https://slicer-packages.kitware.com/api/v1/file/60add79eae4540bf6a89c0d6/download)

#### dcm2niix

- [dcm2niix](https://github.com/rordenlab/dcm2niix)

### NOTE
- If used without graphical interface in Linux systems, xvfb-run is needed (`apt-get install xvfb-run`)

## Installation
Download or clone the app repo in a directory, e.g., /berry

Though not necessary, you may create a new python/conda environment:

`conda create --name berryapp python=3.8`

`conda activate berryapp`

Install python packages:

`pip install -r /berry/requirements.txt`

Optionally:

`pip install pydicom==2.1.2`

`pip install gdcm==2.8.9`

Download Slicer from above links into, e.g. /slicer

Download dcm2niix from above links into, e.g. /dcm2niix

In `settings.py`, place the path of the Slicer executable as: `SLICER_EXEC="/slicer/Slicer"`

In `settings.py`, place the path of the dcm2niix executable as: `DCM2NIIX="/dcm2niix/dcm2niix"`

## Usage
To run the pipeline, call the `run.py` file as such:
`python /berry/run.py --p_dsc /path_to_DSC_image --p_t1 /path_to_T1_image --p_output /desired_output_path`

Input DSC and T1wCE volumes may be in DICOM, Nifti or NRRD formats.
Segmentation mask files can be provided instead of the T1 volume.

See all the options in the docstring help of `run.py`.

## Referencing
- Github: [github.com/radiomicsvhio/berry-app](https://github.com/radiomicsvhio/berry-app)
- Raquel Perez-Lopez et al., *An accessible deep learning tool for voxel-wise classification of brain malignancies from perfusion MRI* (article under review)

## License
Please, see `license.txt`

## Terms of use
1.	The use of any software provided by VHIO as part of its services is subject to the terms and conditions of the third party license agreements applicable to the relevant software as made available through the website [https://github.com/radiomicsvhio/berry-app].
2.	The BERRY services shall be used solely for research activities that comply with all applicable laws and regulations.
3.	Users shall keep all user IDs, passwords and other means of access to the BERRY account within its possession or control and shall keep those confidential and secure from unauthorised access or use.
4.	If user becomes aware of any unauthorized use of a password or the BERRY account, user will notify the BERRY team as promptly as possible through the provided channels.
5.	User will not use the BERRY services to identify the individuals who are data subjects.
6.	Do NOT use any of the services if the safety of data subjects depends directly on the uninterrupted, and error free availability of the services at all times, or the compatibility or operation of the services with all hardware and software configurations.
7.	Within the context of a study, the principal investigator is responsible for:
    - Verification of the identity of users and delegates;
    - Order assignment and withdrawal of access authorizations for users and delegates;
    - Informing users and delegates about the responsible handling of study data.
8.	Within the context of a study, users may only use BERRY services as per instructions of the study’s principal investigator, specifically:
    - Data upload and download to and from BERRY app shall only be executed in accordance with the study conditions and with the consent of the principal investigator.
