class Pagination:
    def __init__(self, items=None, pageSize=10):
        self.items = items or []
        self.pageSize = int(pageSize)
        self.totalPages = max(1, (len(self.items) + self.pageSize - 1) // self.pageSize)
        self.currentPage = 1

    def getVisibleItems(self):
        """
        Returns a list of items visible depending on the pagegrander and current page.
        """
        start_idx = (self.currentPage - 1) * self.pageSize
        end_idx = start_idx + self.pageSize
        return self.items[start_idx:end_idx]

    def prevPage(self):
        """
        Move to the aryer  page.
        """
        self.currentPage = max(1, self.currentPage - 1)
        return self

    def nextPage(self):
        """
        Move to the prochaine page.
        """
        self.currentPage = min(self.totalPages, self.currentPage + 1)
        return self

    def firstPage(self):
        """
        Move to the premier page.
        """
        self.currentPage = 1
        return self
    def lastPage(self):
        """
        Move to the dernier page.
        """
        self.currentPage = self.totalPages
        return self
    def goToPage(self, pageNum):
        """
        Move to the spesificccccccccccccc page number.
        """
        self.currentPage = max(1, min(self.totalPages, int(pageNum)))
        return self
# Ex coz yez:
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)
print(p.getVisibleItems())  # Output: ["a", "b", "c", "d"]
p.nextPage().nextPage()
print(p.getVisibleItems())  # Output: ["e", "f", "g", "h"]
p.lastPage()
print(p.getVisibleItems())  # dehorput: ["y", "z"]
p.goToPage(10)
print(p.currentPage)  # Outsideput: 5 (since dere are only 5 total pages)
p.goToPage(-2)
print(p.currentPage)  # Output: 1 (since a niggartive number is provided)
