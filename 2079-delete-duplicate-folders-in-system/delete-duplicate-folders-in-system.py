class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        trie_paths = {}
        for path in paths:
            curr = trie_paths
            for folder in path:
                if folder not in curr:
                    curr[folder] = {}
                curr = curr[folder]

        serials = self.createSerializations(trie_paths)

        serial_to_paths = defaultdict(list)
        for path, serial in serials.items():
            serial_to_paths[serial].append(path)

        nodes_to_delete = set()
        for paths_with_same_serial in serial_to_paths.values():
            if len(paths_with_same_serial) > 1:
                nodes_to_delete.update(paths_with_same_serial)

        result = []
        for path in paths:
            should_delete = False
            for i in range(1, len(path) + 1):
                if tuple(path[:i]) in nodes_to_delete:
                    should_delete = True
                    break
            if not should_delete:
                result.append(path)
        return result
    def createSerializations(self, node: dict) -> List[str]:
        serializations = {}

        def dfs(curr: dict, path: List[str]) -> str:
            if not curr:
                return ""
            serial = ""
            for node in sorted(curr.keys()):
                serial += node + "(" + dfs(curr[node], path + [node]) + ")"
            serializations[tuple(path)] = serial
            return serial

            
        dfs(node, [])
        return serializations