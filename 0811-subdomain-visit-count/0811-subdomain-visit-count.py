class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        word_map = {}
        for cpdomain in cpdomains:
            count, domain = cpdomain.split(" ")
            count = int(count)
            words = domain.split(".")
            for idx in range(len(words)):
                subdomain = ".".join(words[idx::])
                if subdomain not in word_map:
                    word_map.setdefault(subdomain, count)
                    continue

                word_map[subdomain] += count
        output = [f"{count} {subdomain}" for subdomain, count in word_map.items()]
        return output