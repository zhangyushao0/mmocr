_base_ = [
    "_base_svtr-tiny.py",
    "../_base_/default_runtime.py",
    "../_base_/datasets/mjsynth_lmdb.py",
    "../_base_/datasets/synthtext_lmdb.py",
    "../_base_/datasets/cute80.py",
    "../_base_/datasets/iiit5k.py",
    "../_base_/datasets/svt.py",
    "../_base_/datasets/svtp.py",
    "../_base_/datasets/icdar2013.py",
    "../_base_/datasets/icdar2015.py",
    "../_base_/schedules/schedule_adam_base.py",
]

train_cfg = dict(type="EpochBasedTrainLoop", max_epochs=20, val_interval=1)

optim_wrapper = dict(
    type="OptimWrapper",
    optimizer=dict(
        type="AdamW",
        lr=5 / (10**4) * 2048 / 2048,
        betas=(0.9, 0.99),
        eps=8e-8,
        weight_decay=0.05,
    ),
)

param_scheduler = [
    dict(
        type="LinearLR",
        start_factor=0.5,
        end_factor=1.0,
        end=2,
        verbose=False,
        convert_to_iter_based=True,
    ),
    dict(
        type="CosineAnnealingLR",
        T_max=19,
        begin=2,
        end=20,
        verbose=False,
        convert_to_iter_based=True,
    ),
]

# dataset settings
train_list = [
    _base_.mjsynth_lmdb_textrecog_train,
    _base_.synthtext_lmdb_textrecog_train,
]
test_list = [
    _base_.cute80_textrecog_test,
    _base_.iiit5k_textrecog_test,
    _base_.svt_textrecog_test,
    _base_.svtp_textrecog_test,
    _base_.icdar2013_textrecog_test,
    _base_.icdar2015_textrecog_test,
]

val_evaluator = dict(
    dataset_prefixes=["CUTE80", "IIIT5K", "SVT", "SVTP", "IC13", "IC15"]
)
test_evaluator = val_evaluator

train_dataloader = dict(
    batch_size=128,
    num_workers=6,
    persistent_workers=True,
    pin_memory=True,
    sampler=dict(type="DefaultSampler", shuffle=True),
    dataset=dict(
        type="ConcatDataset", datasets=train_list, pipeline=_base_.train_pipeline
    ),
)

val_dataloader = dict(
    batch_size=128,
    num_workers=8,
    persistent_workers=True,
    pin_memory=True,
    drop_last=False,
    sampler=dict(type="DefaultSampler", shuffle=False),
    dataset=dict(
        type="ConcatDataset", datasets=test_list, pipeline=_base_.test_pipeline
    ),
)

test_dataloader = val_dataloader
