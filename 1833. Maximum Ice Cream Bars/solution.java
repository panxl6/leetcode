class Solution {
    public int maxIceCream(int[] costs, int coins) {
        Arrays.sort(costs);
        int count = 0;
        for (int item : costs) {
            coins -= item;
            if (coins >= 0) {
                count++;
            } else {
                break;
            }
        }
        return count;
    }
}
