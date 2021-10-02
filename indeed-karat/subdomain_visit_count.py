from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        result = {}
        for domain in cpdomains:
            splitted_domain_count = domain.split()
            splitted = splitted_domain_count[1].split(".")
            for index, word in enumerate(splitted):
                if ".".join(splitted[index:]) in result:
                    result[".".join(splitted[index:])] += int(splitted_domain_count[0])
                else:
                    result[".".join(splitted[index:])] = int(splitted_domain_count[0])
        final_result = []
        for domain_count in result:
            final_result.append(str(result[domain_count]) + " " + domain_count)
        return final_result
