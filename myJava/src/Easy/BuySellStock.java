package Easy;

public class BuySellStock {

    /**
     * You are given an integer array prices where prices[i] is the price of
     * NeetCoin on the ith day.
     * You may choose a single day to buy one NeetCoin and choose a different day in
     * the future to sell it.
     * Return the maximum profit you can achieve. You may choose to not make any
     * transactions, in which case the profit would be 0.
     * 
     * Example 1:
     * Input: prices = [10,1,5,6,7,1]
     * Output: 6
     * Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.
     * 
     * Example 2:
     * Input: prices = [10,8,7,5,2]
     * Output: 0
     * Explanation: No profitable transactions can be made, thus the max profit is
     * 0.
     * 
     * Constraints:
     * 1 <= prices.length <= 100
     * 0 <= prices[i] <= 100
     **/

    public static int maxProfit(int[] prices) {
        int max_profit = 0, left = 0, right = 1;

        while (right < prices.length) {
            if (prices[left] < prices[right]) {
                max_profit = Math.max(max_profit, prices[right] - prices[left]);
            } else {
                left = right;
            }
            right++;
        }
        return max_profit;
    }

    public static void main(String[] args) {
        int[] prices = new int[] { 7, 1, 3, 5, 6, 4 };
        int res = maxProfit(prices);

        System.out.println(res);
    }

}
