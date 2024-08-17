class Solution:
    def simplifyPath(self, path: str) -> str:
        directory = []
        path = path.split("/")

        for elem in path:
            if directory and elem == "..":
                directory.pop()
            elif elem not in (".", "", ".."):
                directory.append(elem)
            
        return "/" + "/".join(directory)