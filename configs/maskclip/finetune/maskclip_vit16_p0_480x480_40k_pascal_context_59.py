_base_ = './maskclip_vit16_480x480_40k_pascal_context_59.py'
model = dict(
    backbone=dict(
        freeze_xsfm=True,
        freeze_cls=True,
        freeze_pos=True,
        num_prompt=0,
    )
)