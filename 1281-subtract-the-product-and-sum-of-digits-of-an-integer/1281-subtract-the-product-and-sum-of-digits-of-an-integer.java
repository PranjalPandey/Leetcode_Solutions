class Solution {
    public int subtractProductAndSum(int n) {
        String s = String.valueOf(n);
        int prod = 1;
        int summ = 0;
        for(int i=0;i<s.length();i++){
           
            int x=s.charAt(i)-'0';
            prod*=x;
            summ+=x;
        }
        return prod-summ;
    }
}