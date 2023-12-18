import os, shutil


def dfs_showdir(path, depth, target="depth"):
    if depth == 0:
        print(f"root:[{path}]")

    for item in os.listdir(path):
        if '.git' not in item:
            # print("| " * depth + "+--" + item)

            newitem = path + '/' + item
            if os.path.isdir(newitem):
                if item == target:
                    shutil.rmtree(newitem)
                    print(f"{newitem}已被删除")
                else:
                    dfs_showdir(newitem, depth + 1)


if __name__ == '__main__':
    path = "part_A"
    assert os.path.exists(path), f"{path}不存在"
    dfs_showdir(path, 0)
