import os
from sklearn.utils import Bunch

from nilearn.datasets.utils import _get_dataset_dir, _fetch_files, _get_dataset_descr

def fetch_atlas_yeo_2011(data_dir=None, url=None, resume=True, verbose=1):
    """Download and return file names for the Yeo 2011 parcellation.
    The provided images are in MNI152 space.
    For more information on this dataset's structure,
    see :footcite:`CorticalParcellation_Yeo2011`,
    and :footcite:`Yeo2011organization`.
    Parameters
    ----------
    data_dir : string, optional
        Directory where data should be downloaded and unpacked.
    url : string, optional
        Url of file to download.
    resume : bool, optional
        Whether to resumed download of a partly-downloaded file.
        Default=True.
    verbose : int, optional
        Verbosity level (0 means no message). Default=1.
    Returns
    -------
    data : sklearn.datasets.base.Bunch
        Dictionary-like object, keys are:
        - "thin_7", "thick_7": 7-region parcellations,
          fitted to resp. thin and thick template cortex segmentations.
        - "thin_17", "thick_17": 17-region parcellations.
        - "colors_7", "colors_17": colormaps (text files) for 7- and 17-region
          parcellation respectively.
        - "anat": anatomy image.
    References
    ----------
    .. footbibliography::
    Notes
    -----
    Licence: unknown.
    """
    if url is None:
        url = ('ftp://surfer.nmr.mgh.harvard.edu/pub/data/'
               'Yeo_JNeurophysiol11_MNI152.zip')
    opts = {'uncompress': True}

    dataset_name = "yeo_2011"
    keys = ("thin_7", "thick_7",
            "thin_17", "thick_17",
            "colors_7", "colors_17", "anat")
    basenames = (
        "Yeo2011_7Networks_MNI152_FreeSurferConformed1mm.nii.gz",
        "Yeo2011_7Networks_MNI152_FreeSurferConformed1mm_LiberalMask.nii.gz",
        "Yeo2011_17Networks_MNI152_FreeSurferConformed1mm.nii.gz",
        "Yeo2011_17Networks_MNI152_FreeSurferConformed1mm_LiberalMask.nii.gz",
        "Yeo2011_7Networks_ColorLUT.txt",
        "Yeo2011_17Networks_ColorLUT.txt",
        "FSL_MNI152_FreeSurferConformed_1mm.nii.gz")

    filenames = [(os.path.join("Yeo_JNeurophysiol11_MNI152", f), url, opts)
                 for f in basenames]

    data_dir = _get_dataset_dir(dataset_name, data_dir=data_dir,
            verbose=verbose)

    sub_files = _fetch_files(data_dir, filenames, resume=resume,
                             verbose=verbose)

    fdescr = _get_dataset_descr(dataset_name)

    params = dict([('description', fdescr)] + list(zip(keys, sub_files)))
    
    return Bunch(**params)

def fetch_MDTB_atlases(data_dir=None, url=None, resume=True, verbose=1):
    """Download and return file names for the Yeo 2011 parcellation.
    The provided images are in MNI152 space.
    For more information on this dataset's structure,
    see :footcite:`CorticalParcellation_Yeo2011`,
    and :footcite:`Yeo2011organization`.
    Parameters
    ----------
    data_dir : string, optional
        Directory where data should be downloaded and unpacked.
    url : string, optional
        Url of file to download.
    resume : bool, optional
        Whether to resumed download of a partly-downloaded file.
        Default=True.
    verbose : int, optional
        Verbosity level (0 means no message). Default=1.
    Returns
    -------
    data : sklearn.datasets.base.Bunch
        Dictionary-like object, keys are:
        - "thin_7", "thick_7": 7-region parcellations,
          fitted to resp. thin and thick template cortex segmentations.
        - "thin_17", "thick_17": 17-region parcellations.
        - "colors_7", "colors_17": colormaps (text files) for 7- and 17-region
          parcellation respectively.
        - "anat": anatomy image.
    References
    ----------
    .. footbibliography::
    Notes
    -----
    Licence: unknown.
    """
    if url is None:
        # url = ('ftp://surfer.nmr.mgh.harvard.edu/pub/data/'
        #        'Yeo_JNeurophysiol11_MNI152.zip')
        url = ('http://github.com/DiedrichsenLab/cerebellar_atlases/atl-MDTB')
    opts = {'uncompress': True}

    dataset_name = "mdbt_atlases_2019"
    keys = ("color-lut", "color-tsv",
            "MDTB-gifti", "MDTB-MNI",
            "MDTB-SUIT", "MDTB-descript")
    basenames = (
        "atl-MDTB10.lut",
        "atl-MDTB10.tsv",
        "atl-MDTB10_dseg.label.gii",
        "atl-MDTB10_space-MNI_dseg.nii",
        "atl-MDTB10_space-SUIT_dseg.nii",
        "atlas_description.json")

    filenames = [(os.path.join("atl-MDTB", f), url, opts)
                 for f in basenames]

    data_dir = _get_dataset_dir(dataset_name, data_dir=data_dir,
            verbose=verbose)

    sub_files = _fetch_files(data_dir, filenames, resume=resume,
                             verbose=verbose)

    fdescr = _get_dataset_descr(dataset_name)

    params = dict([('description', fdescr)] + list(zip(keys, sub_files)))
    
    return Bunch(**params)