public class Solution {
    public int DistMoney(int money, int children) {
        if(money < children || (money == 4 && children == 1))
            return -1;
        money -= children;
        int givemax = money/7;
        int rem = money%7;
        if(givemax > children){
            rem += (givemax-children)*7;
            givemax = children;
        }
        if((rem == 3 && givemax == children-1) ||(givemax == children && rem>0)){
            givemax = Math.Max(givemax-=1,0);
        }
        return Math.Min(givemax, children);
    }
}