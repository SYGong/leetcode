class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1, l2 = map(len, [num1, num2])
        lp = l1 + l2   
        product = [0] * lp 
        # product[0] for possible carry
        for i in range(l1):
            for j in range(l2):
                product[i + j + 1] += int(num1[i]) * int(num2[j])
        for i in reversed(range(lp)):    
                product[i - 1] += product[i] // 10
                product[i] %= 10
        while len(product) > 1 and product[0] == 0:
            product.popleft()
        return "".join(map(str, product))

def main():
    print(Solution().multiply('3','4'))

if __name__ == "__main__":
    main()
