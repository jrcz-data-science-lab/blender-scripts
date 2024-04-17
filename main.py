"""Read the collections of a blender file"""

import json
import sys
import bpy


def traverse_tree(current, *parent_obj):
    """Get object and the parent of the object"""
    yield current, parent_obj
    for child in current.children:
        yield from traverse_tree(child, *parent_obj, current.name)


def find_collection_info(scene_coll):
    coll_list = {}
    for c, parents in traverse_tree(scene_coll):
        coll_list[c.name] = {
            "current_parent": list(parents)[-1] if len(list(parents)) > 0 else None,
            "parents": list(parents),
            "inner_meshes": [obj.name for obj in c.objects if obj.type == "MESH"],
            "inner_collections": [obj.name for obj in c.children],
        }
    return coll_list


def get_parent_collections_of_mesh(coll_list: dict):
    meshes_for_tags = {}
    for collection, values in coll_list.items():
        parents = values.get("parents", [])
        parents.append(collection)
        for mesh in values.get("inner_meshes", []):
            meshes_for_tags[mesh] = parents
    return meshes_for_tags


if __name__ == "__main__":
    bpy.ops.wm.open_mainfile(filepath=sys.argv[1])
    scene_coll = bpy.context.scene.collection

    coll_list = find_collection_info(scene_coll)

    with open("blender_collections.json", "w", encoding="utf-8") as outfile:
        json.dump(coll_list, outfile)

    meshes_for_tags = get_parent_collections_of_mesh(coll_list)

    with open("meshes_for_tags.json", "w", encoding="utf-8") as outfile:
        json.dump(meshes_for_tags, outfile)
