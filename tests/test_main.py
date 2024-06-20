"""Tests the methods from the command line"""

import os
import bpy

from main import find_collection_info, get_parent_collections_of_mesh

TEST_FILE = "tests/test_file.blend1"


def test_opening_file():
    """Tests if a file can be opened"""
    assert os.path.exists(TEST_FILE)
    bpy.ops.wm.open_mainfile(filepath=TEST_FILE)
    assert bpy.data.filepath == os.path.realpath(TEST_FILE)


def test_find_collection_info():
    """Test if all the collections can be gathered with their info"""
    bpy.ops.wm.open_mainfile(filepath=TEST_FILE)
    scene_coll = bpy.context.scene.collection

    coll_list = find_collection_info(scene_coll)
    # shows all elements
    assert list(coll_list.keys()) == [
        "Scene Collection",
        "Collection",
        "normal",
        "remove",
        "mball",
        "seperate bake",
    ]
    # has expected information
    assert list(coll_list.get("Scene Collection", {}).keys()) == [
        "current_parent",
        "parents",
        "inner_meshes",
        "inner_collections",
    ]
    # has inner collections in parent
    assert coll_list.get("Scene Collection", {}).get("inner_collections", []) == [
        "Collection",
        "normal",
        "remove",
        "mball",
        "seperate bake",
    ]
    # shows parent in current_parent
    assert (
        coll_list.get("Collection", {}).get("current_parent", "") == "Scene Collection"
    )
    assert coll_list.get("Collection", {}).get("parents", []) == ["Scene Collection"]
    # shows inner meshes
    assert coll_list.get("normal", {}).get("inner_meshes", []) == ["Cube"]


def test_get_parent_collections_of_mesh():
    """Test if the parent path can be returned on a mesh"""
    bpy.ops.wm.open_mainfile(filepath=TEST_FILE)
    scene_coll = bpy.context.scene.collection
    coll_list = find_collection_info(scene_coll)
    meshes_for_tags = get_parent_collections_of_mesh(coll_list, True)
    # shows all elements
    assert list(meshes_for_tags.keys()) == [
        "Cube",
        "Cube.001",
        "Cube.002",
        "Cube.003",
    ]
    # has path to parent
    assert meshes_for_tags.get("Cube", "") == "Scene Collection/normal"
