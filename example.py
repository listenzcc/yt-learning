"""
File: example.py
Author: Chuncheng Zhang
Date: 2024-02-15
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    Amazing things

Functions:
    1. Requirements and constants
    2. Function and class
    3. Play ground
    4. Pending
    5. Pending
"""

# %% ---- 2024-02-15 ------------------------
# Requirements and constants
import yt
import numpy as np
import nibabel as nib

import matplotlib.pyplot as plt

from rich import print, inspect


# %% ---- 2024-02-15 ------------------------
# Function and class


def draw_example():
    ds = yt.load("e:\\datastation\\Enzo_64\\DD0043\\data0043")
    print(f"Loaded ds: {ds} | {type(ds)}, dir(ds): {dir(ds)}")

    def draw(ds, profile_field=("gas", "density")):
        sc = yt.create_scene(ds, profile_field, lens_type="perspective")

        # Get a reference to the VolumeSource associated with this scene
        # It is the first source associated with the scene, so we can refer to it
        # using index 0.
        source = sc[0]

        # Set the bounds of the transfer function
        source.tfh.set_bounds((3e-31, 5e-27))

        # set that the transfer function should be evaluated in log space
        source.tfh.set_log(True)

        # Make underdense regions appear opaque
        source.tfh.grey_opacity = True

        # Plot the transfer function, along with the CDF of the density field to
        # see how the transfer function corresponds to structure in the CDF
        source.tfh.plot("transfer_function.png", profile_field=profile_field)

        # save the image, flooring especially bright pixels for better contrast
        sc.save("rendering.png", sigma_clip=6.0)

    draw(ds, profile_field=("gas", "density"))

    return ds


# ds_example = draw_example()

print(f"dir(yt): {dir(yt)}")

# %%
nii_img = nib.load("ExBox17/T1.nii.gz")
nii_data = nii_img.get_fdata()
print(f"Loaded nii_data: {nii_data.shape}")

plt.imshow(nii_data[100])

# %%
# n = 128 // 2
# pos = [np.random.random((n, n, n)) for i in range(3)]
# dens = np.random.random((n, n, n))
dens = nii_data
data = dict(
    # particle_position_x=pos[0],
    # particle_position_y=pos[1],
    # particle_position_z=pos[2],
    Density=dens,
)
bbox = np.array([[0.0, 1.0], [0.0, 1.0], [0.0, 1.0]])
ds = yt.load_uniform_grid(data, dens.shape, 3.08e24, bbox=bbox)
print(f"Derived ds: {ds}, field_list: {ds.field_list}")

# %%
field = ds.field_list[0]  # ("stream", "Density")
im, sc = yt.volume_render(ds, field)
# yt.SlicePlot(ds, "x", field)
print(f"Generated sc: {sc}, {dir(sc)}")

# %%
yt.toggle_interactivity()
sc.show()

# %% ---- 2024-02-15 ------------------------
# Play ground

# %%

# %%

# %% ---- 2024-02-15 ------------------------
# Pending

# %% ---- 2024-02-15 ------------------------
# Pending

# %%
