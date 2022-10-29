import pandas as pd
from lxml import etree
import datetime
import sys


def add_rows(rows, head_id, tree, path, pem_map):
    time = tree.xpath("//INodeSection/inode[id/text() = " + head_id + "]/mtime/text()")[0]
    time = datetime.datetime.fromtimestamp(int(time) / 1000).strftime("%#m/%#d/%Y %H:%M")
    blocks = len(tree.xpath("//INodeSection/inode[id/text() = " + head_id + "]/blocks"))
    size = tree.xpath("//INodeSection/inode[id/text() = " + head_id + "]/blocks/block/numBytes/text()")
    if len(size) == 0:
        size = 0
    else:
        size = tree.xpath("//INodeSection/inode[id/text() = " + head_id + "]/blocks/block/numBytes/text()")[0]
    permission = tree.xpath("//INodeSection/inode[id/text() = " + head_id + "]/permission/text()")[0]
    pem = ""
    if size == 0:
        pem += "d"
    else:
        pem += "-"
    permission = permission[-3:]
    for num in permission:
        pem += pem_map[num]
    rows.append({"Path": path,
                 "ModificationTime": time,
                 "BlocksCount": blocks,
                 "FileSize": size,
                 "Permission": pem})


def main():
    pem_map = {'0': '---', '1': '--x', '2': '-w-', '3': '-wx', '4': 'r--', '5': 'r-x', '6': 'rw-', '7': 'rwx'}
    cols = ["Path", "ModificationTime", "BlocksCount", "FileSize", "Permission"]
    rows = []
    f = open(sys.argv[1])
    tree = etree.parse(f)
    root_id = tree.xpath("//INodeSection/inode[name[not(node())]]/id/text()")[0]
    path = "/"
    add_rows(rows, root_id, tree, path, pem_map)
    q = [root_id]
    q2 = [""]
    while len(q) != 0:
        for i in range(0, len(q)):
            head = q.pop(0)
            head_path = q2.pop(0)
            if len(tree.xpath("//INodeDirectorySection/directory[parent/text() = " + head + "]")) == 0:
                continue
            directory = tree.xpath("//INodeDirectorySection/directory[parent/text() = " + head + "]")[0]
            for child in directory.xpath(
                    "//INodeDirectorySection/directory[parent/text() = " + head + "]/child/text()"):
                path = head_path + "/" + tree.xpath("//INodeSection/inode[id/text() = " + child + "]/name/text()")[0]
                add_rows(rows, child, tree, path, pem_map)
                q.append(child)
                q2.append(path)
    df = pd.DataFrame(rows, columns=cols)
    df.to_csv(sys.argv[2], index=False, sep="\t")


if __name__ == '__main__':
    main()
