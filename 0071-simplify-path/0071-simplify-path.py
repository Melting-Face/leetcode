class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = []
        items = [text for text in path.split('/') if text and text != '.']
        for item in items:
            if item == '..':
                if arr:
                    arr.pop()
            else:
                arr.append(item)

        return f'/{"/".join(arr)}'