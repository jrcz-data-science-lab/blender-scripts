# Read-blender [![Running tests](https://github.com/jrcz-data-science-lab/blender-scripts/actions/workflows/python-app.yml/badge.svg)](https://github.com/jrcz-data-science-lab/blender-scripts/actions/workflows/python-app.yml)

This tool can be used to print blender collection information in JSON format

Example of the resulting blender_collections.json:

```json
{
  "Scene Collection": {
    "current_parent": null,
    "parents": [],
    "inner_meshes": [],
    "inner_collections": [
      "Heart",
      ...
    ]
  },
}
```

Example of the resulting meshes_for_tags.json:

```json
{
  "Artery": "Scene Collection/Heart/Vessels"
}
```

## Using the tool

Packages within this project are managed via [Poetry](https://python-poetry.org) or [PDM](https://pdm-project.org/en/latest/).
Install the needed packages with `pdm install` or `poetry install`.
After that you can run the project with `pdm run main.py "path/to/blender/file.blend"` or `poetry run python3 main.py "path/to/blender/file.blend"`.

## Running via Docker

You can also run the tool via Docker instead:

```sh
docker build --tag read-blender . # build the Docker container and naming it read-blender
docker run --rm -it --mount type=bind,source="${PWD}",target=/app read-blender bash # running a interactive shell with the necessary dependencies
python3 main.py "path/to/blender/file.blend" # run the tool
```

### Mac OS M1 fix:

The bpy package was build Mac OS 11.2 and newer, for some reason python doesn't detect Mac OS 14.4 as a newer platform for macosx arm.
To fix this, download "https://files.pythonhosted.org/packages/43/99/8c71bb21b62c5a6c22d166f24d0b47b53f0850959f60731df7cc76c52177/bpy-4.1.0-cp311-cp311-macosx_11_2_arm64.whl".
Rename the downloaded file to "bpy-4.1.0-cp311-cp311-macosx_14_4_arm64.whl", Where 14.4 is the current Mac OS version and add it to the whl_files folder.
And uncomment the following line within the "pyproject.toml" file:

```toml
# { platform = "darwin", markers = "platform_machine == 'x86_64'", file = "whl_files/bpy-4.1.0-cp311-cp311-macosx_14_4_arm64.whl" }, # mac os support fix
```
