class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        response = address.split('.')
        return '[.]'.join(response)