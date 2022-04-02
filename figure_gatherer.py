import os

PATH = "/eos/user/c/camontan/definitive_dyn_indicators/figs"

def check_file_path(path: str) -> str:
    # check if the file exists
    # if not, raise a ValueError
    print(path)
    if not os.path.exists(path):
        print("File does not exist")
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
        out_path = os.path.join(PATH, subpath, f"{dynamic_indicator}_histogram.jpg")

    else:# plot_kind == "colormap":
        out_path = os.path.join(PATH, subpath, "colormap/stable_colormaps.jpg")

    return check_file_path(out_path)
