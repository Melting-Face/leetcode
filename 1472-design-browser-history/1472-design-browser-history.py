class BrowserHistory:
    def __init__(self, homepage: str):
        self.index = 0
        self.sites = [homepage]

    def visit(self, url: str) -> None:
        self.index += 1
        self.sites = self.sites[: self.index] + [url]

    def back(self, steps: int) -> str:
        self.index -= steps
        if self.index < 0:
            self.index = 0
        return self.sites[self.index]

    def forward(self, steps: int) -> str:
        index = self.index
        self.index += steps
        if self.index >= len(self.sites):
            self.index = len(self.sites) - 1

        return self.sites[self.index]