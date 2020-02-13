class Solution:
    def defangIPaddr(self, address: str) -> str:
        new_addr = ''
        for x in range(len(address)):
            if address[x] != '.':
                new_addr += address[x]
            else:
                new_addr += "[.]"
        return new_addr
