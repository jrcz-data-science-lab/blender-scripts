# Read-blender
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
  "Artery": "Scene Collection/Heart/Vessels",
}
```
