import os

PATH = "/eos/project/d/da-and-diffusion-studies/DA_Studies/Simulations/Models/dynamic_indicator_analysis/big_data/figs"

def check_file_path(path: str) -> str:
    # check if the file exists
    # if not, raise a ValueError
    if not os.path.exists(path):
        raise ValueError(f"File {path} does not exist")
    return path

def path_gatherer(
    omegas: str,
    epsilon: str,
    mu: str,
    plot_kind: str,
    dynamic_indicator: str,
    zoom=None,
    kernel=None,
) -> str:
    subpath = f"{omegas}/{epsilon}_{mu}" if kernel == "none" else f"{omegas}/{epsilon}_{mu}/{kernel}"
    print(subpath)
    
    if plot_kind == "performance":
        out_path = os.path.join(PATH, subpath, f"performance_{dynamic_indicator}_z_{zoom}.jpg")

    elif plot_kind == "histogram":
        out_path = os.path.join(PATH, subpath, f"histogram_{dynamic_indicator}.jpg")

    else:# plot_kind == "colormap":
        out_path = os.path.join(PATH, subpath, "colormap/stable_colormaps.jpg")

    return check_file_path(out_path)
