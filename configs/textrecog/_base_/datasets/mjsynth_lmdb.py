mjsynth_lmdb_textrecog_data_root = 'data/mjsynth'

mjsynth_lmdb_textrecog_train = dict(
    type='RecogLMDBDataset',
    data_root=mjsynth_lmdb_textrecog_data_root,
    ann_file='textrecog_train.lmdb',
    pipeline=None)

mjsynth_lmdb_sub_textrecog_train = dict(
    type='RecogLMDBDataset',
    data_root=mjsynth_lmdb_textrecog_data_root,
    ann_file='subset_textrecog_train.lmdb',
    pipeline=None)
